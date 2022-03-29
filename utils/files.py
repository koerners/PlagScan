import subprocess


def parseFiles(language='c', processes=4):
    process = subprocess.Popen(['sh', 'parseFile.sh', str(language), str(processes)],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stderr

