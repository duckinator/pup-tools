#!/usr/bin/env python3

import inspect
import sys
import urllib.request

def fetch(method, url):
    method = method.upper()
    request  = urllib.request.Request(url, method=method)
    response = urllib.request.urlopen(request)
    return response

def _main(argv=None):
    """
    Usage: python3 -m pup.http [METHOD] URL

    Where
        - METHOD is `get`. (DEFAULT: get.)
            - TODO: Support literally anything else.
        - URL is the URL to request.
    """

    if argv is None:
        argv = sys.argv

    args = argv[1:] # Drop the process name.

    if len(args) < 1 or len(args) > 2 or "-h" in args or "--help" in args:
        print(inspect.getdoc(_main), file=sys.stderr)
        return 1

    if len(args) == 2:
        method = args[0]
        url = args[1]
    else:
        method = "get"
        url = args[0]

    contents = fetch(method, url).read().decode()
    print(contents)

    return 0

if __name__ == "__main__":
    exit(_main())
