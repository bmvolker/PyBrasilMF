# -*- coding: utf-8 -*-

from .cvm import *
from .bacen import *

class cvm():
    def __init__(self):
        pass
    def cvm_info_cadastral(self, tipo):
        return inner_cvm_info_cadastral(tipo)
    def dados_cvm_fi_estruturado(self):
        return inner_dados_cvm_fi_estruturado()
    def dados_cvm_fi_icvm555(self):
        return inner_dados_cvm_fi_icvm555()
    def dados_cvm_dfp(self, documento, ano, tipo):
        return inner_dados_cvm_dfp(documento, ano, tipo)

class bacen():
    def __init__(self):
        pass
    def dados_bacen(self, serie_value):
        return inner_dados_bacen(serie_value)

if __name__ == '__main__':
    pass
