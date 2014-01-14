import sys
import subprocess

command_process = subprocess.Popen(
    ['sqlcmd', '-V1', '-H', 'localhost', '-d', 'DATABASENAME', '-i', sys.argv[1], '-U', 'sa', '-P', 'xxx'],
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
command_output = command_process.communicate()[0]

print command_output