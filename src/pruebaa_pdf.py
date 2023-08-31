#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:04:36 2023

@author: eduardo
"""
import os
os.chdir("/home/eduardo/GCBA/Encuesta/")

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter,A4

my_path='my_pdf.pdf'
# file path
c = canvas.Canvas(my_path,bottomup=1,pagesize=letter)
c.translate(inch,inch) #starting point of coordinate to one inch
c.setStrokeColorRGB(1,0,0) # red colour of linec.setLineWidth(10) #width of the line 
c.line(0,8*inch,7*inch,8*inch) # draw line
c.showPage() # saves current page
c.save() # stores the file and close  the canvas