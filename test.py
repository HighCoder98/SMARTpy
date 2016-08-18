#!/usr/bin/env python
# -*- coding: utf-8 -*-

from smart import *

smart = SMARTManager()

devs = smart.get_devices()
for i in devs:
    print i.path + ": " + i.serial
