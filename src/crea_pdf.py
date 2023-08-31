from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pandas as pd
#import pypdf
#from fpdf import FPDF
from reportlab .lib.units import inch



import os
import sys
os.chdir("/home/eduardo/GCBA/Encuesta/")

canvas = canvas.Canvas("form.pdf", pagesize=letter)
#canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)

#img_file = 'ba.jpeg'
img_file = 'escudo22.png'

x_start = 30
y_start = 650
#canvas.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
canvas.drawImage(img_file, x_start, 680, width=120, preserveAspectRatio=True, mask='auto')


#canvas.showPage()
#canvas.save()
#sys.exit()
#canvas.drawImage('logo.png',-0.8*inch,.3*inch)
#canvas.drawImage('https://www.plus2net.com/images/top2.jpg',-0.8*inch,9.3*inch)

#canvas.drawString(30,740,'Organismo:')
#canvas.drawString(100,740,'El orga')
#canvas.drawString(500,750,"27/10/2016")
#canvas.line(480,747,580,747)


#canvas.drawString(30,720,'Area:')
#canvas.drawString(100,720,"El Area")
#canvas.line(378,723,580,723)


pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

canvas.setFont('Courier', 12)
#canvas.drawString(50,703,'ETIQUETA:')
#canvas.line(30,700,580,700)
#canvas.drawString(120,703,"<ASUNTO DE LA CARTA GENERICO>")

canvas.setFont('VeraBd', 12)
#canvas.drawString(30, 750, "Some text encoded in UTF-8")
#canvas.drawString(30, 760, "In the Vera TT Font!")

scores = pd.read_csv('Score_Final.csv',sep=';', encoding='utf-8')

for i in range(len(scores)-1):
     Area                              = str(scores.iloc[i]['Area'])
     Organismo                         = str(scores.iloc[i]['Organismo'])
     Fuente_de_información_Integración = str(scores.iloc[i]['Fuente de información/Integración'])
     Ciencia_de_datos                  = str(scores.iloc[i]['Ciencia de datos'])
     Actualidad_de_Reportes_productos  = str(scores.iloc[i]['Actualidad de Reportes/productos'])    
     Disponibilizacion                 = str(scores.iloc[i]['Disponibilización'])
     Proteccion_de_datos               = str(scores.iloc[i]['Protección de datos'])
     Gobernanza_de_datos               = str(scores.iloc[i]['Gobernanza de datos'])
     Gestion_de_acceso_a_datos         = str(scores.iloc[i]['Gestión de acceso a datos'])
     Calidad_de_los_datos              = str(scores.iloc[i]['Calidad de los datos'])
     Reutilizacion_de_datos            = str(scores.iloc[i]['Reutilización de datos'])
     Modelo_de_datos                   = str(scores.iloc[i]['Modelo de datos'])
     
     canvas.setFont('Courier-Bold',18)
     canvas.setFillColorRGB(1,0,0) 
     canvas.drawString(160,740,Area)
     canvas.drawString(160,720,Organismo)


     canvas.setFillColorRGB(.8, .8, .8)
     canvas.line(30,690,580,690)

     canvas.setFont('Times-BoldItalic',13) 
     canvas.setFillColorRGB(0,0.1,0.5)
     
     canvas.drawString(30,660,'Fuente de información Integración:')
     canvas.drawString(300,660,Fuente_de_información_Integración)
     
     canvas.drawString(30,640,'Ciencia de datos:')
     canvas.drawString(300,640,Ciencia_de_datos)
     
     canvas.drawString(30,620,'Actualidad de Reportes productos:')
     canvas.drawString(300,620,Actualidad_de_Reportes_productos)
     
     canvas.drawString(30,600,'Disponibilizacion:')
     canvas.drawString(300,600,Disponibilizacion)
     
     canvas.drawString(30,580,'Proteccion de datos:')
     canvas.drawString(300,580,Proteccion_de_datos)
     
     canvas.drawString(30,560,'Gobernanza de datos:')
     canvas.drawString(300,560,Gobernanza_de_datos)
     
     canvas.drawString(30,540,'Gestion de acceso a datos:')
     canvas.drawString(300,540,Gestion_de_acceso_a_datos)
     
     canvas.drawString(30,520,'Calidad de los datos:')
     canvas.drawString(300,520,Calidad_de_los_datos)
     
     canvas.drawString(30,500,'Reutilizacion de datos:')
     canvas.drawString(300,500,Reutilizacion_de_datos)
     
     canvas.drawString(30,480,'Modelo de datos:')
     canvas.drawString(300,480,Modelo_de_datos)

     #key, value = pregunta+"-"+categoria, codigo
     #codigos2.update({key: value})


# canvas.grid(xlist, ylist)
# canvas.bezier(x1, y1, x2, y2, x3, y3, x4, y4)
# canvas.arc(x1,y1,x2,y2)
# canvas.rect(x, y, width, height, stroke=1, fill=0)
# canvas.ellipse(x1,y1, x2,y2, stroke=1, fill=0)
# canvas.wedge(x1,y1, x2,y2, startAng, extent, stroke=1, fill=0)
# canvas.circle(x_cen, y_cen, r, stroke=1, fill=0)
# canvas.roundRect(x, y, width, height, radius, stroke=1, fill=0) 

canvas.save()


# from reportlab.pdfgen import canvas
 
# img_file = '../../static/img/code_maven_440x440.png'
# pdf_file = 'hello_world.pdf'
 
# can = canvas.Canvas(pdf_file)
# can.drawString(20, 400, "Hello World!")
 
# x_start = 0
# y_start = 0
# can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
 
# can.showPage()
# can.save()


