#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:09:56 2023

@author: eduardo
"""

from reportlab.pdfgen import canvas
from reportlab .lib.units import inch

pdffile= canvas.Canvas("Pruebas del pdf")
fonts = pdffile.getAvailableFonts()

print(fonts)

y = 760
pdffile.translate(inch, inch )

for font in fonts:
        pdffile.setFont(font,15)
        pdffile.setFillColorRGB(0,0.1,0.5)
        pdffile.drawString(30,y,font)
        y = y-20
        print(y)
        print(font)
        
pdffile.save()




#  Courier-Bold