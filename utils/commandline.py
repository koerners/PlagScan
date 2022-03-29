import argparse


class Commandline:
    def __init__(self):
        # Initialize parser
        _parser = argparse.ArgumentParser()

        _parser.add_argument(
            "-l",
            "--Language",
            required=True,
            help="Programming language that is beeing parsed. \
            Options: c, python",
        )

        # Adding optional argument
        _parser.add_argument("-p", "--Processes",
                             help="Number of processes used")

        _parser.add_argument("-o", "--Output",
                             help="Outputfile (default: report.md)")

        _parser.add_argument("-j", "--Parse",
                             help="Parse sourcecode [y]/n")

        # Read arguments from command line
        _args = _parser.parse_args()

        self._nr_of_processes = int(
            _args.Processes) if _args.Processes else None
        self._language = _args.Language
        self._parse = True if _args.Parse == "y" else False
        self._output = _args.Output if _args.Output else "report.md"

    @property
    def nr_of_processes(self) -> int:
        return self._nr_of_processes

    @property
    def language(self) -> int:
        return self._language

    @property
    def parse(self) -> int:
        return self._parse

    @property
    def output(self) -> str:
        return self._output
