#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:55:11 2023

@author: eduardo
"""

# -*- coding:utf-8 -*
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch  # Tambien podemos usar otras medidas

import os
import sys
os.chdir("/home/eduardo/GCBA/Encuesta/")



c=canvas.Canvas("test.pdf", pagesize = A4)

#Ancho y alto de la página
ancho, alto = A4

#Definimos el tipo y tamaño de fuente
c.setFont("Helvetica", 24)

#Dibujamos un par de lineas, por omision serán de color negro
#-line(x1,y1,x2,y2) x1,y1 inicio de line; x2, y2 fin de linea
c.line(50,50,50,350)
c.line(50,50,350,50)

#Escogemos algunos colores
c.setStrokeColorRGB(0.0, 1, 0.0)  # Color de trazo
c.setFillColorRGB(0, 0.0, 0.5)  # Color de relleno

#Dibujamos un Cuadrado a partir de un rectángulo redondeado
#-roundRect(x, y, ancho, alto, radio de curva, stroke, fill)
#stroke y fill, si es 0 inidica no mostrar trazo ni relleno
c.roundRect(75, 75, 275, 257, 20, stroke = 1, fill = 1)
c.setFillColorRGB(0.75, 0.75, 0.0)  # Relleno para el texto "Cuadrado"
c.drawString(125, 80, "Cuadrado")

#Dibujamos un Círculo
c.setFillColorRGB(0.8, 0.0, 0.2)
c.circle(205, 205, 100, stroke=1, fill=1)  # x, y, radio, stroke, fill
c.setFillColorRGB(0, 1, 0.2)
c.drawString(155, 200, "Circulo")

#Dibujamos una Elipse
c.setStrokeColorRGB(1, 0, 0.0)
c.ellipse(75, 450, 350, 335)  #x1, y1, x2, y2, stroke, fill
c.setFillColorRGB(0, 0, 0.5)
c.drawString(150, 375, "Elipse")

c.showPage()  # Finalizamos la página

#Si lo han notado hemos de ingresar color de relleno y trazo para cada forma,
#sino especificamos, lo hara en negro.
#grid(lista en x, lista en y)
c.grid([20,40,60,80], [alto-20,alto-40,alto-60,alto-80])
#arc(x1,y1,x2,y2)
c.arc(200, 200, 400, 400)
#rect(x, y, alto, ancho, stroke=1, fill=0)
c.rect(300,500, 200, 100)

#Veamos los tipos de dibujo de texto
c.line(ancho/2, 720, ancho/2, 640)
c.drawString(ancho/2, 700, "Texto con punto de referencia a la izquierda")
c.drawRightString(ancho/2, 680, "Texto con punto de referencia a la derecha")
c.drawCentredString(ancho/2, 660, "Texto con punto de referencia en el centro")

c.save()  # Archivamos y cerramos canvas
#os.system("test.pdf")  # Lanzamos el pdf
