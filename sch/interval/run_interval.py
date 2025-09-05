import argparse
import os
from time import sleep

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, help='Script name')
    parser.add_argument('interval', type=int, help='Interval in seconds')
    args = parser.parse_args()
    while True:
        if args.name.endswith('.py'):
            os.system('python '+ args.name)
        else:
            os.system(args.name)
        sleep(args.interval)
