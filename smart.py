#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from device import *

class SMARTManager(object):
    def execute(self, cmd):
        return subprocess.Popen(cmd.split(), stdout=subprocess.PIPE).communicate()[0].strip()

    def get_devices(self):
        output = self.execute("smartctl --scan")

        dev_list = []

        for line in output.split('\n'):
            d = SMARTDevice()
            d.path = line.split('#')[1].split(',')[0].strip()
            d.dev_type = line.split('#')[1].split(',')[1].strip()
            d.smart_attributes = self.get_smart_attributes(d.path).split('\n')[6:]

            for a in d.smart_attributes:
                if a.strip().startswith("194 Temperature_Celsius"):
                    d.temp = int(a.split()[9].strip())
                elif a.strip().startswith("9 Power_On_Hours"):
                    d.power_on_hours = int(a.split()[9].strip())
            
            d.health_status = self.get_health_info(d.path).split("SMART overall-health self-assessment test result:")[1].strip()

            for line in self.get_device_info(d.path).split('\n'):
                if "Model Family" in line:
                    d.model_family = line.split(":", 1)[1].strip()
                elif "Device Model" in line:
                    d.device_model = line.split(":", 1)[1].strip() 
                elif "Serial Number" in line:
                    d.serial = line.split(":", 1)[1].strip()
                elif "Firmware Version" in line:
                    d.firmware_version = line.split(":", 1)[1].strip()
                elif "User Capacity" in line:
                    d.user_capacity = line.split(":", 1)[1].strip()
                elif "Sector Size" in line:
                    d.sector_size = line.split(":", 1)[1].strip()
                elif "Rotation Rate" in line:
                    d.rotation_rate = line.split(":", 1)[1].strip()
                elif "Form Factor" in line:
                    d.form_factor = line.split(":", 1)[1].strip()
                elif line.startswith("ATA Version"):
                    d.ata_version = line.split(":",1)[1].strip()
                elif "SATA Version" in line:
                    d.sata_version = line.split(":", 1)[1].strip()

            dev_list.append(d)

        return dev_list

    def get_smart_attributes(self, path):
        return self.execute("smartctl -A " + path)

    def get_device_info(self, path):
        return self.execute("smartctl -i " + path)

    def get_health_info(self, path):
        return self.execute("smartctl -H "+path)