# -*- coding: utf-8 -*-


import requests as re
from lxml import html
from requests_html import HTMLSession
from .utils import *
from tqdm import tqdm
import numpy as np
import pandas as pd
import io
import requests
import zipfile
import datetime


def inner_cvm_info_cadastral(tipo):
    """
    Parameters
    ----------
    tipo : string

    Returns
    -------
    Retorna a série requerida

    """
    if tipo == 'fi':
        r = directory_crawl('http://dados.cvm.gov.br/dados/FI/CAD/DADOS/')
        r_aux = np.array([int(x.split('.csv')[0].split('fi_')[1]) for x in r]).max()
        url_download = [x for x in r if str(r_aux) in x]
        return pd.read_csv(url_download[0],sep=';',engine='python')
    elif tipo in ["fie","fie_adiministrador","fie_auditor","fie_gestor"]:
        r = requests.get('http://dados.cvm.gov.br/dados/FIE/CAD/DADOS/cad_fie.zip')
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if tipo == 'fie':
            with z as z:
                with z.open('cad_fie.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'fie_adiministrador':
            with z as z:
                with z.open('cad_fie_admin.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'fie_auditor':
            with z as z:
                with z.open('cad_fie_auditor.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'fie_gestor':
            with z as z:
                with z.open('cad_fie_gestor.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
    elif tipo in ["auditor_pj","auditor_pf"]:
        r = requests.get('http://dados.cvm.gov.br/dados/AUDITOR/CAD/DADOS/cad_auditor.zip')
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if tipo == 'auditor_pj':
            with z as z:
                with z.open('cad_auditor_pj.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'auditor_pf':
            with z as z:
                with z.open('cad_auditor_pf.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
    elif tipo in ["participante_intermediario_empresa","participante_intermediario_responsavel"]:
        r = requests.get('http://dados.cvm.gov.br/dados/INTERMED/CAD/DADOS/cad_intermed.zip')
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if tipo == 'participante_intermediario_empresa':
            with z as z:
                with z.open('cad_intermed.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'participante_intermediario_responsavel':
            with z as z:
                with z.open('cad_intermed_resp.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
    elif tipo in ["agente_autonomo_pj","agente_autonomo_pf"]:
        r = requests.get('http://dados.cvm.gov.br/dados/INTERMED/CAD/DADOS/cad_intermed.zip')
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if tipo == 'agente_autonomo_pj':
            with z as z:
                with z.open('cad_agente_auton_pj.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'agente_autonomo_pf':
            with z as z:
                with z.open('cad_agente_auton_pf.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
    elif tipo in ["cias_incentivadas"]:
        return pd.read_csv('http://dados.cvm.gov.br/dados/CIA_INCENT/CAD/DADOS/cad_cia_incent.csv', sep = ';', engine = 'python')
    elif tipo in ["cias_estrangeiras"]:
        return pd.read_csv('http://dados.cvm.gov.br/dados/CIA_ESTRANG/CAD/DADOS/cad_cia_estrang.csv', sep = ';', engine = 'python')
    elif tipo in ["cias_abertas"]:
        return pd.read_csv('http://dados.cvm.gov.br/dados/CIA_INCENT/CAD/DADOS/cad_cia_aberta.csv', sep = ';', engine = 'python')
    elif tipo in ["representante_inv_n_residente_pj", "representante_inv_n_residente_pf"]:
        r = requests.get('http://dados.cvm.gov.br/dados/INVNR/CAD/DADOS/cad_invnr_repres.zip')
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if tipo == 'representante_inv_n_residente_pj':
            with z as z:
                with z.open('cad_invnr_repres_pj.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'representante_inv_n_residente_pf':
            with z as z:
                with z.open('cad_invnr_repres_pf.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
    elif tipo in ["consultor_pj", "consultor_pf", "consultor_diretor", "consultor_socios"]:
        r = requests.get('http://dados.cvm.gov.br/dados/CONSULTOR_VLMOB/CAD/DADOS/cad_consultor_vlmob.zip')
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if tipo == 'consultor_pj':
            with z as z:
                with z.open('cad_consultor_vlmob_pj.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'consultor_pf':
            with z as z:
                with z.open('cad_consultor_vlmob_pf.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'consultor_diretor':
            with z as z:
                with z.open('cad_consultor_vlmob_diretor.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'consultor_socios':
            with z as z:
                with z.open('cad_consultor_vlmob_socios.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
    elif tipo in ["administrador_fii"]:
        return pd.read_csv('http://dados.cvm.gov.br/dados/ADM_FII/CAD/DADOS/cad_adm_fii.csv', sep = ';', engine = 'python')
    elif tipo in ["administrador_carteira_pj", "administrador_carteira_pf", "administrador_carteira_diretor", "administrador_carteira_socios", "administrador_carteira_responsaveis"]:
        r = requests.get('http://dados.cvm.gov.br/dados/ADM_CART/CAD/DADOS/cad_adm_cart.zip')
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if tipo == 'administrador_carteira_pj':
            with z as z:
                with z.open('cad_adm_cart_pj.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'administrador_carteira_pf':
            with z as z:
                with z.open('cad_adm_cart_pf.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'administrador_carteira_diretor':
            with z as z:
                with z.open('cad_adm_cart_diretor.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'administrador_carteira_socios':
            with z as z:
                with z.open('cad_adm_cart_socios.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
        elif tipo == 'administrador_carteira_responsaveis':
            with z as z:
                with z.open('cad_adm_cart_resp.csv') as f:
                    return pd.read_csv(f, sep = ';', engine = 'python')
    else:
        return print('A opção {0} é inválida'.format(tipo))

def inner_dados_cvm_fi_estruturado():
    r = directory_crawl('http://dados.cvm.gov.br/dados/FIE/MEDIDAS/DADOS/')
    r_aux = np.array([int(x.split('.csv')[0].split('fie_')[1]) for x in r]).max()
    url_download = [x for x in r if str(r_aux) in x]
    return pd.read_csv(url_download[0],sep=';',engine='python')

def inner_dados_cvm_fi_icvm555():
    r = directory_crawl('http://dados.cvm.gov.br/dados/FI/DOC/LAMINA/DADOS/')
    r_aux = np.array([int(x.split('.zip')[0].split('fi_')[1]) for x in r]).max()
    url_download = [x for x in r if str(r_aux) in x]
    r = requests.get(url_download[0])
    z = zipfile.ZipFile(io.BytesIO(r.content))
    to_return = []
    to_iterate = ["lamina_fi_{0}.csv".format(r_aux),\
                  "lamina_fi_carteira_{0}.csv".format(r_aux),\
                  "lamina_fi_rentab_ano_{0}.csv".format(r_aux),\
                  "lamina_fi_rentab_mes_{0}.csv".format(r_aux)]
    with z as z:
        for file in to_iterate:
            with z.open(file) as f:
                to_return.append(pd.read_csv(f, sep = ';', engine = 'python', error_bad_lines = False))

    return to_return[0], to_return[1], to_return[2], to_return[3]

def inner_dados_cvm_dfp(documento, ano, tipo):
    try:
        if documento.upper() in ['BPA','BPP','DFC_MD','DFC_MI','DMPL','DRE','DVA']:
            if 2010 <= ano <= datetime.datetime.now().year:
                url_download = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/{0}/DADOS/{0}_cia_aberta_{1}.zip'.format(documento, ano)
            else:
                raise ValueError('Ano inválido')
        else:
            raise ValueError('Documento inválido')
    except:
        raise ValueError('Parâmetros inválidos')
    if tipo == 'consolidada':
        r = requests.get(url_download)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        with z as z:
            with z.open("{0}_cia_aberta_con_{1}.csv".format(documento.lower(), ano)) as f:
                return pd.read_csv(f, sep = ';', engine = 'python')
    elif tipo == 'individual':
        r = requests.get(url_download)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        with z as z:
            with z.open("{0}_cia_aberta_ind_{1}.csv".format(documento.lower(), ano)) as f:
                return pd.read_csv(f, sep = ';', engine = 'python')
    else:
        raise ValueError("Tipo Inválido")
