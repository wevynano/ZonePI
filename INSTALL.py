#!/usr/bin/python3
# -*- coding:utf-8 -*-

import platform

if platform.uname().system == "Linux":
    os.system('sudo pip3 install colorama')
    os.system('sudo pip3 install requests')
    os.system('chmod +x zonepi.py')
    os.system('mv zonepi.py zonepi.py')