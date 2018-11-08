#!/usr/bin/python3

import argparse
import json
import grammar
import gluply
from oracle import Oracle

# Parse arguments for the program
parser = argparse.ArgumentParser(description='Runs an English-speaking chatbot that answers questions about your website')
parser.add_argument('conf_file', metavar='JSON_FILE', type=str, help='Read parameters for the program')

# Under which mode will the app run. There is no default mode, you need to choose one
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--train', dest='train', action='store_true', help='Precalculates everything')
group.add_argument('--run', metavar='SENTENCE', type=str, help="Answers to the given input")
args = parser.parse_args()

# Time to read the program parameters
with open(args.conf_file) as f:
    params = json.load(f)

if args.train:
    print(params['bibtex'])
else:
    parsed_input = gluply.read_input(args.run)
    print(parsed_input)
    chatbot = Oracle()
    print(chatbot.ask(parsed_input))
