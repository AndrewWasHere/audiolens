"""
Copyright 2015 Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>. 
"""
import argparse

from lib.albatross import log
from lib.albatross import path


_log = log.get_logger(__name__)


def parse_command_line():
    parser = argparse.ArgumentParser()
    log.add_log_parser_arguments(parser)
    subparsers = parser.add_subparsers()

    args = parser.parse_args()
    if args.log:
        args.log = path.abs_path(args.log)
    return args


def main():
    """Run an experiment."""
    args = parse_command_line()
    with log.logger(**log.configure_logging(args)):
        args.func(args)

if __name__ == '__main__':
    main()