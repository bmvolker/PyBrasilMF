# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:02:47 2020

@author: bmvol
"""

import requests as re
import shutil

def download_file(url):
    local_filename = url.split('/')[-1]
    with re.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename
