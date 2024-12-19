# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:39:19 2024

@author: Mx
"""

from datetime import datetime

# import os
# from bs4 import BeautifulSoup

# Getting the current date and time
dt = datetime.now()
date = str(dt.date())
time = str(dt.time())

filepath = __file__[:__file__.rfind('\\')+1]


logtext = f'''Log-{dt} \n
Test Output \n 
----------------------------------\n'''

with open(filepath + "logfile.txt", "a") as output:
    output.write(logtext)



