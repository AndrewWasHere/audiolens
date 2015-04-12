"""
Copyright 2015 Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>. 
"""
import argparse
import os
from lib.albatross import log
from lib.albatross import path


_log = log.get_logger(__name__)


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        nargs='?',
        default=None,
        help='Path to audio file to load.'
    )
    parser.add_argument(
        '--log',
        nargs='?',
        default=None,
        help='Path to log file.'
    )
    parser.add_argument(
        '-v',
        action='count',
        default=0
    )

    args = parser.parse_args()

    if args.filepath:
        args.filepath = path.abs_path(args.filepath)
    if args.log:
        args.log = path.abs_path(args.log)

    return args


def configure_logging(args):
    log_levels = (log.WARNING, log.INFO, log.DEBUG, log.NOTSET)
    level = log_levels[min(args.v, len(log_levels) - 1)]
    settings = {
        'stream_settings': {
            'level': level
        }
    }
    if args.log:
        settings['file_settings'] = {
            'path': os.path.abspath(os.path.expanduser(args.log))
        }

    return settings


def main():
    """Launch audiolenscli."""
    args = parse_command_line()
    with log.logger(**configure_logging(args)):
        _log.info('Audiolens starting with the following arguments: %s', args)

if __name__ =='__main__':
    main()
