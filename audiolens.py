"""
Copyright 2015, Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>.
"""
import argparse
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
    parser.add_argument(
        '--log',
        nargs='?',
        default=None,
        help='Path to log file.'
    )
    parser.add_argument(
        '--log-http',
        nargs='?',
        default=None,
        help='URI (host:port, no protocol) of network log receiver, if any.'
    )
    parser.add_argument(
        '-v',
        action='count',
        default=0
    )
    return parser.parse_args()


def configure_logging(args):
    log_levels = (log.WARNING, log.INFO, log.DEBUG, log.NOTSET)
    level = log_levels[min(args.v, len(log_levels) - 1)]
    settings = {
        'stream_settings': {
            'level': level
        }
    }
    return settings


def main():
    """Launch audiolens."""
    args = parse_command_line()
    with log.logger(**configure_logging(args)):
        _log.info('Audiolens starting with the following arguments: %s', args)
        _log.critical('This is a critical message')
        _log.error('This is an error message')
        _log.warning('This is a warning message')
        _log.info('This is an info message')
        _log.debug('This is a debug message')
        _log.log(log.NOTSET, 'This message level is not set')
        try:
            raise ValueError()
        except ValueError:
            _log.exception('This is an exception message')


if __name__ =='__main__':
    main()

