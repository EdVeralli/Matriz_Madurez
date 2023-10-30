import pandas as pd

# $ pip install -U kaleido

#  https://plotly.com/python/radar-chart/


import os
import sys
os.chdir("/home/eduardo/GCBA/Encuesta/Matriz_Madurez/data/")

import json
 
# # Opening JSON file
# f = open('submission-6.json')
 
# # returns JSON object as
# # a dictionary
# data = json.load(f)
 
# # Iterating through the json
# # list
# for i in data['serial']:
#     print(i)

# print("*********************")
# #print(data['data'])

# respuestas = data['data']

# # Closing file
# f.close()

# sys.exit()

p = open("Scores_monica.csv", "w")
Score_Final_titulo = "id"+";"+"Fecha"+";"+"NombreApellido"+";"+"mail"+";"+'cargo'+";"+"Organismo"+ \
        ";"+"Fuente de información/Integración"+";"+"nivel d1"+";"+"texto d1"+ \
        ";"+'Ciencia de datos'+";"+"nivel d2"+";"+"texto d2"+ \
        ';'+'Actualidad de Reportes/productos'+";"+"nivel d3"+";"+"texto d3"+ \
        ';'+'Disponibilización'+";"+"nivel d4"+";"+"texto d4"+ \
        ';'+'Protección de datos'+";"+"nivel d5"+";"+"texto d5"+ \
        ";"+'Gobernanza de datos'+";"+"nivel d6"+";"+"texto d6"+ \
        ';'+'Gestión de acceso a datos'+";"+"nivel d7"+";"+"texto d7"+ \
        ';'+'Calidad de los datos'+";"+"nivel d8"+";"+"texto d8"+ \
        ';'+'Reutilización de datos'+";"+"nivel d9"+";"+"texto d9"+ \
        ';'+'Modelo de datos' +";"+"nivel d10"+";"+"texto d10"+  \
        ';'+'Final' +";"+"nivel final"+";"+"texto final"         
        
        
        
p.write(Score_Final_titulo+"\n")



scores = pd.read_csv('Score_Final.csv',index_col=False, encoding='utf-8',sep=';')

#sys.exit()

for i in range(len(scores)):
     Fecha                             = str(scores.iloc[i]['Fecha'])
     NombreApellido                    = str(scores.iloc[i]['NombreApellido'])
     mail                              = str(scores.iloc[i]['mail'])
     cargo                             = str(scores.iloc[i]['cargo'])   
     Organismo                         = str(scores.iloc[i]['Organismo'])     
     

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
     

     cant_dim = scores.iloc[i]['Dim_validas']

   
     
     Suma = Fuente_de_informacion_Integracion_int + Ciencia_de_datos_int + Actualidad_de_Reportes_productos_int+Disponibilizacion_int +Proteccion_de_datos_int +Gobernanza_de_datos_int +Gestion_de_acceso_a_datos_int+Calidad_de_los_datos_int+Reutilizacion_de_datos_int +Modelo_de_datos_int                   
     Promedio = Suma / cant_dim

     if Fuente_de_informacion_Integracion_int == 0:
        nivel_dim1 = "Cero"
        texto_dim1 = "En el camino de la mejora deberan desarrollar la integracion y recoleccion de datos para garantizar la consistencia y actualizacion de la informacion. Es fundamental poseer una base de datos propia con tecnologia de integracion y documentar las politicas de dicha integracion. Esto proporcionara claridad, transparencia y garantizara el cumplimiento normativo. Asimismo, les permitira la planificacion de estrategias, lo que impactara positivamente en el rendimiento de la organizacion."

     if Fuente_de_informacion_Integracion_int > 0 and Fuente_de_informacion_Integracion_int<1:
        nivel_dim1 = "Inicial"
        texto_dim1 = "La organizacion debe especializarse en la recopilacion de datos y en la implementacion de una estrategia de integracion y aprovechamiento de la informacion. Es decir, debe contar con bases de datos propias para gestionar eficientemente los datos, mejorando su accesibilidad y analisis, lo que ademas le permitira avanzar en el desarrollo de la integracion de los datos."

     if Fuente_de_informacion_Integracion_int >= 1 and Fuente_de_informacion_Integracion_int<2:
        nivel_dim1 = "Medio"
        texto_dim1 = "La organizacion cuenta con bases de datos propias, lo que robustece la integracion de datos de diferentes fuentes e impulsa la toma de decisiones informadas y la identificacion de patrones en los datos para obtener ventajas competitivas."
        
     if Fuente_de_informacion_Integracion_int >= 2 and Fuente_de_informacion_Integracion_int<3:
        nivel_dim1 = "Avanzado"
        texto_dim1 = "La organizacion cuenta con una estrategia de integracion de datos que maximiza su valor, mejora la toma de decisiones y la eficiencia operativa. Bases de datos propias, gestion responsable y capacidad de integrar datos de multiples fuentes, brindan ventajas competitivas. Documentar politicas de integracion asegura consistencia, cumplimiento normativo, calidad de datos y comunicacion efectiva."

     if Fuente_de_informacion_Integracion_int >= 3 and Fuente_de_informacion_Integracion_int<4:
        nivel_dim1 = "Experto"
        texto_dim1 = "La organizacion ha demostrado su progreso en el tratamiento de datos demuestra un enfoque destacado en la toma de decisiones. Asimismo, puede seguir progresando mediante la evaluacion constante, la adopcion de tecnologias y la capacitacion continua para cerrar la brecha hacia la maxima madurez en la gestion de datos."

     if Fuente_de_informacion_Integracion_int >= 4 and Fuente_de_informacion_Integracion_int<=6:
        nivel_dim1 = "Mejora continua"
        texto_dim1 = "La organizacion al estar en este nivel refleja el compromiso con el tratamiento adecuado de los datos como un activo de valor. Es fundamental a seguir trabajando en este camino para el logro de niveles aun mas avanzados de madurez en la gestion de datos."



