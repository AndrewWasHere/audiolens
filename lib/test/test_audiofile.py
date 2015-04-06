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


class AudiofileTestCase(unittest.TestCase):
    """Test audiofile interfaces."""
    @classmethod
    def setUpClass(cls):
        cls.gold_audio = os.path.join(
            os.path.dirname(__file__),
            'gold',
            'great_horned_owl.wav'
        )

    def test_non_audio(self):
        """Test read valid file, not audio."""
        with tempfile.NamedTemporaryFile() as tf:
            with open(tf.name, 'w') as f:
                f.write('Not a wav file.')

            with self.assertRaises(ValueError):
                audiofile.read(tf.name)

    def test_read_not_a_file(self):
        """Test read invalid file path."""
        with self.assertRaises(FileNotFoundError):
            audiofile.read('/not/a/valid/path')

    def test_read_wav(self):
        """Test read valid audio file."""
        datarate, data = audiofile.read(self.gold_audio)

        self.assertEqual(datarate, 44100)
        self.assertEqual(data.shape, (162630, 2))

    def test_write_wav(self):
        """Test write wav file."""
        datarate, data = audiofile.read(self.gold_audio)
        with tempfile.NamedTemporaryFile() as tf:
            audiofile.write(tf.name, datarate, data)
            datarate_prime, data_prime = audiofile.read(tf.name)

        self.assertEqual(datarate_prime, datarate)
        self.assertTrue(np.array_equal(data_prime, data))


if __name__ == '__main__':
    unittest.main(verbosity=2)
