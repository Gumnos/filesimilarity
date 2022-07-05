#!/usr/local/bin/python3
from collections import defaultdict
from itertools import islice
import argparse
import re
import sys

THRESHOLD = 2

word_re = re.compile(r'\w+')

def build_parser():
    parser = argparse.ArgumentParser(
        description="Find similarities between files"
        )

    parser.add_argument("--threshold",
        metavar="VALUE", 
        type=int,
        default=5,
        help="Threshold for the number of triads that files must share",
        )
        
        
    parser.add_argument('files',
        metavar="files",
        nargs='+',
        help="files to compare",
        )
    return parser

def word_iter(f):
    for line in f:
        for word in word_re.finditer(line):
            yield word.group()

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def find_triads(fnames):
    data = defaultdict(lambda: defaultdict(int))

    for fname in fnames:
        with open(fname) as f:
            for triad in window(word_iter(f), 3):
                data[triad][fname] += 1
    return data

def main():
    args = build_parser().parse_args()
    data = find_triads(args.files)

    candidates = defaultdict(int)
    for triad, files2counts in data.items():
        if len(files2counts) > 1:
            files = tuple(sorted(files2counts))
            candidates[files] += 1

    candidate_list = [
        (triad, counts)
        for triad, counts in candidates.items()
        if counts >= args.threshold
        ]
    candidate_list.sort(key=lambda pair: pair[1])
    for candidate, count in candidate_list:
        print(f"{count}:{','.join(candidate)}")
        
if __name__ == "__main__":
    main()
