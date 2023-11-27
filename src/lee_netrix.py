#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:23:46 2023

@author: eduardo
"""

import csv
import os
import sys
import pandas as pd
from os import system
import time


from dotenv import load_dotenv
import os

# from dotenv import dotenv_values
# load_dotenv()
# ultimo_proceso = os.getenv('FECHA')

os.chdir("/home/eduardo/GCBA/Encuesta/Matriz_Madurez/data/")

df2 = pd.read_csv("formulario_205769.csv",index_col=False, encoding='utf-8')
df2["property"] = 0

for i in range(len(df2)):
     campo = df2.iloc[i]['name']
     guion = campo.find("_")
     if guion < 3 and guion>0:
        orden  = campo[:guion]
        print("orden",orden+"--"+campo)
        columna_nombre = "property"
        df2.iloc[i, df2.columns.get_loc(columna_nombre)] = int(orden)
     if campo == "apellido_y_nombre":
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = -10
     if campo == "_perteneces_a_un_area_del_gobierno_de_la_ciudad_de_buenos_aires_":
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = -9    
     if campo == "correo_electronico":
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = -8
     if campo == "cargo_puesto_que_ocupa":
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = -7
     if campo == "_de_que_secretaria_o_subsecretaria_depende_":
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = -6
     if campo == "pais":
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = -12
         columna_nombre = "name"
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = "Fecha"
     if campo == "nombre_de_la_ciudad":
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = -11
         columna_nombre = "name"
         df2.iloc[i, df2.columns.get_loc(columna_nombre)] = "Score"





df_ordenado = df2.sort_values(by='property')
df_filter = df_ordenado[df_ordenado["property"] != 0]
df_filter.set_index('property', inplace=True)  # Establecer 'Nombre' como índice
df_filter = df_filter.fillna('None')  ## cambio los NaN por 0's

df_filter = df_filter.reset_index(drop=True)

df = df_filter.drop(['delta'], axis=1)
df = df.drop(['webform_id'], axis=1)
df = df.drop(['sid'], axis=1)
df = df.drop(['fecha_ingesta'], axis=1)

df.to_csv('pivoteada.csv', index=False, encoding='utf-8',sep=';')


df2 = pd.read_csv("pivoteada.csv",index_col=False, encoding='utf-8',sep=';')
df2 = df2.fillna('None')  ## cambio los NaN por 0's

#sys.exit()


df_nuevo = df2.pivot(columns='name', values='value')

df_nuevo.to_csv('pivoteada2.csv', index=False, encoding='utf-8',sep=';')
     


