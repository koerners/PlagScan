import subprocess

def parseFiles(language='c'):
    process = subprocess.Popen(['sh', 'parseFile.sh', language],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

