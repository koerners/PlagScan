import subprocess

def parseFiles():
    process = subprocess.Popen(['sh', '../parseFile.sh', 'c'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