######

     if Ciencia_de_datos_int == 0:
        nivel_dim2 = "Cero"
        texto_dim2 = "Es recomendable contar con areas de desarrollo de ciencia de datos, ya que es beneficiosa en diversos aspectos, fundamentalmente para la toma de decisiones informadas. Es importante identificar las oportunidades de mejora que se pueden alcanzar a partir de la implementacion de capacidades en este tema."
        
     if Ciencia_de_datos_int > 0 and Ciencia_de_datos_int<1:
        nivel_dim2 = "Inicial"
        texto_dim2 = "La organizacion demuestra el reconocimiento de la importancia de la Ciencia de Datos. En este nivel, podran fortalecer su capacidad respecto de la toma de decisiones informadas y aprovechar al maximo el potencial de los datos disponibles mediante el desarrollo y entrenamiento de modelos de aprendizaje automatico, analisis predictivo y su documentacion."
        
     if Ciencia_de_datos_int >= 1 and Ciencia_de_datos_int<2:
        nivel_dim2 = "Medio"
        texto_dim2 = "La organizacion va por un buen camino y la aplicacion de tecnicas estadisticas, modelos de aprendizaje automatico y analisis predictivo. Es fundamental para seguir avanzando, es crucial documentar sistematicamente los proyectos para garantizar la replicabilidad y la transparencia como tambien la transferencia de conocimientos y el cumplimiento normativo."
        
     if Ciencia_de_datos_int >= 2 and Ciencia_de_datos_int<3:
        nivel_dim2 = "Avanzado"
        texto_dim2 = "La organizacion debe continuar invirtiendo en habilidades tecnicas, actualizandose en tendencias y colaborando con expertos externos para maximizar el valor de los datos para la toma de decisiones y asi lograr niveles mas avanzados de madurez."
        
     if Ciencia_de_datos_int >= 3 and Ciencia_de_datos_int<4:
        nivel_dim2 = "Experto"
        texto_dim2 = "La organizacion demostro madurez y practicas avanzadas en el tratamiento de datos. Recomendamos que continuen invirtiendo en capacitacion, colaboracion externa y seguimiento de avances para maximizar el valor de los datos para la toma de decisiones mas eficientes para la organizacion."
        
     if Ciencia_de_datos_int >= 4 and Ciencia_de_datos_int<=6:
        nivel_dim2 = "Mejora continua"
        texto_dim2 = "La organizacion demostro dedicacion y practicas avanzadas en el tratamiento de los datos un grado avanzado de madurez. Instamos a que continuen actualizandose y explorando nuevas aplicaciones para continuar la innovacion basada en datos."
        

######

     if Actualidad_de_Reportes_productos_int == 0:
        nivel_dim3 = "Cero"
        texto_dim3 = "Disponer de reportes actualizados es fundamental para garantizar la transparencia, la rendicion de cuentas, la toma de decisiones informadas, la evaluacion, asi como la comunicacion interna y externa efectiva. Es recomendable el diseño de un sistema que contenga un componente para la generacion y la publicacion de reportes de forma regular, que reflejen sus actividades, resultados e impacto."
        
     if Actualidad_de_Reportes_productos_int > 0 and Actualidad_de_Reportes_productos_int<1:
        nivel_dim3 = "Inicial"
        texto_dim3 = "La organizacion dispone de reportes de datos, aunque es importante automatizarlos y actualizarlos con frecuencia. Recopilar la opinion de los usuarios y ajustar los procesos de actualizacion mejora la toma de decisiones y la comunicacion en la organizacion."
        
     if Actualidad_de_Reportes_productos_int >= 1 and Actualidad_de_Reportes_productos_int<2:
        nivel_dim3 = "Medio"
        texto_dim3 = "La organizacion genera reportes de datos actualizados regularmente. Pero se recomienda su automatizacion. Es esencial trabajar con las devoluciones de los usuarios para ajustar los procesos de actualizacion en funcion de sus experiencias de uso. Los informes precisos y accesibles son fundamentales para la toma de decisiones y la comunicacion efectiva."
        
     if Actualidad_de_Reportes_productos_int >= 2 and Actualidad_de_Reportes_productos_int<3:
        nivel_dim3 = "Avanzado"
        texto_dim3 = "La organizacion genera reportes de datos actualizados y automatizados con frecuencia. Es recomendable realizar ajustes en los procesos de actualizacion segun los comentarios de los usuarios, ya que es fundamental para mejorar los informes y demostrar que sus opiniones son valoradas."
        
     if Actualidad_de_Reportes_productos_int >= 3 and Actualidad_de_Reportes_productos_int<4:
        nivel_dim3 = "Experto"
        texto_dim3 = "La organizacion demuestra un alto grado de madurez en el tratamiento de los datos para generar reportes y productos actualizados habilidades solidas y conocimientos en la generacion de reportes y productos basados en datos mediante procesos eficientes. Para continuar avanzando recomendamos que continuen evaluando y mejorando periodicamente sus procesos, aprovechando las ultimas tendencias y tecnologias en la generacion de reportes y productos basados en datos."
        
     if Actualidad_de_Reportes_productos_int >= 4 and Actualidad_de_Reportes_productos_int<=6:
        nivel_dim3 = "Mejora continua"
        texto_dim3 = "La organizacion demuestra una madurez en el tratamiento de datos, generacion de reportes relevantes y establecimiento de procesos solidos reflejan un enfoque destacado en la toma de decisiones. Los aldentamos a que continuen en este camino optimizando y compartiendo practicas eficientes para impulsar la cultura de mejora continua."
        
