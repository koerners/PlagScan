import itertools

from networkx.algorithms import isomorphism
from rich.table import Table


def analyze(graphs, log_all):
    """
    Function to analyze the similarity of graphs

    Arguments:
        graphs: a dict of graphs that should be tested
        log_all: print also non susupicious results to the console
    Returns:
        table: Table object that is printed to the console
        results: list of suspicous pairs for saving to a file
    """

    permutations = list(itertools.combinations(graphs.keys(), 2))

    results = []
    table = Table(title="Results")
    table.add_column("Submission A")
    table.add_column("Submission B")
    table.add_column("Plagiarism Check")
    for perm in permutations:
        a, b = perm
        graph_a = graphs.get(a)
        graph_b = graphs.get(b)

        if graph_a is None or graph_b is None:
            continue

        if check_plagiarism(graph_a, graph_b):
            table.add_row(a, b, ":red_circle:")
            results.append([a, b])
        elif log_all:
            table.add_row(a, b, ":green_circle:")
            
    return table, results


def check_plagiarism(graph_a, graph_b):
    # Some more sophisticated logic could be used here.
    # However, this simple check has proven to work really well.
    GM = isomorphism.GraphMatcher(graph_a, graph_b)
    return GM.is_isomorphic()
