import requests, argparse, sys, re
parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')
parser.add_argument('-c', '--count')      # option that takes a value


args = parser.parse_args()
print(args.count)