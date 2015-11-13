#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:54:02 2015

@author: pedroalpacheco
"""
from datetime import datetime
import shutil
import os

#Pega data e hora
agora = datetime.now()
hoje = str(agora)

#Abre o arquivo adicionando na última linha
arquivo = open('HISTORICO_SITE_DELETADOS.txt', "a+")

caminhoorig = "/home/papacheco/dirorig/"
destino = "/home/papacheco/dirbackup/"

site = raw_input("Digite o diretorio:")

caminhotot = caminhoorig + site

#print caminhotot

#Verifica se caminho existe
if os.path.exists(caminhotot):
    shutil.move(caminhotot, destino)
    print " -Site %s MOVIDO " % site
    #Gera dados de log de acoes
    resulthist = " -Site %s MOVIDO " % site
    arquivo.writelines('\n'+hoje+resulthist)
    arquivo.close()
else:
    print " -Site %s NAO ENCONTRADO! " % site
    resulthist = " -Site %s NAO ENCONTRADO! " % site
    #Gera dados de log de acoes
    arquivo.writelines('\n'+hoje+resulthist)
    arquivo.close()
    
    
    
    
    
