# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:02:47 2020

@author: bmvol
"""

import requests as re
import shutil
from requests_html import HTMLSession

# def download_file(url):
#     local_filename = url.split('/')[-1]
#     with re.get(url, stream=True) as r:
#         with open(local_filename, 'wb') as f:
#             shutil.copyfileobj(r.raw, f)
#     return local_filename

def directory_crawl(url):
    """
    lista todos os subdiretórios, fazendo sentido ou não
    """
    root_url = 'http://dados.cvm.gov.br/dados'
    session = HTMLSession()
    r = session.get(url)
    tags = ['{0}{1}'.format(url,x) for x in r.html.links if x[-4:] in ['.csv', '.zip']]
    if len(tags) == 0:
        tags = False
    else:
        tags = [x for x in tags if '//' not in x.split(root_url)[1]]
    return tags

def download_file(url):
    r = requests.get(url).content
    return r