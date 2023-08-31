#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:30:01 2023


https://blog.desdelinux.net/instalar-fuentes-tipograficas-linux/


@author: eduardo
"""

# -*- coding:utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

os.chdir("/home/eduardo/GCBA/Encuesta/")



#TTFont(nombre, archivo)
pdfmetrics.registerFont(TTFont('Comicate', 'Comicate.ttf'))

c=canvas.Canvas("test.pdf", pagesize = A4)
c.drawString(100, 700, "Texto sin usar fuente ttf")

c.setFont('Comicate', 20)
c.drawString(100, 600, "Texto usando fuente ttf")

c.showPage()

c.save()
os.system("test.pdf")
