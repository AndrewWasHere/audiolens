"""
Copyright 2015 Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>. 
"""
import numpy as np
from lib.albatross import log


_log = log.get_logger(__name__)


class BeamFormer():
    """Audio Beam Former."""
    def __init__(self):
        self._l_channel = None
        self._r_channel = None
        self._autocorrelation = None
        self._sources = []

    def process(self, audio):
        """Process audio file.

        Pull left and right channels out of an audio file and do the
        autocorrelation.

        Args:
            audio (np.ndarray): two-channel audio.
        """
        _log.debug('%s.process(%s)', self.__class__.__name__, audio)

        # Process audio.
        self._l_channel = np.zeros(0)
        self._r_channel = np.zeros(0)
        self._autocorrelation = np.correlate(
            self._l_channel,
            self._r_channel,
            mode='full'
        )

        # Identify sources.

    def sources(self):
        """Number of sources found in audiofile."""
        _log.debug('%s.source()', self.__class__.__name__)

        return len(self._sources)

    def audio(self, source=None):
        """Get audio for source.

        Returns the single-channel audio for the specified source. If source
        is None, return the original audio (as one channel). Otherwise, return
        the specified source.

        Args:
            source (int, str, None): Audio source to return.
                None => Original audio (as one channel).
                'l' => Original audio, left channel only.
                'r' => Original audio, right channel only.
                Otherwise => Beam formed audio for source.
        """
        _log.debug('%s.audio(%s)', self.__class__.__name__, source)

        if source is None:
            # Original audio as one channel.
            return None

        elif source == 'l':
            # Left channel.
            return self._l_channel[:]

        elif source == 'r':
            # Right channel.
            return self._r_channel[:]

        else:
            # Source.
            return self._extract_source(source)

    def _extract_source(self, source):
        """Extract source audio.

        Beam form and extract source audio.
        """
        _log.debug('%s._extract_source(%s)', self.__class__.__name__, source)

        source = self._sources[source]
        pad = np.zeros(abs(source.phase))
        if source.phase < 0:
            left = np.concatenate((self._l_channel, pad))
            right = np.concatenate((pad, self._r_channel))

        elif source.phase > 0:
            left = np.concatenate((pad, self._l_channel))
            right = np.concatenate((self._r_channel + pad))

        else:
            left = self._l_channel
            right = self._r_channel

        return left + right