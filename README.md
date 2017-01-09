# Galaxy_v2

This is a project created by Sam Hollenbach as an independent research project at Macalester College.

The simulation began as a open ended project for my Modern Astronomy course during as a freshman. The first generation (Galaxy_v1) could only be visualized in 2D and had a very rudimentary Dark Matter approximation, as well as being very inefficient doing calculations. 

Galaxy_v1 can be found at https://github.com/samhollenbach/Galaxy

Galaxy can be run with either one or two galaxies at the moment, but infinitely scalable. The galaxy initializations can be found in the single_galaxy() and double_galaxy() methods. Follow the format in these methods to create your own galaxy/galaxies with the constants you desire.

Galaxy_v2 has been drasticly improved in simulation accuracy, code effciency, and visualization.


Notable features of v2:

-NFW Dark Matter Profile (learn more here: https://en.wikipedia.org/wiki/Navarro%E2%80%93Frenk%E2%80%93White_profile)

-Dark Matter analysis mode, to quickly determine how accurate the NFW profile is with specified constants

-3D visualization using the Python library matplotlib (Reader.py)

-Parallel processing ability using the Python library joblib

-All around improved code speed and readability


Contact me at shollenb@macalester.edu if you have any quesitons
