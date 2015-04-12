"""
Copyright 2015, Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>.
"""
import argparse
import os
from lib.albatross import log


_log = log.get_logger(__name__)


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        nargs='?',
        default=None,
        help='Path to audio file to load.'
    )
    log.add_log_parser_arguments(parser)
    return parser.parse_args()


def main():
    """Launch audiolens."""
    args = parse_command_line()
    with log.logger(**log.configure_logging(args)):
        _log.info('Audiolens starting with the following arguments: %s', args)

if __name__ =='__main__':
    main()

