# Audiolens
Audiolens is a two-channel audio beamforming application written in Python 3.
The intent is to take a stereo audio recording, find the prominent audio sources
in the recording, and use beamforming techniques to enhance the audio sources
for playback or saving to files.

Supported input audio file formats include:

* wav

Supported output audio file formats include:

* wav

## Requirements
The following applications and libraries are needed by Audiolens:

* Python 3.4.2 or later. 
  http://python.org, apt-get install python3
* numpy 1.8.2 or later.
  http://numpy.org, apt-get install python3-numpy.
* scipy 0.14.0 or later.
  http://scipy.org, apt-get install python3-scipy.
* matplotlib 1.3.1 or later.
  http://matplotlib.org, apt-get install python3-matplotlib.

Audiolens was written and tested on Ubuntu 14.10.

## References
The following sources were referenced during the creation of Audiolens:

* http://www.labbookpages.co.uk/audio/beamforming/delaySum.html
* Allred, Daniel. Evaluation and Comparison of Beamforming Algorithms for 
  Microphone Array Speech Processing. Masters Thesis, Georgia Institute of
  Technology. August 2006.
  http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.136.4516&rep=rep1&type=pdf
* Zhang Wenyi. Microphone Array Processing for Speech: Dual Channel 
  Localization, Robust Beamforming and ICA Analysis. PhD Dissertation,
  University of California, San Diego. 2010.
  https://escholarship.org/uc/item/8pb5353s

## License
Copyright 2015, Andrew Lin.
All rights reserved.
Licensed under the BSD 3-clause License. See LICENSE.txt or
<http://opensource.org/licenses/BSD-3-Clause>.
