"""
Copyright 2015 Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>. 
"""
from scipy.io import wavfile

from lib.albatross import log


_log = log.get_logger(__name__)


def read(filename):
    """Read audio file.

    Arguments:
        filename (str): Path to file to read.

    Returns:
        datarate (int): Sample rate (in samples/second).
        data (numpy.ndarray): Data read from wav file.

    Raises:
        FileNotFoundError: filename is not a file path.
        ValueError: filename is not a wav file.
    """
    _log.debug('%s.read(%s)', __name__, filename)

    return wavfile.read(filename)


def write(filename, datarate, data):
    """Write data to audio file.

    Arguments:
        filename (str): Path to file to write to.
        datarate (int): Sample rate (in samples/second).
        data (numpy.ndarray): Samples as a 1-D or 2-D numpy array of integers
            or float data type.
    """
    _log.debug('%s.write(%s, %s, %s)', __name__, filename, datarate, data)

    wavfile.write(filename, datarate, data)