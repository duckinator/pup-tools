import argparse
import sys

def parseargs(args=None):
    parser = argparse.ArgumentParser(description='Sort lines fed via stdin.')
    parser.add_argument('--key',
                        help='Function to use for key sorting.')
    parser.add_argument('--reverse', '-r', action='store_true',
                        help='Perform a reversed sort.')
    parser.add_argument('--separator', '-s',
                        help='Use the provided value instead of newlines.')

    return parser.parse_args(args)

def main(args=None):
    opts = parseargs(args)
    key  = opts.key
    sep  = opts.separator

    if isinstance(key, str):
        key = eval(key)

    if sep is None:
        sepfn = str.splitlines
    else:
        sepfn = lambda x: x.split(sep)

    vals = sepfn(sys.stdin.read())
    ret = sorted(vals, key=key)
    if opts.reverse:
        ret = reversed(ret)

    print(*ret, sep='\n')
    return 0

if __name__ == '__main__':
    sys.exit(main())
