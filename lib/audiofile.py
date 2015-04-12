"""
Copyright 2015 Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>. 
"""
import numpy as np
from scipy.io import wavfile

from lib.albatross import log


_log = log.get_logger(__name__)


def read(filename, separate_channels=False):
    """Read audio file.

    Args:
        filename (str): Path to file to read.
        separate_channels (bool): Separate channels into vectors instead of
            returning a single data array

    Returns:
        datarate (int): Sample rate (in samples/second).
        data (numpy.ndarray, or list of numpy.ndarrays): Data read from wav
            file.

    Raises:
        FileNotFoundError: filename is not a file path.
        ValueError: filename is not a wav file.
    """
    _log.debug('%s.read(%s, %s)', __name__, filename, separate_channels)

    datarate, data = wavfile.read(filename)
    if separate_channels:
        _, channels = data.shape
        data = [data[:, n] for n in range(channels)]

    return datarate, data


def write(filename, datarate, data):
    """Write data to audio file.

    Args:
        filename (str): Path to file to write to.
        datarate (int): Sample rate (in samples/second).
        data (numpy.ndarray or list of numpy.ndarrays): Samples as a 1-D or 2-D
            numpy array of integers or float data type.
    """
    _log.debug('%s.write(%s, %s, %s)', __name__, filename, datarate, type(data))

    if isinstance(data, list):
        data = np.column_stack(data)

    wavfile.write(filename, datarate, data)