#!/usr/bin/env python3
"""count the vowels in a word"""
import sys
from collections import Counter

args = sys.argv

if len(args) < 2:
    print("Usage:", args[0], "STRING")
    sys.exit(1)

c = Counter(args[1].lower())

numv = c["a"] + c["e"] + c["i"] + c["o"] + c["u"]

if numv == 1:
    sp = "vowel"
    ir = "is"
else:
    sp = "vowels"
    ir = "are"

print("There", ir, numv, sp, "in", '"'+args[1]+'."')

