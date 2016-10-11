# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:32:33 2016

@author: welion
"""

#!/usr/bin/env python
from PIL import Image
import os
import os.path
import sys

path = sys.argv[1]

for root, dirs, files in os.walk(path):
    for f in files:
        fp = os.path.join(root, f)
        img = Image.open(fp)
        w, h = img.size
        try:
            img.resize((w/2, h/2)).save(os.path.join(path, f), "JPEG")
        except Exception :
            pass
        print "Resize OK"
