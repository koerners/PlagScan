import argparse


class Commandline:
    def __init__(self):
        # Initialize parser
        _parser = argparse.ArgumentParser()

        _parser.add_argument(
            "-l",
            "--Language",
            required=True,
            help="Programming language that is beeing used. \
            Options: c, python",
        )

        # Adding optional argument
        _parser.add_argument("-p", "--Processes",
                             help="Number of processes used.")

        _parser.add_argument("-o", "--Output",
                             help="Outputfile (default: report.md).")

        _parser.add_argument("-v", "--Verbose",
                             help="Print [all] results or only [suspicious] (default: suspicious).")

        _parser.add_argument("-sp", "--SkipParse",
                             help="[DEBUG] Skip code parsing [y/n] (default: n).")

        # Read arguments from command line
        _args = _parser.parse_args()

        self._nr_of_processes = int(
            _args.Processes) if _args.Processes else 1
        self._language = _args.Language
        self._parse = False if _args.SkipParse == "y" else True
        self._output = _args.Output if _args.Output else "report.md"
        self._verbose = True if _args.Verbose == "all" else False

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

    @property
    def verbose(self) -> bool:
        return self._verbose