######

     if Disponibilizacion_int == 0:
        nivel_dim4 = "Cero"
        texto_dim4 = "La organizacion deberian contar con datos disponibles para tomar decisiones informadas y realizar analisis. La disponibilidad de datos tambien debe estar en linea con las politicas de privacidad y seguridad de la informacion."
        
     if Disponibilizacion_int > 0 and Disponibilizacion_int<1:
        nivel_dim4 = "Inicial"
        texto_dim4 = "La organizacion debe asegurarse de tener los datos disponibles con regularidad y en formatos estandar abiertos como CSV, JSON, XML, KML, GEOJSON, a los fines de tomar decisiones informadas y realizar analisis. Ademas, es importante desarrollar APIs para permitir el acceso externo y utilizar un lenguaje adecuado segun la audiencia (demografica, tributaria, etc.). Asimismo, es importante que los datos esten protegidos mediante politicas de seguridad de la informacion."
        
     if Disponibilizacion_int >= 1 and Disponibilizacion_int<2:
        nivel_dim4 = "Medio"
        texto_dim4 = "La organizacion debe procurar  disponibilizar los datos  en formatos estandar abiertos como CSV, JSON, XML, KML, GEOJSON desarrollar APIs para permitir el acceso externo y utilizar un lenguaje adecuado segun la audiencia (demografica, tributaria, etc.). La disponibilidad de los datos es fundamental para la toma de decisiones informadas y realizar analisis, aunque tambien deben estar protegidos mediante politicas de seguridad de la informacion."
        
     if Disponibilizacion_int >= 2 and Disponibilizacion_int<3:
        nivel_dim4 = "Avanzado"
        texto_dim4 = "La organizacion demostro un gran avance al tener  disponibles los datos y utilizar algunos de los formatos estandares abiertos mas conocidos para leerlos. Sin embargo, es recomendable disponer de APIs para que los usuarios externos puedan acceder a los datos. Asimismo, es importante difundir y utilizar el lenguaje adecuado para las distintas audiencias, en funcion de los datos y de lo que se produce con ellos (informacion demografica, informacion tributaria, etc). La disponibilidad de los datos es fundamental para la toma de decisiones informadas y realizar analisis, aunque tambien deben estar protegidos mediante politicas de seguridad de la informacion. "
        
     if Disponibilizacion_int >= 3 and Disponibilizacion_int<4:
        nivel_dim4 = "Experto"
        texto_dim4 = "La organizacion demostro un gran compromiso y avance la disponibilizacion de los datos. Pero es importante utilizar formatos estandar abiertos (CSV, JSON, XML, KML, GEOJSON) y desarrollar APIs para el acceso externo. Difundir y utilizar el lenguaje adecuado para diferentes audiencias (demografica, tributaria, etc.) es esencial. Los datos deben estar disponibles para la toma decisiones informadas y analisis pero tambien deben estar protegidos con politicas y procedimientos de seguridad de la informacion."
        
     if Disponibilizacion_int >= 4 and Disponibilizacion_int<=6:
        nivel_dim4 = "Mejora continua"
        texto_dim4 = "La organizacion al tener los datos disponibles de forma permanente y en formatos abiertos mejora el acceso para usuarios externos y fomenta su reutilizacion y es una excelente practica para la disponibilidad y transparencia de los datos. "
        
