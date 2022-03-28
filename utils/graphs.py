import os
import networkx as nx
from utils.iso import fix_labels
from networkx.algorithms import isomorphism

def get_graphs(directory):
    graphs = {}
    for sub_directory in os.scandir(directory):
        if sub_directory.is_dir():
            filename = sub_directory.name
            graphs[filename] = nx.Graph()

            for subgraph in os.scandir(sub_directory.path):
                if subgraph.is_file():
                    new_graph = nx.Graph(
                        nx.drawing.nx_pydot.read_dot(subgraph.path))
                    graphs[filename] = nx.compose(graphs[filename], new_graph )
            fix_labels(graphs[filename])

    return graphs


def check_plagiarism(graph_a, graph_b):
    GM = isomorphism.GraphMatcher(graph_a, graph_b)
    return GM.is_isomorphic()

    
