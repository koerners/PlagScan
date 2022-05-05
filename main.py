import csv

from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich.text import Text

from utils.analyze import analyze
from utils.commandline import Commandline
from utils.files import parse_files
from utils.graphs import get_graphs

if __name__ == "__main__":
    commandline_args = Commandline()
    console = Console()

    console.print(
        Padding(Panel.fit(Text("Your submissions are beeing processed. \n Depending on the number of submissions and their complexity this may take some time.", justify="center")), (1, 0)))

    try:

        with Progress("[progress.description]{task.description}", SpinnerColumn(), TimeElapsedColumn()) as progress:
            task_parse = progress.add_task(
                "[red]Parsing source code...", start=True, total=1)
            task_load = progress.add_task(
                "[green]Loading graphs...", start=False, total=1)
            task_analyze = progress.add_task(
                "[cyan]Analyzing...", start=False, total=1)

            parse_files(commandline_args.language,
                        commandline_args.nr_of_threads)

            progress.update(task_id=task_parse, completed=1)
            progress.start_task(task_load)
            graphs = get_graphs('graphs', console)
            progress.update(task_id=task_load, completed=1)
            progress.start_task(task_analyze)
            table, report = analyze(graphs, commandline_args.verbose)
            progress.update(task_id=task_analyze, completed=1)
            progress.stop()
            console.print(Padding(table, (1, 0)))
            with open(f"submissions/{commandline_args.output}", "wt") as report_file:
                writer = csv.writer(report_file)
                writer.writerows(report)
                console.log(
                    f"[green]Report saved as {commandline_args.output}")
    except Exception as e:
        console.log(e, style="bold red")
