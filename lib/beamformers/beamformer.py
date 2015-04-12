"""
Copyright 2015 Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>. 
"""
from abc import ABCMeta, abstractmethod
import numpy as np
from lib.albatross import log


_log = log.get_logger(__name__)


class BeamFormerError(Exception):
    """Error while beam forming."""


class BeamFormer(metaclass=ABCMeta):
    """Audio beam former base class."""
    def __init__(self, max_channels):
        self.max_channels = max_channels

    # Public Interfaces. #######################################################

    def process(self, audio):
        """Process audio file.

        Args:
            audio (np.ndarray or list of np.ndarray): multi-channel audio.

        Raises:
            ValueError: Problem with audio.
            BeamFormerError: Problem while processing audio.
        """
        _log.debug('%s.process(%s)', self.__class__.__name__, audio)

        # Process audio.
        if isinstance(audio, np.ndarray):
            _, channels = audio.shape
            audio = [audio[:, n] for n in range(channels)]

        n_channels = len(audio)
        if n_channels < 2:
            raise ValueError(
                'Not enough channels in audio to beam form. (found %d)',
                n_channels
            )

        elif self.max_channels and n_channels > self.max_channels:
            raise ValueError(
                'Too many channels in audio. There cannot be more than %d '
                'channels. Found %d.',
                self.max_channels,
                n_channels
            )

        self._process(audio)  # Derived class implementation.

    # Private methods. #########################################################

    @abstractmethod
    def _process(self, audio):
        """Process audio.

        This function is implemented in derived classes.

        Args:
            audio (list of np.ndarray): multi-channel audio.

        Raises:
            BeamFormerException (or a derivation thereof): Problem while
                processing audio.
        """
