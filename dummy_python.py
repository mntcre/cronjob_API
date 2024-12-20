# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:39:19 2024

@author: Mx
"""

from datetime import datetime
import os
import sys


# Getting the current date and time
dt = datetime.now()
date = str(dt.date())
time = str(dt.time())

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Change the working directory to the script's directory
#os.chdir(script_dir)
print(script_dir)

logtext = f'''Log-{dt} \n
Test Output \n 
----------------------------------\n'''

with open(script_dir + "/logfile.txt", "a") as output:
    output.write(logtext)



