import os

import networkx as nx

from utils.fix_labels import fix_labels


def get_graphs(directory, console):
    graphs = {}
    for sub_directory in os.scandir(directory):
        if sub_directory.is_dir():
            filename = sub_directory.name
            graphs[filename] = nx.Graph()
            
            try:
                for subgraph in os.scandir(sub_directory.path):
                    if subgraph.is_file():
                        new_graph = nx.Graph(
                            nx.drawing.nx_pydot.read_dot(subgraph.path))
                        graphs[filename] = nx.compose(graphs[filename], new_graph)
                fix_labels(graphs[filename])  # to improve analyzing speed

            except Exception:
                console.log(f"{filename} is not a valid graph", style="bold red")
                graphs[filename] = None

    return graphs
