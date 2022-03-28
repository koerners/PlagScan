from networkx.algorithms import isomorphism
import itertools
from utils.graphs import get_graphs
import networkx as nx
GRAPHS = get_graphs('graphs')
permutations = list(itertools.combinations(GRAPHS.keys(), 2))
for a, b in permutations:
    graph_a = GRAPHS.get(a)
    graph_b = GRAPHS.get(b)
    # print(f'comparing {graph_a} to {graph_b}')

    GM = isomorphism.GraphMatcher(graph_a, graph_b)
    if GM.is_isomorphic():
        print(f"Plagiarism detected at {a, b}")

