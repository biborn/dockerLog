# A stand alone version

from os import system
from time import sleep
# Getting params from the CLI
from argparse import ArgumentParser

parser = ArgumentParser(description='Description of your program')
parser.add_argument('-c','--container', help='The id of the container', required=True)
parser.add_argument('-s','--second', help='The refresh interval rate', required=False, default="7")
args = vars(parser.parse_args())

while(1):
    system("clear")
    print("--dockerLog-StandAlone--------------------------------------------------")
    system("docker logs "+args["container"])
    sleep(int(args["second"]))