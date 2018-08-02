import sys
import argparse
import ast
import subprocess
import os
import astunparse
from typing import List

__all__ = ('main',)


def parseargs(args=None):
    parser = argparse.ArgumentParser(description='Evaluate a Python expression')
    parser.add_argument('imports', nargs='*',
                        help='Modules to import')
    parser.add_argument('expr',
                        help='Expression to evaluate')
    parser.add_argument('-p', '--python', default=sys.executable,
                        help='Python to use')
    parser.add_argument('-e', '--venv', action='store_true',
                        help='Use the active virtual environment')

    return parser.parse_args(args)


def find_binary(bin, use_venv):
    if use_venv and 'VIRTUAL_ENV' in os.environ:
        # FIXME: Do the Windows version of this
        return os.path.join(os.environ['VIRTUAL_ENV'], 'bin', 'python')
    else:
        return bin


def build_imports(modules):
    return [
        ast.ImportFrom(module=mod, names=[ast.alias(name='*', asname=None)], level=0)
        for mod in modules
    ]


def build_print_repr(expr):
    return [
        ast.Expr(
            value=ast.Call(
                func=ast.Name(id='print', ctx=ast.Load()), 
                args=[ast.Call(
                    func=ast.Name(id='repr', ctx=ast.Load()),
                    args=[expr],
                    keywords=[],
                )],
                keywords=[],
            )
        )
    ]


def recompile(code, imports):
    expr = ast.parse(code, filename='<args>', mode='eval')
    return ast.Module(build_imports(imports) + build_print_repr(expr.body))


def main(args: List[str]=None) -> int:
    opts = parseargs(args)
    bin = find_binary(opts.python, opts.venv)
    tree = recompile(opts.expr, opts.imports)
    code = astunparse.unparse(tree)

    proc = subprocess.run([bin, '-c', code])
    return proc.returncode


if __name__ == '__main__':
    sys.exit(main())
