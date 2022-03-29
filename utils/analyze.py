from rich.table import Table
import itertools

from utils.graphs import check_plagiarism


def analyze(graphs, log_all):

    permutations = list(itertools.combinations(graphs.keys(), 2))

    table = Table(title="Results")
    table.add_column("Submission A")
    table.add_column("Submission B")
    table.add_column("Plagiarism Check")
    for perm in permutations:
        a, b = perm
        graph_a = graphs.get(a)
        graph_b = graphs.get(b)

        if check_plagiarism(graph_a, graph_b):
            table.add_row(a, b, ":red_circle:")
        elif log_all:
            table.add_row(a, b, ":green_circle:")
    return table