######

     if Proteccion_de_datos_int == 0:
        nivel_dim5 = "Cero"
        texto_dim5 = "Es importante conocer ambas normativas y asegurarse de cumplir con las obligaciones legales establecidas en cada una de ellas. Esto puede evitar posibles sanciones y multas por incumplimiento de las leyes de proteccion de datos y tambien ayuda a proteger la privacidad y seguridad de los datos personales de los titulares de los mismos."
        
     if Proteccion_de_datos_int > 0 and Proteccion_de_datos_int<1:
        nivel_dim5 = "Inicial"
        texto_dim5 = "Es fundamental  conocer y cumplir con las normativas legales para evitar sanciones y proteger la privacidad de los datos personales. Ademas, es importante establecer los limites de tiempo aceptables de permanencia de los datos en los sistemas para evitar, de esta forma, riesgos innecesarios para la seguridad y privacidad de los titulares de los datos."
        
     if Proteccion_de_datos_int >= 1 and Proteccion_de_datos_int<2:
        nivel_dim5 = "Medio"
        texto_dim5 = "La organizacion conoce las obligaciones legales, los tiempos en que deben permanecer los datos personales en los sistemas, la clasificacion de datos sensibles y el consentimiento informado. Para avanzar, se sugiere implementar mecanismos de minimizacion o destruccion periodica de datos, establecer espacios de dialogo y comites para abordar temas de proteccion de datos, como tambien disponer de lineamientos definidos para garantizar la privacidad, seguridad y cumplimiento normativo"
        
     if Proteccion_de_datos_int >= 2 and Proteccion_de_datos_int<3:
        nivel_dim5 = "Avanzado"
        texto_dim5 = "La organizacion cumple con las obligaciones legales, permanencia de los datos en los sistemas, clasificacion y minimizacion. Para robustecer aun mas la proteccion de datos se recomienda generar espacios de dialogo, establecer lineamientos claros de proteccion de datos y actualizarlos regularmente para reflejar cambios normativos. Esto garantizara una mayor adhesion y fortaleza en la proteccion de datos."
        
     if Proteccion_de_datos_int >= 3 and Proteccion_de_datos_int<4:
        nivel_dim5 = "Experto"
        texto_dim5 = "La organizacion conoce y cumple con las obligaciones legales, permanencia de datos en los sistemas, clasificacion y consentimiento. Se destaca la importancia de contar con lineamientos de proteccion de datos definidos, comunicados y actualizados periodicamente. Esto fortalecera la proteccion de datos, promovera la cultura de cumplimiento y seguridad en toda la organizacion."
        
     if Proteccion_de_datos_int >= 4 and Proteccion_de_datos_int<=6:
        nivel_dim5 = "Mejora continua"
        texto_dim5 = "La organizacion ha implementado practicas solidas de proteccion de datos y cuenta con lineamientos definidos. Esto garantiza un tratamiento coherente de los datos y cumplimiento normativo, ademas de promover una cultura de responsabilidad. Se recomienda seguir fortaleciendo el enfoque mediante capacitacion, evaluacion continua y medidas adicionales segun sea necesario para garantizar la proteccion y confianza en la privacidad de la informacion."

######

     if Gobernanza_de_datos_int == 0:
        nivel_dim6 = "Cero"
        texto_dim6 = "Es importante conocer los roles de cada integrante de la organizacion respecto de los datos. Es recomendable que esten bien definidos y relevados ya que esto ayuda a garantizar la seguridad y privacidad de los datos personales y a asegurar el cumplimiento de las regulaciones y leyes aplicables. Asimismo, facilita la asignacion de responsabilidades especificas a los agentes de la organizacion e impulsa el sostenimiento de una estructura de gobernanza para la gestion de los datos."
        
     if Gobernanza_de_datos_int > 0 and Gobernanza_de_datos_int<1:
        nivel_dim6 = "Inicial"
        texto_dim6 = "La organizacion debe establecer y cumplir politicas sobre el uso y acceso de los datos, garantizando la privacidad y seguridad de la informacion. Documentar el ciclo de vida de los datos y capacitar al personal en gobernanza de datos son acciones recomendadas para cumplir con las regulaciones y mejorar la eficiencia del trabajo."
        
     if Gobernanza_de_datos_int >= 1 and Gobernanza_de_datos_int<2:
        nivel_dim6 = "Medio"
        texto_dim6 = "La organizacion cuenta con politicas que garanticen el uso etico y responsable de los datos personales para la proteccion de la privacidad y los derechos de las personas. Documentar el ciclo de vida de los datos y capacitar al personal en gobernanza de datos son medidas adicionales recomendadas para cumplir con las regulaciones y mejorar la eficiencia en el manejo de los mismos."
        
     if Gobernanza_de_datos_int >= 2 and Gobernanza_de_datos_int<3:
        nivel_dim6 = "Avanzado"
        texto_dim6 = "La organizacion no tan solo conoce y cumple con las normativas legales, en este nivel es deseable documentar las etapas del ciclo de vida de los datos. Las capacitaciones en gobernanza de datos, en especial sobre clasificacion y roles, son fundamentales para garantizar la privacidad y seguridad de estos, proteger los derechos de las personas y cumplir con las regulaciones, mejorando la eficiencia"
        
     if Gobernanza_de_datos_int >= 3 and Gobernanza_de_datos_int<4:
        nivel_dim6 = "Experto"
        texto_dim6 = "La organizacion cuenta con las herramientas para la buena gestion y tratamiento de los datos y es recomendable para seguir en este camino documentar las etapas del ciclo de vida de los datos contar con lineamientos, ya que proporcionan coherencia, estandarizacion, reducen el riesgo y la incertidumbre, promueven la transparencia y la responsabilidad, aumentan la eficiencia, la productividad, y su gestion segura. Las capacitaciones en gobernanza de datos, en especial sobre clasificacion y roles, son fundamentales para garantizar la privacidad y seguridad de los datos, proteger los derechos de las personas y cumplir con las regulaciones, mejorando la eficiencia del personal."
        
     if Gobernanza_de_datos_int >= 4 and Gobernanza_de_datos_int<=6:
        nivel_dim6 = "Mejora continua"
        texto_dim6 = "La organizacion tomo medidas significativas en la gobernanza de datos. Mantener un enfoque proactivo y fortalecer aspectos clave ayudara a maximizar el valor de los datos, garantizar el cumplimiento normativo y la confianza de los stakeholders."

