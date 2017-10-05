#!/usr/bin/env python3

import sys

args = sys.argv

if len(args) < 2:
    print('Usage:', args[0], "NAME [NAME2 ...]")
    sys.exit(1)

if len(args) == 2:
    print("Hello to the ", (len(args) - 1), " of you: ", args[1],"!",sep="")

if len(args) == 3:
    print("Hello to the ", (len(args) - 1), " of you: ", " and ".join(args[1:]),"!",sep="")

if len(args) > 3:
   print("Hello to the ", (len(args) - 1), " of you: ", ", ".join(args[1:-1]),", ", "and ", args[-1], "!", sep="")
