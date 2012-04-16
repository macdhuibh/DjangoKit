#DjangoKit

This is a friendly fork of Tom Insam's DjangoKit.

		https://code.google.com/p/djangokit/
		http://movieos.org/code/djangokit/
		http://movieos.org/blog/2007/djangokit-gets-better/

I forked it here in an attempt to get it up and running on my Lion box with Python2.7 and Django 1.3+.

DjangoKit is a framework that will take a Django application, and turn it into a stand-alone MacOS application with a local database and media files.

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
	django 1.3+
	MacOS X 10.6 Lion