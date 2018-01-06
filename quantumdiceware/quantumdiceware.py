"""
Diceware passphrases generated from quantum random data.
http://github.com/justinsloan/qdg

Requires Python 3.6 or better

Features:
    - Simulates dice rolls by gathering quantum data.
    - Includes the complete standard Diceware wordlist.
    - Generate passphrases from custom wordlists.

Usage:
    >>> $ pip3 install quantumdiceware
    >>> $ qdg
    >>> $ qdg -c 6 > output.txt

Version History:
0.1.9 - DATE
- added version option

0.1.8 - 5 JAN 2017
- first build
"""

__version__ = "0.1.8"

import random
import argparse
import quantumrandom
import pkg_resources

# Specify the location of the word list inside the package
resource_name = __name__
path = "diceware_word_list.txt"
word_list_file = pkg_resources.resource_filename(resource_name, path)

# Build the argument parser
parser = argparse.ArgumentParser(
    description="Generate Diceware passphrases using quantum data.",
    epilog=f"QDG v.{__version__} | by Justin M. Sloan")
parser.add_argument("-c","--count",nargs="?",default=1,type=int, help="number of passphrases to generate")
parser.add_argument("-w","--words",nargs="?",default=6,type=int, help="number of words per passphrase")
parser.add_argument("-v","--verbose",action="store_true", help="increase output verbosity")
parser.add_argument("-l","--local",action="store_false", help="use local random data, no connection required (faster)")
parser.add_argument("-f","--file",nargs="?",default=word_list_file, help="specify the word list to use")
parser.add_argument("--version",action="version",version=f"QDG v.{__version__}")
args = parser.parse_args()

# Load the word list file
word_dict = {}
with open(args.file) as f:
    for line in f.readlines():
        index, word = line.strip().split('\t')
        word_dict[int(index)] = word


def generate_diceware_phrase(word_count=6, quantum=True, verbose=False):
    """Generates a Diceware Passphrase of length N."""
    passphrase = []

    if quantum:
        if verbose:
            print("Gathering quantum data...".ljust(38))
        data_count = word_count * 5
        quantum_data = quantumrandom.uint16(data_count)
        dice = (int("".join([str(y) for y in (quantum_data % 6) + 1])))
        roll = [str(dice)[i:i+5] for i in range(0, len(str(dice)), 5)]
        for i in roll:
            if verbose:
                print(f"Dice Rolls: {i}")
            passphrase.append(word_dict[int(i)])
    else:
        if verbose:
            print("Using local random data...")
        for words in range(0, word_count):
            this_index = 0
            for position in range(0, 5):
                digit = random.randint(1, 6)
                this_index += digit * pow(10, position)
            passphrase.append(word_dict[this_index])
            if verbose:
                print(f"Dice Rolls: {this_index}")
    return ' '.join(passphrase)   


def main():
    """Takes optional arguments and prints passphrases."""

    # Loop until requested number of passphrases are generated
    for i in range(0,args.count):
        phrase = generate_diceware_phrase(args.words, args.local, args.verbose)
        print(phrase)
