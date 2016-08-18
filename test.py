#!/usr/bin/env python
# -*- coding: utf-8 -*-

from smart import *
from sys import exit

smart = SMARTManager()

devs = smart.get_devices()
for i in devs:
    print i.path + ": " + i.serial
