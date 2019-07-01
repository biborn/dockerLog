from os import system
import time, argparse
from subprocess import Popen, PIPE, STDOUT

# Initialize the arguments
prs = argparse.ArgumentParser()

prs.add_argument('-c', '--container', help='Container ID', type=str)
prs.add_argument('-t', '--time', help='Refresh time', type=str, default="5")
prs.add_argument('-d', '--do', help='What the dockerLog is suppose to really do.', type=str) # 

prs = prs.parse_args()

proc = Popen(['docker', 'logs', str(prs.container)], stdout=PIPE, stderr=STDOUT)
output = str(proc.communicate()[0])
print (str(output))

# system("docker logs "+str(prs.container))
