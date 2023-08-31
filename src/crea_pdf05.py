from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pandas as pd
#import pypdf
#from fpdf import FPDF
from reportlab .lib.units import inch
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import pandas as pd

# $ pip install -U kaleido

#  https://plotly.com/python/radar-chart/


import os
import sys
os.chdir("/home/eduardo/GCBA/Encuesta/")


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


# pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
# pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
# pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
# pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

#canvas.setFont('Courier', 12)
#canvas.drawString(50,703,'ETIQUETA:')
#canvas.line(30,700,580,700)
#canvas.drawString(120,703,"<ASUNTO DE LA CARTA GENERICO>")

#canvas.setFont('VeraBd', 12)
#canvas.drawString(30, 750, "Some text encoded in UTF-8")
#canvas.drawString(30, 760, "In the Vera TT Font!")

scores = pd.read_csv('Score_Final.csv',sep=';', encoding='utf-8')

for i in range(len(scores)):
     Area                              = str(scores.iloc[i]['Area'])
     Organismo                         = str(scores.iloc[i]['Organismo'])
     
     print("proceso",Area)
     
     
     nom_file = Area+"-"+Organismo+".pdf"
     canvas2 = canvas.Canvas(nom_file, pagesize=letter)
     #canvas.setLineWidth(.3)
     canvas2.setFont('Helvetica', 12)
     
     #img_file = 'ba.jpeg'
     img_file = 'ba01.png'
     #img_file = 'escudo22.png'
    
     x_start = 30
     y_start = 650
     #canvas.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
     canvas2.drawImage(img_file, x_start, 680, width=120, preserveAspectRatio=True, mask='auto')



     Fuente_de_informacion_Integracion  = str(scores.iloc[i]['Fuente de información/Integración'])
     Ciencia_de_datos                   = str(scores.iloc[i]['Ciencia de datos'])
     Actualidad_de_Reportes_productos   = str(scores.iloc[i]['Actualidad de Reportes/productos'])    
     Disponibilizacion                  = str(scores.iloc[i]['Disponibilización'])
     Proteccion_de_datos                = str(scores.iloc[i]['Protección de datos'])
     Gobernanza_de_datos                = str(scores.iloc[i]['Gobernanza de datos'])
     Gestion_de_acceso_a_datos          = str(scores.iloc[i]['Gestión de acceso a datos'])
     Calidad_de_los_datos               = str(scores.iloc[i]['Calidad de los datos'])
     Reutilizacion_de_datos             = str(scores.iloc[i]['Reutilización de datos'])
     Modelo_de_datos                    = str(scores.iloc[i]['Modelo de datos'])
     




     Fuente_de_informacion_Integracion_int = float(Fuente_de_informacion_Integracion) 
     Ciencia_de_datos_int                  = float(Ciencia_de_datos)                                 
     Actualidad_de_Reportes_productos_int  = float(Actualidad_de_Reportes_productos) 
     Disponibilizacion_int                 = float(Disponibilizacion)                                   
     Proteccion_de_datos_int               = float(Proteccion_de_datos)                           
     Gobernanza_de_datos_int               = float(Gobernanza_de_datos)                        
     Gestion_de_acceso_a_datos_int         = float(Gestion_de_acceso_a_datos)             
     Calidad_de_los_datos_int              = float(Calidad_de_los_datos)                         
     Reutilizacion_de_datos_int            = float(Reutilizacion_de_datos)                        
     Modelo_de_datos_int                   = float(Modelo_de_datos)

     Suma = Fuente_de_informacion_Integracion_int + Ciencia_de_datos_int + Actualidad_de_Reportes_productos_int+Disponibilizacion_int +Proteccion_de_datos_int +Gobernanza_de_datos_int +Gestion_de_acceso_a_datos_int+Calidad_de_los_datos_int+Reutilizacion_de_datos_int +Modelo_de_datos_int                   
     Promedio = Suma / 10

     
     canvas2.setFont('Courier-Bold',18)
     canvas2.setFillColorRGB(1,0,0) 
     canvas2.drawString(260,740,Area)
     canvas2.drawString(260,720,Organismo)

     canvas2.setFillColorRGB(.8, .8, .8)
     
     
     canvas2.line(30,690,580,690)
     pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
     pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
     pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
     pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
     #canvas2.setFont('Courier-Italic',13) 
     canvas2.setFont('VeraIt', 12)
     canvas2.setFillColorRGB(0,0.1,0.5)
     
     canvas2.drawString(120,675,'Calificación por dimensiones (rango entre 0 y 5)')


     canvas2.setFont('Times-BoldItalic',13) 
     canvas2.setFillColorRGB(0,0.1,0.5)
     
     canvas2.drawString(30,650,'Fuente de información Integración:')
     canvas2.drawString(300,650,Fuente_de_informacion_Integracion)
     
     canvas2.drawString(30,630,'Ciencia de datos:')
     canvas2.drawString(300,630,Ciencia_de_datos)
     
     canvas2.drawString(30,610,'Actualidad de Reportes productos:')
     canvas2.drawString(300,610,Actualidad_de_Reportes_productos)
     
     canvas2.drawString(30,590,'Disponibilización:')
     canvas2.drawString(300,590,Disponibilizacion)
     
     canvas2.drawString(30,570,'Protección de datos:')
     canvas2.drawString(300,570,Proteccion_de_datos)
     
     canvas2.drawString(30,550,'Gobernanza de datos:')
     canvas2.drawString(300,550,Gobernanza_de_datos)
     
     canvas2.drawString(30,530,'Gestión de acceso a datos:')
     canvas2.drawString(300,530,Gestion_de_acceso_a_datos)
     
     canvas2.drawString(30,510,'Calidad de los datos:')
     canvas2.drawString(300,510,Calidad_de_los_datos)
     
     canvas2.drawString(30,490,'Reutilización de datos:')
     canvas2.drawString(300,490,Reutilizacion_de_datos)
     
     canvas2.drawString(30,470,'Modelo de datos:')
     canvas2.drawString(300,470,Modelo_de_datos)
  
     canvas2.line(30,460,330,460)
     
     canvas2.drawString(30,440,'Calificación Final:')
     canvas2.drawString(300,440,str(round(Promedio,2)))
     
     #canvas2.rect(50, 330, 310, 180)
     
     
     canvas2.setFillColorRGB(0.2,0.2,0.2)
     if Promedio >= 0 and Promedio< 1:
         canvas2.drawString(30,410,'Inicial') 
         canvas2.drawString(30,390,'Los Datos son usados como un requerimiento para hacer proyectos')        
         
     if Promedio >= 1 and Promedio< 2:
         canvas2.drawString(30,410,'Media') 
         canvas2.drawString(30,390,'Hay una concientización acerca de la importancia como un activo clave')        
         
     if Promedio >= 2 and Promedio< 3:
         canvas2.drawString(30,410,'Avanzada') 
         canvas2.drawString(30,390,'Los datos son considerados a nivel organizacional como muy relevantes ')
         canvas2.drawString(30,380,'para la organización para un resultado exitoso')        
         
     if Promedio >= 3 and Promedio< 4:
         canvas2.drawString(30,410,'Experta') 
         canvas2.drawString(30,390,'La posesión de información de calidad es una ventaja para la toma de decisiones')        
         
     if Promedio >= 4 and Promedio< 6:
         canvas2.drawString(30,410,'Mejora continua') 
         canvas2.drawString(30,390,'Se incluyen mecanismos de gestión del conocimiento, formas de aprender de los ')
         canvas2.drawString(30,380,'que se hace, mecanismos de auditoria y de revisión de procesos, de compartir los mejores procesos')        


     # df2 = df.drop(['Area'], axis=1)
     # df3 = df2.drop(['Organismo'], axis=1)
    
     # categories = [*df3.columns[1:], df3.columns[1]]


     df = scores.loc[scores['Area'] == Area]

     df2 = df.drop(['Area'], axis=1)
     df3 = df2.drop(['Organismo'], axis=1)
    
     categories = [*df3.columns[0:], df3.columns[0]]
     #categories2 = categories.pop(0)
     #categories.remove("Organismo")
     #categories.remove("Organismo")
    
     data = [go.Scatterpolar(
                r=[*row.values, row.values[0]],
                theta=categories,
                name=label) for label, row in df3.iterrows()]

     fig = go.Figure(
         data=data,
         layout=go.Layout(
             title=go.layout.Title(text="Análisis de Dimensiones:"+Area, xanchor='center', x=0.2),
             polar={'radialaxis': {'visible': True}},
             showlegend=True
         )
     )




    
     # fig = go.Figure(data=go.Scatterpolar(
     #   r=[Fuente_de_informacion_Integracion_int, Ciencia_de_datos, Actualidad_de_Reportes_productos, Disponibilizacion, Proteccion_de_datos,Gobernanza_de_datos,Gestion_de_acceso_a_datos,Calidad_de_los_datos,Reutilizacion_de_datos,Modelo_de_datos],
     #   theta=['Fuente de información/Integración','Ciencia de datos','Actualidad de Reportes/productos',
     #            'Disponibilización', 'Protección de datos','Gobernanza de datos','Gestión de acceso a datos','Calidad de los datos','Reutilización de datos','Modelo de datos'],
     #   fill='toself',
     #   ),
     #   layout=go.Layout(
     #   title=go.layout.Title(text="Análisis de Dimensiones--", xanchor='center', x=0.5),
     #   polar={'radialaxis': {'visible': True}},
     #   showlegend=False))
       
    
     fig.update_layout(
      polar=dict(
          radialaxis=dict(
          visible=True
          ),
        ),
        showlegend=False
      )






     # df = pd.DataFrame(dict(
     #     r=[Fuente_de_informacion_Integracion_int, Ciencia_de_datos, Actualidad_de_Reportes_productos, Disponibilizacion, Proteccion_de_datos,Gobernanza_de_datos,Gestion_de_acceso_a_datos,Calidad_de_los_datos,Reutilizacion_de_datos,Modelo_de_datos],
     #     theta=['Fuente de información/Integración','Ciencia de datos','Actualidad de Reportes/productos',
     #            'Disponibilización', 'Protección de datos','Gobernanza de datos','Gestión de acceso a datos','Calidad de los datos','Reutilización de datos','Modelo de datos']))
     # fig = px.line_polar(df, r='r', theta='theta', line_close=True)
     # #fig.show()
     #pyo.plot(fig)
     
     fig.write_image("radar01.png")
     img_file = 'radar01.png'
     #img_file = 'escudo22.png'
   
     x_start = 340
     y_start = 300
     #canvas.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
     canvas2.drawImage(img_file, x_start, 330, width=250, preserveAspectRatio=True, mask='auto')

     #Dibujamos un Cuadrado a partir de un rectángulo redondeado
     #-roundRect(x, y, ancho, alto, radio de curva, stroke, fill)
     #stroke y fill, si es 0 inidica no mostrar trazo ni relleno
     canvas2.roundRect(20, 430, 315, 240, 20, stroke = 1, fill = 0)
     canvas2.setFillColorRGB(0.75, 0.75, 0.0)  # Relleno para el texto "Cuadrado"
     canvas2.drawString(125, 80, "Cuadrado")
             

     canvas2.save()
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


