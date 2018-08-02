#!/usr/bin/env python3

import inspect
import sys
from xml.etree import ElementTree

def main(argv=None):
    """
    Usage: python3 -m pup.xpath QUERY [QUERY...]

    Where
        - Each QUERY is a valid XPath query.
        - An XML document is provided via stdin.
    """

    if argv is None:
        argv = sys.argv

    if len(argv) < 2 or argv[1] == "-h" or argv[1] == "--help":
        print(inspect.getdoc(main), file=sys.stderr)
        return 1

    doc = ElementTree.parse(sys.stdin)
    for arg in argv[1:]:
        print(doc.findtext(arg))
    return 0

if __name__ == "__main__":
    exit(main())
