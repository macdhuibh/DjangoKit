#DjangoKit

##Develpoment Environment Setup

First clone the repo and enter the DjangoKit directory.

		git clone https://github.com/macdhuibh/DjangoKit
		cd DjangoKit

Next we need to setup the PyObjC Bridge. Unfortunately pip can't seem to install pyobjc-core.
It throws an error like the following:

		class egg_info has no attribute 'iter_entry_points'

We need to install pyobjc-core with easy_install (this might take a while to compile)
If you aren't using virtualenv, you'll need to use sudo.

		easy_install pyobjc-core

The rest of PyObjC can be installed with pip. So we can install PyObC and the rest or our dependancies with:
Again, if you aren't using virtualenv, you'll need to use sudo.

		pip install -r requirements.txt

##Software version used
	python2.7
	PyObjC 2.3
	py2app 0.6.4
	MacOS X 10.6 Lion