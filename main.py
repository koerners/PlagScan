
from utils.analyze import analyze
from utils.commandline import Commandline
from utils.files import parseFiles
from utils.graphs import get_graphs
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich.panel import Panel
from rich.padding import Padding
from rich.text import Text
if __name__ == "__main__":
    commandline_args = Commandline()
    console = Console()

    console.print(
        Padding(Panel.fit(Text("Your submissions are beeing processed. Depending on the number of submissions and their complexity this may take some time. \nConsider using the --Processes commandline option to improve speed.", justify="center")), (1, 1)))

    try:

        with Progress("[progress.description]{task.description}", SpinnerColumn(), TimeElapsedColumn()) as progress:
            if commandline_args.parse:
                task_parse = progress.add_task(
                    "[red]Parsing source code...", start=True, total=1)
            task_load = progress.add_task(
                "[green]Loading graphs...", start=False, total=1)
            task_analyze = progress.add_task(
                "[cyan]Analyzing...", start=False, total=1)

            if commandline_args.parse:
                parseFiles(commandline_args.language,
                           commandline_args.nr_of_processes)

                progress.update(task_id=task_parse, completed=1)
            progress.start_task(task_load)
            graphs = get_graphs('graphs')
            progress.update(task_id=task_load, completed=1)
            progress.start_task(task_analyze)
            table = analyze(graphs)
            progress.update(task_id=task_analyze, completed=1)
            progress.stop()
            console.print(Padding(table, (1, 1)))
            with open(f"submissions/{commandline_args.output}", "wt") as report_file:
                console2 = Console(file=report_file)
                console2.print(table)
    except Exception as e:
        console.log(e, style="bold red")
