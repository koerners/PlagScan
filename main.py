import itertools
from utils.commandline import Commandline
from utils.files import parseFiles
from utils.graphs import check_plagiarism, get_graphs
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich.table import Table

console = Console()


def analyze(GRAPHS):

    permutations = list(itertools.combinations(GRAPHS.keys(), 2))

    console.print("Scanning for plagiarisms...")
    table = Table(title="Results")
    table.add_column("Submission A")
    table.add_column("Submission B")
    table.add_column("Plagiarism Check")
    for graphs in permutations:
        a, b = graphs
        graph_a = GRAPHS.get(a)
        graph_b = GRAPHS.get(b)

        if check_plagiarism(graph_a, graph_b):
            table.add_row(a, b, ":red_circle:")
        else:
            table.add_row(a, b, ":green_circle:")
    return table


if __name__ == "__main__":
    commandline_args = Commandline()
    with Progress("[progress.description]{task.description}", SpinnerColumn(), TimeElapsedColumn()) as progress:
        if commandline_args.parse:
            task_parse = progress.add_task(
                "[red]Parsing source code...", start=True, total=1)
        task_load = progress.add_task(
            "[green]Loading graphs...", start=False, total=1)
        task_analyze = progress.add_task(
            "[cyan]Analyzing...", start=False, total=1)

        if commandline_args.parse:
            parseFiles('c')
            progress.update(task_id=task_parse, completed=1)
        progress.start_task(task_load)
        graphs = get_graphs('graphs')
        progress.update(task_id=task_load, completed=1)
        progress.start_task(task_analyze)
        table = analyze(graphs)
        progress.update(task_id=task_analyze, completed=1)
        console.print(table)
