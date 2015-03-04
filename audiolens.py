"""
Copyright 2015 Andrew Lin.

This file is part of Audiolens.

Audiolens is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Audiolens is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Audiolens.  If not, see <http://www.gnu.org/licenses/>.
"""
import argparse


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        nargs='?',
        default=None,
        help='Path to audio file to load.'
    )
    return parser.parse_args()


def main():
    """Launch audiolens"""
    args = parse_command_line()
    print(args)


if __name__ =='__main__':
    main()