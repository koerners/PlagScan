import subprocess


def parseFiles(language='c', processes=4):
    process = subprocess.Popen(['sh', 'parseFile.sh', str(language), str(processes)],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        raise Exception(
            "Error when reading the submissions. Please make sure the folder is mounted correctly.")
