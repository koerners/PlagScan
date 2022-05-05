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
        _parser.add_argument("-t", "--Threads",
                             help="Number of threads used (default: 4).")

        _parser.add_argument("-o", "--Output",
                             help="CSV that contains all suspicious combinations (default: report.csv).")

        _parser.add_argument("-v", "--Verbose",
                             help="Print [all] results or only [suspicious] (default: suspicious).")

        # Read arguments from command line
        _args = _parser.parse_args()

        self._nr_of_threads = int(
            _args.Threads) if _args.Threads else 4
        self._language = _args.Language
        self._output = _args.Output if _args.Output else "report.csv"
        self._verbose = True if _args.Verbose == "all" else False

    @property
    def nr_of_threads(self) -> int:
        return self._nr_of_threads

    @property
    def language(self) -> int:
        return self._language

    @property
    def output(self) -> str:
        return self._output

    @property
    def verbose(self) -> bool:
        return self._verbose
