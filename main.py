from datetime import datetime
import itertools
from utils.commandline import Commandline
from utils.files import parseFiles
from utils.graphs import check_plagiarism, get_graphs
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich.table import Table

console = Console()


def analyze(graphs):

    permutations = list(itertools.combinations(graphs.keys(), 2))

    console.print("Scanning for plagiarisms...")
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
            error = parseFiles(commandline_args.language,
                    commandline_args.nr_of_processes)
            if error:
                console.print(error, style="red")
            progress.update(task_id=task_parse, completed=1)
        progress.start_task(task_load)
        graphs = get_graphs('graphs')
        progress.update(task_id=task_load, completed=1)
        progress.start_task(task_analyze)
        table = analyze(graphs)
        progress.update(task_id=task_analyze, completed=1)
        progress.stop()
        console.print(table)
        with open(f"submissions/{commandline_args.output}", "wt") as report_file:
            console2 = Console(file=report_file)
            console2.print(table)

