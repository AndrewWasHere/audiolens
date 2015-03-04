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
The following application and libraries are needed by Audiolens:

* Python 3.4.2 or later (http://python.org).
* numpy 1.8.2 or later (http://numpy.org) (sudo atp-get install python3-numpy).

Audiolens was written and tested on Ubuntu 14.10.

## References
The following sources were referenced during the creation of Audiolens:

* TBD

## License
Audiolens is Copyright 2015, Andrew Lin, and released under GPL 3.0.

Audiolens is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Audiolens is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

A copy of the GNU General Public License is available in the license.txt file
distributed with the Audiolens source.  If not, see 
<http://www.gnu.org/licenses/>.
