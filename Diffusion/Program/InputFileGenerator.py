# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:38:20 2015

@author: Timothy
"""

#alternative is to import os and call a subprocess
import json


name = raw_input('Enter name of input file: ') + '.txt'
file = open(name, 'w+')

userInput = {"Lx" : 1000 ,
			"nx" : 1000 ,
			"rebarDepth" :  ,
			"corrosionInitiation" :  ,
			"" :  ,	
			"" :  ,
			"" :  ,
            }

json.dump(userInput, file)

file.close