######

     if Gestion_de_acceso_a_datos_int == 0:
        nivel_dim7 = "Cero"
        texto_dim7 = "La organizacion debe establecer politicas claras, implementar sistemas y mecanismos de gestion de acceso a datos, capacitar al personal, garantizar la seguridad y privacidad de los datos ademas de cumplir con las regulaciones aplicables. Estas acciones ayudaran a mejorar la transparencia, la seguridad y la gestion adecuada de los datos en la institucion."
        
     if Gestion_de_acceso_a_datos_int > 0 and Gestion_de_acceso_a_datos_int<1:
        nivel_dim7 = "Inicial"
        texto_dim7 = "La organizacion esta dando sus primeros pasos en las buenas practicas de gestion de datos. Por lo tanto debe tener implementado un sistema o una politica de acceso a la informacion es fundamental para promover la transparencia, responsabilidad, eficiencia y proteccion de datos. Es importante destacar que la eleccion del sistema de acceso a la informacion dependera del nivel de seguridad que se requiera para proteger la informacion. Recomendamos contar con reportes de acceso a datos, ya que constituyen una importante herramienta para monitorear y mejorar la seguridad de la informacion y para cumplir con las regulaciones y normativas sobre esta. "
        
     if Gestion_de_acceso_a_datos_int >= 1 and Gestion_de_acceso_a_datos_int<2:
        nivel_dim7 = "Medio"
        texto_dim7 = "La organizacion esta demostrando que contar con reportes de acceso a los datos es un buen comienzo para monitorear y registrar las actividades relacionadas con el acceso a la informacion. Sin embargo, es importante tener un sistema de acceso robusto y seguro, implementado un control efectivo sobre quien tiene acceso a los datos y en que circunstancias, ello fortalecera la proteccion de los datos, reducira los riesgos de acceso no autorizado y facilitara la administracion y el monitoreo de los accesos, lo que resultara en una mayor eficiencia y cumplimiento normativo."
        
     if Gestion_de_acceso_a_datos_int >= 2 and Gestion_de_acceso_a_datos_int<3:
        nivel_dim7 = "Avanzado"
        texto_dim7 = "La organizacion implementa reportes de acceso a los datos y sistemas de acceso a la informacion. Estas medidas son fundamentales para garantizar la transparencia y la rendicion de cuentas en el manejo de los datos. Continuar fortaleciendo estas practicas a traves de politicas claras, seguridad de datos, evaluaciones periodicas y capacitacion adecuada ayudara a promover la transparencia, la seguridad y la confianza en la institucion. "
        
     if Gestion_de_acceso_a_datos_int >= 3 and Gestion_de_acceso_a_datos_int<4:
        nivel_dim7 = "Experto"
        texto_dim7 = "La organizacion  logro una excelencia, un alto grado de madurez en la gestion del acceso a los datos e implementacion de practicas solidas y avanzadas para garantizar la seguridad y el acceso adecuado a la informacion. En pos de alcanzar el nivel maximo los alentamos a seguir mejorando las politicas y controles de acceso, actualizandose en las mejores practicas y tecnologias. "
        
     if Gestion_de_acceso_a_datos_int >= 4 and Gestion_de_acceso_a_datos_int<=6:
        nivel_dim7 = "Mejora continua"
        texto_dim7 = "La organizacion demuestra una madurez y excelencia en el tratamiento y acceso seguro a los datos, mediante la implementacion de practicas solidas, con politicas y controles eficientes para proteger y garantizar el acceso a los datos. Es importante mantener esta forma de trabajo, evaluando y actualizando politicas y controles, con las ultimas tendencias y tecnologias en seguridad de datos promoviendo la capacitacion y lineamientos sobre la proteccion de datos. Asimismo, recomendamos que en sus experiencias con otras areas, fomenten una cultura de seguridad y colaboracion en la gestion del acceso a los datos. "

