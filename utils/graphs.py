import os
import networkx as nx

from utils.iso import fix_labels

def get_graphs(directory):
    graphs = {}
    for filename in os.scandir(directory):
        if filename.is_dir():
            graphs[filename] = nx.Graph()

            for subgraph in os.scandir(filename.path):
                if subgraph.is_file():
                    new_graph = nx.Graph(nx.drawing.nx_pydot.read_dot(subgraph.path))
                    graphs[filename] = nx.compose(graphs[filename], new_graph )
            fix_labels(graphs[filename])

    return graphs

    
