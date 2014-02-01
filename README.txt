Project by poplav92 (Michael Poplavski)
Acknowledgments to Tigge & dtcooper
Code from their repositories at:
https://github.com/Tigge/Garmin-Forerunner-610-Extractor
https://github.com/dtcooper/python-fitparse

==============================================================================

Features:

Analyze your avg speed, distance, monthly miles, and normalized effort or run difficulty (actual distance vs projected distance given avg speed or runs) throughout time!

==============================================================================

Requirements:

*nix based system

R

Python 2.7+

PyUSB → Install via:
pip install pyusb

ANT USBStick

Garmin ANT-FS device (should cover most of Garmin's products this is built specifically for the Forerunner series)

==============================================================================

Usage:

Place GarminDataAgent in your home directory!

Sudo bash MainController.sh

You should see the visualizations in the GarminDataAgent/Output folder.

Note:  I ran this with my data so you should see a filled garmin_data.csv file and visualizations in the Output folder.  When you want to flush all the data and start loading back everything on your device you need to erase the previous .fit files in the activity folder at ~/.config/garmin-extractor/3863488130/activites/ as well as GarminDataAgent/FitActivities.

==============================================================================

Screenshots:

Still need to upload them, I will get to that soon.
As of now see samples in Output folder.

==============================================================================

Further Info:

Email me questions, suggestions, or open source project collaboration ideas
