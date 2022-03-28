import itertools
from utils.graphs import get_graphs
import networkx as nx

GRAPHS = get_graphs('graphs')

permutations = list(itertools.permutations(GRAPHS.keys(), 2))
for a, b in permutations:
    graph_a = GRAPHS.get(a)
    graph_b = GRAPHS.get(b)
    print(f'comparing {graph_a} to {graph_b}')
    sim = nx.graph_edit_distance(graph_a, graph_b)
    print(sim)


