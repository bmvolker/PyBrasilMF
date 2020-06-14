# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:47:12 2020

@author: bmvol
"""

class InvalidSerie(Exception):
    """
    Erro retornado quando a série requisitada não existe
    """
    def __init__(self):
        print("A série é inválida")
    