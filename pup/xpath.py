#!/usr/bin/env python3

import inspect
import sys
from xml.etree import ElementTree

def match(text, *queries):
    doc = ElementTree.parse(text)
    return [doc.findtext(query) for query in queries]

def _main(argv=None):
    """
    Usage: python3 -m pup.xpath QUERY [QUERY...]

    Where
        - Each QUERY is a valid XPath query.
        - An XML document is provided via stdin.
    """

    if argv is None:
        argv = sys.argv

    args = argv[1:] # Drop the process name.

    if len(args) < 1 or "-h" in args or "--help" in args:
        print(inspect.getdoc(_main), file=sys.stderr)
        return 1

    print("\n".join(match(sys.stdin, *args)))
    return 0

if __name__ == "__main__":
    exit(_main())
