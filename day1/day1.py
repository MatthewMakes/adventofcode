#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "MSL"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from pprint import pprint


def main(args):
    """ Main entry point of the app """
    # Starting frequency is zero.
    frequency = 0

    # Read input file
    with open(args.inputfile, 'r') as inputfile:
        # Each line of the file is a frequency adjustment.
        for adjustment_text in inputfile.readlines():
            adjustment = int(adjustment_text)
            frequency += adjustment
    pprint('Final frequency is ' + str(frequency))



if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("inputfile", help="Input file")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)