######

     if Calidad_de_los_datos_int == 0:
        nivel_dim8 = "Cero"
        texto_dim8 = "Recomendamos realizar controles periodicos en la calidad de los datos, fundamentalmente, con una periodicidad adecuada. Esto implica establecer procesos y procedimientos claros para llevar a cabo estas revisiones, asignar responsabilidades y recursos y utilizar herramientas o tecnicas adecuadas para realizar las verificaciones necesarias. A partir de ello, la organizacion mejorara la calidad de sus datos, fortalecera su toma de decisiones y cumplira con los estandares de calidad requeridos.  "
        
     if Calidad_de_los_datos_int > 0 and Calidad_de_los_datos_int<1:
        nivel_dim8 = "Inicial"
        texto_dim8 = "La organizacion tiene identificadas las diferentes dimensiones de los datos y es importante que avancen tanto en la implementacion de controles de calidad, como en la identificacion de las metricas de calidad que analizan esos controles. Tambien, se sugiere documentar los procesos y procedimientos que analicen el grado de cumplimiento de las dimensiones definidas y perfiles profesionales/tecnicos dedicados a evaluar periodicamente las metricas de calidad. "
        
     if Calidad_de_los_datos_int >= 1 and Calidad_de_los_datos_int<2:
        nivel_dim8 = "Medio"
        texto_dim8 = "La organizacion contribuye a generar confianza y eficiencia en la calidad de datos. Para mejorar es necesario definir metricas, documentar procesos y asignar recursos especializados que se dediquen a garantizar la precision y el cumplimiento de los requisitos normativos y las expectativas de los usuarios. "
        
     if Calidad_de_los_datos_int >= 2 and Calidad_de_los_datos_int<3:
        nivel_dim8 = "Avanzado"
        texto_dim8 = "La organizacion realiza controles de revision y usar metricas solidas son fundamentales para evaluar y mejorar la calidad de los datos. Recomendamos que, en paralelo, documenten los procesos y procedimientos y destinen a esta tarea perfiles profesionales/tecnicos que aseguren la consistencia y la mejora continua. "
        
     if Calidad_de_los_datos_int >= 3 and Calidad_de_los_datos_int<4:
        nivel_dim8 = "Experto"
        texto_dim8 = "La organizacion al encontrarse en este nivel demuestra que constantemente realizan mejoras e incorporan perfiles profesionales o tecnicos dedicados a evaluar periodicamente las metricas de calidad. Estos expertos aportaran conocimientos especializados, garantizaran un monitoreo constante, estableceran responsabilidad y rendicion de cuentas, fortaleciendo asi la toma de decisiones informadas y confiables basadas en datos de alta calidad. "
        
     if Calidad_de_los_datos_int >= 4 and Calidad_de_los_datos_int<=6:
        nivel_dim8 = "Mejora continua"
        texto_dim8 = "La organizacion tiene un enfoque riguroso en la gestion de la calidad de los datos. Alentamos a que continuen trabajando en dicha mejora, para asegurar que los datos sean precisos, relevantes y utiles para la toma de decisiones. Esto puede mejorar significativamente la capacidad de la organizacion para competir en el mercado y lograr sus objetivos. "

######

     if Reutilizacion_de_datos_int == 0:
        nivel_dim9 = "Cero"
        texto_dim9 = "Una organizacion gubernamental que no intercambia datos, que no tiene mecanismos definidos para compartirlos y carece de perfiles especializados en la reutilizacion de los mismos. Es complejo que puedan avanzar. Por lo cual es fundamental establecer politicas, marcos y capacidades para fomentar el intercambio seguro de datos y que puedan ser reutilizados. Ademas de promover esta cultura de reutilizacion, buscar colaboraciones externas, puede ayudar a avanzar hacia una gestion de datos mas eficiente y efectiva."
        
     if Reutilizacion_de_datos_int > 0 and Reutilizacion_de_datos_int<1:
        nivel_dim9 = "Inicial"
        texto_dim9 = "La organizacion esta demostrando interes y cuidado al intercambiar datos y fomentar su reutilizacion es valioso y puede generar beneficios significativos para el gobierno, las organizaciones y la sociedad. Es importante compartir los datos con areas internas y usuarios externos a la organizacion, establecer mecanismos definidos y contar con perfiles profesionales o tecnicos especializados en su reutilizacion. Esto les permitira aprovechar al maximo su valor, promover la colaboracion y la innovacion, mejorar la calidad de la informacion, cumplir con los requisitos normativos y eticos y fomentar una cultura de datos en la organizacion. "
        
     if Reutilizacion_de_datos_int >= 1 and Reutilizacion_de_datos_int<2:
        nivel_dim9 = "Medio"
        texto_dim9 = "La organizacion al intercambiar datos y fomentar su reutilizacion es beneficioso para el gobierno y la sociedad. Es importante que trabajen en compartir los datos con usuarios externos a la organizacion, establecer mecanismos definidos y contar con perfiles profesionales especializados en su reutilizacion. Esto permitira aprovechar al maximo su valor, promover la colaboracion y la innovacion, mejorar la calidad de la informacion, cumplir con los requisitos normativos y eticos y fomentar una cultura de datos en la organizacion. Recomendamos fortalecer estas practicas a traves de estandares abiertos, documentacion clara, portales de datos abiertos, licencias adecuadas y colaboracion activa, lo que ayudara a maximizar el potencial de los datos compartidos y promover una mayor innovacion y transparencia. "
        
     if Reutilizacion_de_datos_int >= 2 and Reutilizacion_de_datos_int<3:
        nivel_dim9 = "Avanzado"
        texto_dim9 = "La organizacion demuestra un gran avance en el equipo y esto hace a la importancia de contar con profesionales y tecnicos especializados en reutilizacion de datos para impulsar y gestionar de manera efectiva este proceso. Su conocimiento, experiencia en gobernanza, capacidad de analisis, habilidades de comunicacion y enfoque innovador son indispensables para generar un beneficio significativo tanto para el gobierno como para la sociedad."
        
     if Reutilizacion_de_datos_int >= 3 and Reutilizacion_de_datos_int<4:
        nivel_dim9 = "Experto"
        texto_dim9 = "La organizacion tiene mecanismos definidos para que las personas de la organizacion compartan datos con un proposito determinado es esencial para el buen desempeño de una organizacion, promueve la transparencia, la colaboracion, la toma de decisiones basadas en evidencia, la innovacion y el desarrollo de servicios centrados en las personas, y se aprovechan al maximo los datos disponibles. Seria importante acompañar esto con profesionales y tecnicos especializados en reutilizacion de datos que impulsen y gestionen de manera efectiva este proceso. Su conocimiento tecnico, experiencia en gobernanza de datos, capacidad de analisis, habilidades de comunicacion y enfoque innovador son indispensables para el valor de los datos y generar beneficios significativos tanto para la organizacion como para la sociedad."
        
     if Reutilizacion_de_datos_int >= 4 and Reutilizacion_de_datos_int<=6:
        nivel_dim9 = "Mejora continua"
        texto_dim9 = "La organizacion no tan solo tienen definidos los mecanismos para compartir datos con un proposito determinado, sino que cuentan con perfiles profesionales especializados en su reutilizacion. Esta combinacion es altamente valiosa y brinda una base solida para aprovechar al maximo los datos y promover la innovacion y la transparencia. Continuar fortaleciendo estas practicas y fomentando una cultura de reutilizacion de datos permitira aprovechar plenamente el potencial de los datos, mejorar la prestacion de servicios y promover la innovacion en beneficio de la sociedad. "

