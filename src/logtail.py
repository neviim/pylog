#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Instalnar dependencias pacotes:

	- Mac
	$ sudo easy_install pygtail 

	- Linux
	$ sudo pip  install pygtail
	$ sudo pip3 install pygtail


	- Uso:
	$ sudo python logtail.py

por: neviim jads
'''

import sys
from pygtail import Pygtail

for line in Pygtail("/var/log/system.log"):
    sys.stdout.write(line)	# equivale ao "print line"

