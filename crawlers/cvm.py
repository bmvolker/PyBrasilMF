# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:20:45 2020

@author: bmvolker
"""

import requests as re
from lxml import html
from requests_html import HTMLSession
from utils import *
from tqdm import tqdm


def directory_crawl(url):
    """
    lista todos os subdiretórios, fazendo sentido ou não
    """
    root_url = 'http://dados.cvm.gov.br/dados'
    # url_aux = '{0}{1}'.format(url, tag)
    session = HTMLSession()
    r = session.get(url)
    tags = ['{0}{1}'.format(url,x) for x in r.html.links if '?' not in x]
    if len(tags) == 0:
        tags = False
    else:
        tags = [x for x in tags if '//' not in x.split(root_url)[1]]
    return tags
    
def cvm_crawl(url):
    """
    Com a url inicial o crawler mapeia todos os pontos finais dos diretórios
    """
    initial_list = directory_crawl(url)
    to_return = []
    while len(initial_list) > 0:
        url_re = initial_list.pop(0)
        if url_re[-4:] in ['.csv', '.txt', '.ods', '.zip']:
            to_return.append(url_re)
        else:
            tags = directory_crawl(url_re)
            if tags == False:
                to_return.append(url_re)
            else:
                initial_list += tags
    return to_return
    

url = 'http://dados.cvm.gov.br/dados/'
result = cvm_crawl(url)

for res in tqdm(result, total = len(result)):
    download_file(res)



