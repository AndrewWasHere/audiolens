"""
Copyright 2015 Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>.
"""
import os
import tempfile
import unittest

import numpy as np

from lib import audiofile
from lib.albatross.path import abs_path


class AudiofileTestCase(unittest.TestCase):
    """Test audiofile interfaces."""
    @classmethod
    def setUpClass(cls):
        cls.gold_audio = abs_path(
            os.path.join('gold', 'great_horned_owl.wav'),
            root=__file__
        )

    def test_read_non_audio(self):
        """Test read valid file, not audio."""
        with tempfile.NamedTemporaryFile() as tf:
            with open(tf.name, 'w') as f:
                f.write('Not a wav file.')

            with self.assertRaises(ValueError):
                audiofile.read(tf.name)

    def test_read_not_a_file(self):
        """Test read invalid file path."""
        with self.assertRaises(FileNotFoundError):
            audiofile.read(
                abs_path(
                    os.path.join('not', 'a', 'valid', 'path'),
                )
            )

    def test_read_wav(self):
        """Test read valid audio file."""
        datarate, data = audiofile.read(self.gold_audio, False)

        self.assertEqual(datarate, 44100)
        self.assertEqual(data.shape, (162630, 2))

        # Verify default for separate_channels parameter.
        datarate_prime, data_prime = audiofile.read(self.gold_audio)

        self.assertEqual(datarate_prime, datarate)
        self.assertTrue(np.array_equal(data_prime, data))

        # Verify separate channels separates channels.
        datarate_prime, data_prime = audiofile.read(self.gold_audio, True)

        self.assertTrue(isinstance(data_prime, list))
        self.assertEqual(datarate_prime, datarate)
        self.assertEqual(len(data_prime), data.shape[1])
        for channel in range(data.shape[1]):
            self.assertTrue(
                np.array_equal(data[:, channel], data_prime[channel])
            )

    def test_write_wav(self):
        """Test write wav file."""
        datarate, data = audiofile.read(self.gold_audio)
        with tempfile.NamedTemporaryFile() as tf:
            audiofile.write(tf.name, datarate, data)
            datarate_prime, data_prime = audiofile.read(tf.name)

        self.assertEqual(datarate_prime, datarate)
        self.assertTrue(np.array_equal(data_prime, data))

    def test_write_wav_mono(self):
        """Test writing single channel wav file."""
        datarate, data = audiofile.read(self.gold_audio, True)
        ref_channel = data[0]
        with tempfile.NamedTemporaryFile() as tf:
            audiofile.write(tf.name, datarate, ref_channel)
            datarate_prime, data_prime = audiofile.read(tf.name)

        self.assertEqual(datarate_prime, datarate)
        self.assertTrue(np.array_equal(data_prime, ref_channel))

    def test_write_wav_channels(self):
        """Test writing wav file from separate channels."""
        datarate, data = audiofile.read(self.gold_audio, False)
        datarate_prime, data_prime = audiofile.read(self.gold_audio, True)

        self.assertTrue(isinstance(data_prime, list))

        with tempfile.NamedTemporaryFile() as tf:
            audiofile.write(tf.name, datarate_prime, data_prime)
            datarate_prime, data_prime = audiofile.read(tf.name, False)

        self.assertEqual(datarate_prime, datarate)
        self.assertTrue(np.array_equal(data_prime, data))


if __name__ == '__main__':
    unittest.main(verbosity=2)
