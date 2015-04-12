"""
Copyright 2015 Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>.
"""
import os
import unittest
import numpy as np

from lib import audiofile
from lib.albatross import path
from lib.beamformer import BeamFormer


class TestBeamFormer(BeamFormer):
    """Have to derive a class since BeamFormer is an abstract base class."""
    def __init__(self, max_channels):
        super().__init__(max_channels)
        self.process_called = False
        self.audio = None

    def _process(self, audio):
        """Implements abstract method."""
        self.process_called = True
        self.audio = audio


class BeamFormerTestCase(unittest.TestCase):
    """Test BeamFormer via TestBeamFormer class."""
    @classmethod
    def setUpClass(cls):
        _, cls.gold_audio = audiofile.read(
            path.abs_path(
                os.path.join('gold', 'great_horned_owl.wav'),
                root=__file__
            ),
            separate_channels=False
        )

        _, cls.gold_audio_channels = audiofile.read(
            path.abs_path(
                os.path.join('gold', 'great_horned_owl.wav'),
                root=__file__
            ),
            separate_channels=True
        )

    def test_too_few_channels(self):
        bf = TestBeamFormer(None)
        with self.assertRaises(ValueError):
            bf.process(self.gold_audio_channels[:1])  # One channel of audio.

        with self.assertRaises(ValueError):
            bf.process(self.gold_audio_channels[0])  # Single channel ndarray.

    def test_too_many_channels(self):
        audio = self.gold_audio_channels * 2  # Four channels.
        bf = TestBeamFormer(3)
        with self.assertRaises(ValueError):
            bf.process(audio)

        with self.assertRaises(ValueError):
            bf.process(np.column_stack(audio))

    def test_ndarray_audio(self):
        bf = TestBeamFormer(None)
        bf.process(self.gold_audio)
        self.assertTrue(bf.process_called)
        for idx in range(len(self.gold_audio_channels)):
            self.assertTrue(
                np.array_equal(self.gold_audio_channels[idx], bf.audio[idx])
            )

    def test_list_audio(self):
        bf = TestBeamFormer(None)
        bf.process(self.gold_audio_channels)
        self.assertTrue(bf.process_called)
        self.assertEqual(len(self.gold_audio_channels), len(bf.audio))
        for idx in range(len(self.gold_audio_channels)):
            self.assertTrue(
                np.array_equal(self.gold_audio_channels[idx], bf.audio[idx])
            )


if __name__ == '__main__':
    unittest.main(verbosity=2)
