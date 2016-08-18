#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SMARTDevice(object):
    name = None
    dev_type = None
    path = None
    model_family = None
    device_model = None
    serial = None
    firmware_version = None
    user_capacity = None
    sector_size = None
    rotation_rate = None
    form_factor = None
    sata_version = None
    ata_version = None
    smart_attributes = None
    temp = None
    health_status = None
    power_on_hours = None
   
    # def __init__(self, name, serial, temp, max_temp, min_temp):
    #     self.name = name
    #     self.serial = serial
    #     self.temp = temp
    #     self.max_temp = max_temp
    #     self.min_temp = min_temp