######

     if Modelo_de_datos_int == 0:
        nivel_dim10 = "Cero"
        texto_dim10 = "Cuando una organizacion no cuenta con un modelo de datos bien documentado y recursos especializados en el tema es importante reconocer la necesidad de trabajar en estos aspectos. Priorizar la implementacion de un modelo de datos, contratar o capacitar especialistas en el tema, realizar un analisis exhaustivo de los datos existentes, establecer estandares y mejores practicas y fomentar la colaboracion interdepartamental, ayudaran a mejorar la gestion de los datos y sentaran las bases para tomar decisiones informadas y eficientes."
        
     if Modelo_de_datos_int > 0 and Modelo_de_datos_int<1:
        nivel_dim10 = "Inicial"
        texto_dim10 = "La organizacion al tener este  Inicial, destaca la  necesidad e importancia de tener un modelo de datos definido que garantice la estructura e integridad de los datos. Recomendamos destinar recursos especializados para documentarlo. Estas acciones promueven la gestion efectiva de los datos y respaldan la toma de decisiones basadas en datos confiables. "
        
     if Modelo_de_datos_int >= 1 and Modelo_de_datos_int<2:
        nivel_dim10 = "Medio"
        texto_dim10 = "La organizacion en este Medio demuestra  la importancia de avanzar para lograr contar con un modelo de datos definido que garantice la estructura, organizacion e integridad de los datos. Recomendamos destinar recursos especializados para documentarlo. Estas acciones promueven la gestion efectiva de los datos y respaldan la toma de decisiones basadas en datos confiables. "
        
     if Modelo_de_datos_int >= 2 and Modelo_de_datos_int<3:
        nivel_dim10 = "Avanzado"
        texto_dim10 = "La organizacion demuestra que cuentan con un modelo de datos definido para garantizar la estructura, organizacion e integridad de los datos. Recomendamos destinar recursos especializados para implementar mejoras en el modelo de datos. Estas acciones fortaleceran la calidad y el valor de los datos de la organizacion. "
        
     if Modelo_de_datos_int >= 3 and Modelo_de_datos_int<4:
        nivel_dim10 = "Experto"
        texto_dim10 = "La organizacion en este nivel demuestra un gran compromiso, ya que  contar con un modelo de datos documentado facilita el diseño de sistemas, el mantenimiento y cumplimiento de los requisitos normativos. Recomendamos destinar recursos especializados en modelo de datos para garantizar un enfoque solido y eficiente en el almacenamiento, acceso y uso de los datos. "
        
     if Modelo_de_datos_int >= 4 and Modelo_de_datos_int<=6:
        nivel_dim10 = "Mejora continua"
        texto_dim10 = "La organizacion tienen un modelo de datos bien documentado y cuentan con personas especializadas en el tema. Continuen trabajando en el mantenimiento, la colaboracion, la promocion de buenas practicas, la capacitacion y el monitoreo, para seguir mejorando y maximizando el valor de su modelo de datos en beneficio de la organizacion. "

     if Promedio == 0:
         nivel_final = "Cero"
         texto_final = "Indica que la organizacion, no contempla lo suficiente el valor de los datos  en la toma de decisiones no es suficientemente apreciado y promovido en la organizacion. Estar en este nivel implica que la organizacion debe comenzar a tomar en cuenta la buena gestion de los datos para avanzar hacia los siguientes niveles de madurez. "

     if Promedio > 0 and Promedio< 1:
         nivel_final = "Inicial"
         texto_final = "Indica que la organizacion reconoce que los datos son un activo invaluable para la toma de decisiones. Para seguir creciendo en la madurez de los datos de la organizacion podria centrarse en aspectos como la calidad de los datos, la gestion de datos, el analisis de datos, la cultura de datos e innovacion y mejora continua en la gestion de datos. "

     if Promedio >= 1 and Promedio< 2:
         nivel_final = "Medio"
         texto_final = "Indica que la  organizacion ha logrado una comprension adecuada de la importancia de los datos como un activo fundamental. Es importante desarrolladar una conciencia solida de los datos como un activo clave. Para seguir creciendo en la madurez de los datos en  la organizacion podria enfocarse en la gestion de datos, gobernanza de datos, calidad e integridad de los datos, el analisis de datos avanzado, impulsar una cultura de datos, un enfoque continuo en la mejorar las practicas de gestion de datos y un impacto significativo en la toma de decisiones."
         
     if Promedio >= 2 and Promedio< 3:
         nivel_final = "Avanzado"
         texto_final = "Indica que la organizacion  ha logrado un reconocimiento pleno de la importancia de los datos para el exito en la toma de decisiones basadas en datos. Para avanzar a un Experto recomendamos centrarse en la innovacion en el uso de datos, la integracion de datos, contar con lineamientos, procesos documentados para la gestion de riesgos y seguridad de datos. El enfoque en la mejora continua y aprendizaje."  
         
     if Promedio >= 3 and Promedio< 4:
         nivel_final = "Experto"
         texto_final = "Indica que la organizacion comprende plenamente la importancia de contar con una excelente infraestructura de datos en todos los niveles, que sus equipos estan conformados por expertos en la materia y buscan tener  datos de calidad y reconocen que esto le proporciona una ventaja competitiva en la toma de decisiones.Para no descuidar el nivel logrado de madurez la organizacion debe enfocarse en la gobernanza de datos, la automatizacion y escalabilidad, la cultura de datos centrada en el valor, la innovacion continua y la colaboracion con los actores que sean necesarios, formar equipos interdisciplinarios para seguir mejorando sus practicas de gestion de datos."
         
     if Promedio >= 4 and Promedio< 6:
         nivel_final = "Mejora continua"
         texto_final = "Indica que la organización implementa constantemente mecanismos para la buena gestion de los datos, busca  aprender de las experiencias, auditar y revisar los procesos y compartir las mejores practicas. Estas acciones demuestran un enfoque constante en la mejora y la optimizacion de las practicas de tratamiento de datos, lo que permite a la organizacion seguir evolucionando y alcanzar niveles mas altos de madurez en el futuro"


     p7_area_cienc_dat = str(scores.iloc[i]['p7'])
     p12_tien_report = str(scores.iloc[i]['p12'])
     p38_model_dat = str(scores.iloc[i]['p38'])
     
     if int(p7_area_cienc_dat)  == -1:
         texto_dim2 = "Esta dimensión no será considerada debido a que respondió que no la aplica en su área"

        
     if int(p12_tien_report)  == -1:
         texto_dim3 = "Esta dimensión no será considerada debido a que respondió que no la aplica en su área"

        
     if int(p38_model_dat)  == -1:
         texto_dim10 = "Esta dimensión no será considerada debido a que respondió que no la aplica en su área"
   

     p.write(str(i+1)+";"+Fecha+";"+NombreApellido+";"+mail+";"+cargo+";"+Organismo+
            ";"+str(Fuente_de_informacion_Integracion_int).replace(".", ",")+";"+nivel_dim1+";"+texto_dim1+  \
            ";"+str(Ciencia_de_datos_int).replace(".", ",")+";"+nivel_dim2+";"+texto_dim2+ \
            ";"+str(Actualidad_de_Reportes_productos_int).replace(".", ",")+";"+nivel_dim3+";"+texto_dim3+ \
            ";"+str(Disponibilizacion_int).replace(".", ",")+";"+nivel_dim4+";"+texto_dim4+ \
            ";"+str(Proteccion_de_datos_int).replace(".", ",")+";"+nivel_dim5+";"+texto_dim5+ \
            ";"+str(Gobernanza_de_datos_int).replace(".", ",")+";"+nivel_dim6+";"+texto_dim6+ \
            ";"+str(Gestion_de_acceso_a_datos_int).replace(".", ",")+";"+nivel_dim7+";"+texto_dim7+ \
            ";"+str(Calidad_de_los_datos_int).replace(".", ",")+";"+nivel_dim8+";"+texto_dim8+ \
            ";"+str(Reutilizacion_de_datos_int).replace(".", ",")+";"+nivel_dim9+";"+texto_dim9+ \
            ";"+str(Modelo_de_datos_int).replace(".", ",")+";"+nivel_dim10+";"+texto_dim10+ \
            ";"+str(Promedio).replace(".", ",")+";"+nivel_final+";"+texto_final+"\n")       


