# -*- coding: utf-8 -*-

import pandas
from requests_html import HTMLSession
import numpy as np
from .error import *
import pandas as pd
import ast

def inner_dados_bacen(serie_value):
    """
    Recebe o número da série do BCB e faz o download
    """
    try:
        query = "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{0}/dados?formato=json".format(serie_value)
        session = HTMLSession()
        r = session.get(query)
        return pd.DataFrame(ast.literal_eval(r.text))
    except:
        raise ValueError("Série Inválida")
