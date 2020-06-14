# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:23:16 2020

@author: bmvol
"""

import pandas
from requests_html import HTMLSession
import numpy as np
from error import *
import pandas as pd
import ast

def bacen(serie_value):
    """
    Recebe o número da série do BCB e faz o download
    """
    try:
        query = "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{0}/dados?formato=json".format(serie_value)
        session = HTMLSession()
        r = session.get(query)
        return pd.DataFrame(ast.literal_eval(r.text))
    except:
        raise InvalidSerie
        return


