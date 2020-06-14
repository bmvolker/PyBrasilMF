# -*- coding: utf-8 -*-


class InvalidSerie(Exception):
    """
    Erro retornado quando a série requisitada não existe
    """
    def __init__(self):
        print("A série é inválida")
    