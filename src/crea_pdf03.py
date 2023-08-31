#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:16:21 2023

@author: eduardo
"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import os

os.chdir("/home/eduardo/GCBA/Encuesta/")


canvas = canvas.Canvas("Pruebas_13_06.pdf", pagesize=letter)
canvas.setLineWidth(.3)

canvas.setFont('Times-Roman', 12)
canvas.setFillColorRGB(0,0.1,0.5)

## setFillColorRGB(Red,Green,Blue)

canvas.setStrokeColorRGB(0,1,0.3)
canvas.setFillColorRGB(0,1,0)
 
la_730 = "Fila numero 730"
la_720 = "Fila numero 720"

y = 760
for i in range(1,100):
        y = y-20
        cadena = str(y)+"---"+ str(i)

        
        if i%35 == 0:
            canvas.showPage()
            canvas.setFont('Times-Roman', 12)
            canvas.setFillColorRGB(0,0.1,0.5)
            y = 760
            canvas.drawString(30,y,cadena)
        else:
            canvas.setFillColorRGB(1,1,0)  ### AMARILLO
            canvas.setFillColorRGB(0,1,0)  ## VERDE
            canvas.setFillColorRGB(1,0,0)  ## ROJO         
            canvas.setFillColorRGB(0,0.1,0.5)  ## AZUL
            canvas.setFillColorRGB(0.2,0.2,0.2) ## NEGRO
            canvas.setFillColorRGB(.8, .8, .8)  ## GRIS
            canvas.setFillColorRGB(.4, .8, .8)  ## CYAN
            canvas.setFillColorRGB(.8, .8, .8)  ## GRIS
            canvas.setFillColorRGB(.6, .6, .6)  ## OTRO GRIS
            canvas.drawString(30,y,cadena)

        # if i%10 == 0:
        #     canvas.setFillColorRGB(.6, .6, .6)
        #     canvas.setFont('Courier', 12)
        #     canvas.line(378,723,580,723)

            
canvas.save()