# #p = open("textos_monica.csv", "w")
# titulo = 'Nivel 1'+";"+"Texto Nivel 1"+";"+'Nivel 2'+";"+"Texto Nivel 2"+";"+'Nivel 3'+";"+"Texto Nivel 3"+";"+'Nivel 4'+";"+"Texto Nivel 4"+";"+'Nivel 5'+";"+"Texto Nivel 5"+";"+'Nivel 6'+";"+"Texto Nivel 6"+";"+'Nivel 7'+";"+"Texto Nivel 7"+";"+'Nivel 8'+";"+"Texto Nivel 8"+";"+'Nivel 9'+";"+"Texto Nivel 9"+";"+'Nivel 10'+";"+"Texto Nivel 10"+"\n"
# p.write(titulo)
# p.write(nivel_dim1+";"+texto_dim1+";"+nivel_dim2+";"+texto_dim2+";"+nivel_dim3+";"+texto_dim3+";"+nivel_dim4+";"+texto_dim4+";"+nivel_dim5+";"+texto_dim5+";"+nivel_dim6+";"+texto_dim6+";"+nivel_dim7+";"+texto_dim7+";"+nivel_dim8+";"+texto_dim8+";"+nivel_dim9+";"+texto_dim9+";"+nivel_dim10+";"+texto_dim10+";"+"\n")
# p.write(";"+"\n")
# p.write(";"+"\n")
# p.write(";"+"\n")
# p.write("Valores Finales ;"+"\n")

# p.write(nivel_final+";"+texto_final+"\n")
p.close()