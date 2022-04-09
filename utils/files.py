import subprocess


def parse_files(language, threads):
    process = subprocess.Popen(['sh', 'parseFile.sh', str(language), str(threads)],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        raise Exception(
            "Error when reading the submissions. Please make sure the folder is mounted correctly.")
