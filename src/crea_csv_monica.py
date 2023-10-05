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



scores = pd.read_csv('Score_Final.csv',index_col=False, encoding='utf-8',sep='')

for i in range(len(scores)):
     Fecha                             = str(scores.iloc[i]['Fecha'])
     NombreApellido                    = str(scores.iloc[i]['NombreApellido'])
     mail                              = str(scores.iloc[i]['mail'])
     cargo                             = str(scores.iloc[i]['Area'])   
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

     Suma = Fuente_de_informacion_Integracion_int + Ciencia_de_datos_int + Actualidad_de_Reportes_productos_int+Disponibilizacion_int +Proteccion_de_datos_int +Gobernanza_de_datos_int +Gestion_de_acceso_a_datos_int+Calidad_de_los_datos_int+Reutilizacion_de_datos_int +Modelo_de_datos_int                   
     Promedio = Suma / 10

     if Fuente_de_informacion_Integracion_int == 0:
        nivel_dim1 = "Cero"
        texto_dim1 = "En el camino de la mejora deberán desarrollar la integración y recolección de datos para garantizar la consistencia y actualización de la información. Es fundamental poseer una base de datos propia con tecnología de integración y documentar las políticas de dicha integración. Esto proporcionará claridad, transparencia y garantizará el cumplimiento normativo. Asimismo, les permitirá la planificación de estrategias, lo que impactará positivamente en el rendimiento de la organización."

     if Fuente_de_informacion_Integracion_int > 0 and Fuente_de_informacion_Integracion_int<1:
        nivel_dim1 = "Inicial"
        texto_dim1 = "La organización debe especializarse en la recopilación de datos y en la implementación de una estrategia de integración y aprovechamiento de la información. Es decir, debe contar con bases de datos propias para gestionar eficientemente los datos, mejorando su accesibilidad y análisis, lo que además le permitirá avanzar en el desarrollo de la integración de los datos."

     if Fuente_de_informacion_Integracion_int >= 1 and Fuente_de_informacion_Integracion_int<2:
        nivel_dim1 = "Medio"
        texto_dim1 = "La organización cuenta con bases de datos propias, lo que robustece la integración de datos de diferentes fuentes e impulsa la toma de decisiones informadas y la identificación de patrones en los datos para obtener ventajas competitivas."
        
     if Fuente_de_informacion_Integracion_int >= 2 and Fuente_de_informacion_Integracion_int<3:
        nivel_dim1 = "Avanzado"
        texto_dim1 = "La organización cuenta con una estrategia de integración de datos que maximiza su valor, mejora la toma de decisiones y la eficiencia operativa. Bases de datos propias, gestión responsable y capacidad de integrar datos de múltiples fuentes, brindan ventajas competitivas. Documentar políticas de integración asegura consistencia, cumplimiento normativo, calidad de datos y comunicación efectiva."

     if Fuente_de_informacion_Integracion_int >= 3 and Fuente_de_informacion_Integracion_int<4:
        nivel_dim1 = "Experto"
        texto_dim1 = "La organización ha demostrado su progreso en el tratamiento de datos demuestra un enfoque destacado en la toma de decisiones. Asimismo, puede seguir progresando mediante la evaluación constante, la adopción de tecnologías y la capacitación continua para cerrar la brecha hacia la máxima madurez en la gestión de datos."

     if Fuente_de_informacion_Integracion_int >= 4 and Fuente_de_informacion_Integracion_int<=6:
        nivel_dim1 = "Mejora continua"
        texto_dim1 = "La organización al estar en este nivel refleja el compromiso con el tratamiento adecuado de los datos como un activo de valor. Es fundamental a seguir trabajando en este camino para el logro de niveles aún más avanzados de madurez en la gestión de datos."



######

     if Ciencia_de_datos_int == 0:
        nivel_dim2 = "Cero"
        texto_dim2 = "Es recomendable contar con áreas de desarrollo de ciencia de datos, ya que es beneficiosa en diversos aspectos, fundamentalmente para la toma de decisiones informadas. Es importante identificar las oportunidades de mejora que se pueden alcanzar a partir de la implementación de capacidades en este tema."
        
     if Ciencia_de_datos_int > 0 and Ciencia_de_datos_int<1:
        nivel_dim2 = "Inicial"
        texto_dim2 = "La organización demuestra el reconocimiento de la importancia de la Ciencia de Datos. En este nivel, podrán fortalecer su capacidad respecto de la toma de decisiones informadas y aprovechar al máximo el potencial de los datos disponibles mediante el desarrollo y entrenamiento de modelos de aprendizaje automático, análisis predictivo y su documentación."
        
     if Ciencia_de_datos_int >= 1 and Ciencia_de_datos_int<2:
        nivel_dim2 = "Medio"
        texto_dim2 = "La organización va por un buen camino y la aplicación de técnicas estadísticas, modelos de aprendizaje automático y análisis predictivo. Es fundamental para seguir avanzando, es crucial documentar sistemáticamente los proyectos para garantizar la replicabilidad y la transparencia como también la transferencia de conocimientos y el cumplimiento normativo."
        
     if Ciencia_de_datos_int >= 2 and Ciencia_de_datos_int<3:
        nivel_dim2 = "Avanzado"
        texto_dim2 = "La organización debe continuar invirtiendo en habilidades técnicas, actualizándose en tendencias y colaborando con expertos externos para maximizar el valor de los datos para la toma de decisiones y así lograr niveles más avanzados de madurez."
        
     if Ciencia_de_datos_int >= 3 and Ciencia_de_datos_int<4:
        nivel_dim2 = "Experto"
        texto_dim2 = "La organización demostro madurez y prácticas avanzadas en el tratamiento de datos. Recomendamos que continúen invirtiendo en capacitación, colaboración externa y seguimiento de avances para maximizar el valor de los datos para la toma de decisiones más eficientes para la organización."
        
     if Ciencia_de_datos_int >= 4 and Ciencia_de_datos_int<=6:
        nivel_dim2 = "Mejora continua"
        texto_dim2 = "La organización demostró dedicación y prácticas avanzadas en el tratamiento de los datos un grado avanzado de madurez. Instamos a que continúen actualizándose y explorando nuevas aplicaciones para continuar la innovación basada en datos."
        

######

     if Actualidad_de_Reportes_productos_int == 0:
        nivel_dim3 = "Cero"
        texto_dim3 = "Disponer de reportes actualizados es fundamental para garantizar la transparencia, la rendición de cuentas, la toma de decisiones informadas, la evaluación, así como la comunicación interna y externa efectiva. Es recomendable el diseño de un sistema que contenga un componente para la generación y la publicación de reportes de forma regular, que reflejen sus actividades, resultados e impacto."
        
     if Actualidad_de_Reportes_productos_int > 0 and Actualidad_de_Reportes_productos_int<1:
        nivel_dim3 = "Inicial"
        texto_dim3 = "La organización dispone de reportes de datos, aunque es importante automatizarlos y actualizarlos con frecuencia. Recopilar la opinión de los usuarios y ajustar los procesos de actualización mejora la toma de decisiones y la comunicación en la organización."
        
     if Actualidad_de_Reportes_productos_int >= 1 and Actualidad_de_Reportes_productos_int<2:
        nivel_dim3 = "Medio"
        texto_dim3 = "La organización genera reportes de datos actualizados regularmente. Pero se recomienda su automatización. Es esencial trabajar con las devoluciones de los usuarios para ajustar los procesos de actualización en función de sus experiencias de uso. Los informes precisos y accesibles son fundamentales para la toma de decisiones y la comunicación efectiva."
        
     if Actualidad_de_Reportes_productos_int >= 2 and Actualidad_de_Reportes_productos_int<3:
        nivel_dim3 = "Avanzado"
        texto_dim3 = "La organización genera reportes de datos actualizados y automatizados con frecuencia. Es recomendable realizar ajustes en los procesos de actualización según los comentarios de los usuarios, ya que es fundamental para mejorar los informes y demostrar que sus opiniones son valoradas."
        
     if Actualidad_de_Reportes_productos_int >= 3 and Actualidad_de_Reportes_productos_int<4:
        nivel_dim3 = "Experto"
        texto_dim3 = "La organización demuestra un alto grado de madurez en el tratamiento de los datos para generar reportes y productos actualizados habilidades sólidas y conocimientos en la generación de reportes y productos basados en datos mediante procesos eficientes. Para continuar avanzando recomendamos que continúen evaluando y mejorando periódicamente sus procesos, aprovechando las últimas tendencias y tecnologías en la generación de reportes y productos basados en datos."
        
     if Actualidad_de_Reportes_productos_int >= 4 and Actualidad_de_Reportes_productos_int<=6:
        nivel_dim3 = "Mejora continua"
        texto_dim3 = "La organización demuestra una madurez en el tratamiento de datos, generación de reportes relevantes y establecimiento de procesos sólidos reflejan un enfoque destacado en la toma de decisiones. Los aldentamos a que continúen en este camino optimizando y compartiendo prácticas eficientes para impulsar la cultura de mejora continua."
        
######

     if Disponibilizacion_int == 0:
        nivel_dim4 = "Cero"
        texto_dim4 = "La organización deberían contar con datos disponibles para tomar decisiones informadas y realizar análisis. La disponibilidad de datos también debe estar en línea con las políticas de privacidad y seguridad de la información."
        
     if Disponibilizacion_int > 0 and Disponibilizacion_int<1:
        nivel_dim4 = "Inicial"
        texto_dim4 = "La organización debe asegurarse de tener los datos disponibles con regularidad y en formatos estándar abiertos como CSV, JSON, XML, KML, GEOJSON, a los fines de tomar decisiones informadas y realizar análisis. Además, es importante desarrollar APIs para permitir el acceso externo y utilizar un lenguaje adecuado según la audiencia (demográfica, tributaria, etc.). Asimismo, es importante que los datos estén protegidos mediante políticas de seguridad de la información."
        
     if Disponibilizacion_int >= 1 and Disponibilizacion_int<2:
        nivel_dim4 = "Medio"
        texto_dim4 = "La organización debe procurar  disponibilizar los datos  en formatos estándar abiertos como CSV, JSON, XML, KML, GEOJSON desarrollar APIs para permitir el acceso externo y utilizar un lenguaje adecuado según la audiencia (demográfica, tributaria, etc.). La disponibilidad de los datos es fundamental para la toma de decisiones informadas y realizar analisis, aunque también deben estar protegidos mediante políticas de seguridad de la información."
        
     if Disponibilizacion_int >= 2 and Disponibilizacion_int<3:
        nivel_dim4 = "Avanzado"
        texto_dim4 = "La organización demostró un gran avance al tener  disponibles los datos y utilizar algunos de los formatos estándares abiertos más conocidos para leerlos. Sin embargo, es recomendable disponer de API´s para que los usuarios externos puedan acceder a los datos. Asimismo, es importante difundir y utilizar el lenguaje adecuado para las distintas audiencias, en función de los datos y de lo que se produce con ellos (información demográfica, información tributaria, etc). La disponibilidad de los datos es fundamental para la toma de decisiones informadas y realizar analisis, aunque también deben estar protegidos mediante políticas de seguridad de la información. "
        
     if Disponibilizacion_int >= 3 and Disponibilizacion_int<4:
        nivel_dim4 = "Experto"
        texto_dim4 = "La organización demostró un gran compromiso y avance la disponibilización de los datos.Pero es importante utilizar formatos estándar abiertos (CSV, JSON, XML, KML, GEOJSON) y desarrollar APIs para el acceso externo. Difundir y utilizar el lenguaje adecuado para diferentes audiencias (demográfica, tributaria, etc.) es esencial. Los datos deben estar disponibles para la toma decisiones informadas y análisis pero también deben estar protegidos con políticas y procedimientos de seguridad de la información."
        
     if Disponibilizacion_int >= 4 and Disponibilizacion_int<=6:
        nivel_dim4 = "Mejora continua"
        texto_dim4 = "La organización al tener los datos disponibles de forma permanente y en formatos abiertos mejora el acceso para usuarios externos y fomenta su reutilización y es una excelente práctica para la disponibilidad y transparencia de los datos. "
        
######

     if Proteccion_de_datos_int == 0:
        nivel_dim5 = "Cero"
        texto_dim5 = "Es importante conocer ambas normativas y asegurarse de cumplir con las obligaciones legales establecidas en cada una de ellas. Esto puede evitar posibles sanciones y multas por incumplimiento de las leyes de protección de datos y también ayuda a proteger la privacidad y seguridad de los datos personales de los titulares de los mismos."
        
     if Proteccion_de_datos_int > 0 and Proteccion_de_datos_int<1:
        nivel_dim5 = "Inicial"
        texto_dim5 = "Es fundamental  conocer y cumplir con las normativas legales para evitar sanciones y proteger la privacidad de los datos personales. Además, es importante establecer los límites de tiempo aceptables de permanencia de los datos en los sistemas para evitar, de esta forma, riesgos innecesarios para la seguridad y privacidad de los titulares de los datos."
        
     if Proteccion_de_datos_int >= 1 and Proteccion_de_datos_int<2:
        nivel_dim5 = "Medio"
        texto_dim5 = "La organización conoce las obligaciones legales, los tiempos en que deben permanecer los datos personales en los sistemas, la clasificación de datos sensibles y el consentimiento informado. Para avanzar, se sugiere implementar mecanismos de minimización o destrucción periódica de datos, establecer espacios de diálogo y comités para abordar temas de protección de datos, como también disponer de lineamientos definidos para garantizar la privacidad, seguridad y cumplimiento normativo"
        
     if Proteccion_de_datos_int >= 2 and Proteccion_de_datos_int<3:
        nivel_dim5 = "Avanzado"
        texto_dim5 = "La organización cumple con las obligaciones legales, permanencia de los datos en los sistemas, clasificación y minimización. Para robustecer aún más la protección de datos se recomienda generar espacios de diálogo, establecer lineamientos claros de protección de datos y actualizarlos regularmente para reflejar cambios normativos. Esto garantizará una mayor adhesión y fortaleza en la protección de datos."
        
     if Proteccion_de_datos_int >= 3 and Proteccion_de_datos_int<4:
        nivel_dim5 = "Experto"
        texto_dim5 = "La organización conoce y cumple con las obligaciones legales, permanencia de datos en los sistemas, clasificación y consentimiento. Se destaca la importancia de contar con lineamientos de protección de datos definidos, comunicados y actualizados periódicamente. Esto fortalecerá la protección de datos, promoverá la cultura de cumplimiento y seguridad en toda la organización."
        
     if Proteccion_de_datos_int >= 4 and Proteccion_de_datos_int<=6:
        nivel_dim5 = "Mejora continua"
        texto_dim5 = "La organización ha implementado prácticas sólidas de protección de datos y cuenta con lineamientos definidos. Esto garantiza un tratamiento coherente de los datos y cumplimiento normativo, además de promover una cultura de responsabilidad. Se recomienda seguir fortaleciendo el enfoque mediante capacitación, evaluación continua y medidas adicionales según sea necesario para garantizar la protección y confianza en la privacidad de la información."

######

     if Gobernanza_de_datos_int == 0:
        nivel_dim6 = "Cero"
        texto_dim6 = "Es importante conocer los roles de cada integrante de la organización respecto de los datos. Es recomendable que estén bien definidos y relevados ya que esto ayuda a garantizar la seguridad y privacidad de los datos personales y a asegurar el cumplimiento de las regulaciones y leyes aplicables. Asimismo, facilita la asignación de responsabilidades específicas a los agentes de la organización e impulsa el sostenimiento de una estructura de gobernanza para la gestión de los datos."
        
     if Gobernanza_de_datos_int > 0 and Gobernanza_de_datos_int<1:
        nivel_dim6 = "Inicial"
        texto_dim6 = "La organización debe establecer y cumplir políticas sobre el uso y acceso de los datos, garantizando la privacidad y seguridad de la información. Documentar el ciclo de vida de los datos y capacitar al personal en gobernanza de datos son acciones recomendadas para cumplir con las regulaciones y mejorar la eficiencia del trabajo."
        
     if Gobernanza_de_datos_int >= 1 and Gobernanza_de_datos_int<2:
        nivel_dim6 = "Medio"
        texto_dim6 = "La organización cuenta con políticas que garanticen el uso ético y responsable de los datos personales para la protección de la privacidad y los derechos de las personas. Documentar el ciclo de vida de los datos y capacitar al personal en gobernanza de datos son medidas adicionales recomendadas para cumplir con las regulaciones y mejorar la eficiencia en el manejo de los mismos."
        
     if Gobernanza_de_datos_int >= 2 and Gobernanza_de_datos_int<3:
        nivel_dim6 = "Avanzado"
        texto_dim6 = "La organización no tan solo conoce y cumple con las normativas legales, en este nivel es deseable documentar las etapas del ciclo de vida de los datos. Las capacitaciones en gobernanza de datos, en especial sobre clasificación y roles, son fundamentales para garantizar la privacidad y seguridad de estos, proteger los derechos de las personas y cumplir con las regulaciones, mejorando la eficiencia"
        
     if Gobernanza_de_datos_int >= 3 and Gobernanza_de_datos_int<4:
        nivel_dim6 = "Experto"
        texto_dim6 = "La organización cuenta con las herramientas para la buena gestión y tratamiento de los datos y es recomendable para seguir en este camino documentar las etapas del ciclo de vida de los datos contar con lineamientos, ya que proporcionan coherencia, estandarización, reducen el riesgo y la incertidumbre, promueven la transparencia y la responsabilidad, aumentan la eficiencia, la productividad, y su gestión segura. Las capacitaciones en gobernanza de datos, en especial sobre clasificación y roles, son fundamentales para garantizar la privacidad y seguridad de los datos, proteger los derechos de las personas y cumplir con las regulaciones, mejorando la eficiencia del personal."
        
     if Gobernanza_de_datos_int >= 4 and Gobernanza_de_datos_int<=6:
        nivel_dim6 = "Mejora continua"
        texto_dim6 = "La organización tomó medidas significativas en la gobernanza de datos. Mantener un enfoque proactivo y fortalecer aspectos clave ayudará a maximizar el valor de los datos, garantizar el cumplimiento normativo y la confianza de los stakeholders."

######

     if Gestion_de_acceso_a_datos_int == 0:
        nivel_dim7 = "Cero"
        texto_dim7 = "La organización debe establecer políticas claras, implementar sistemas y mecanismos de gestión de acceso a datos, capacitar al personal, garantizar la seguridad y privacidad de los datos además de cumplir con las regulaciones aplicables. Estas acciones ayudarán a mejorar la transparencia, la seguridad y la gestión adecuada de los datos en la institución."
        
     if Gestion_de_acceso_a_datos_int > 0 and Gestion_de_acceso_a_datos_int<1:
        nivel_dim7 = "Inicial"
        texto_dim7 = "La organización esta dando sus primeros pasos en las buenas practicas de gestión de datos. Por lo tanto debe tener implementado un sistema o una política de acceso a la información es fundamental para promover la transparencia, responsabilidad, eficiencia y protección de datos. Es importante destacar que la elección del sistema de acceso a la información dependerá del nivel de seguridad que se requiera para proteger la información. Recomendamos contar con reportes de acceso a datos, ya que constituyen una importante herramienta para monitorear y mejorar la seguridad de la información y para cumplir con las regulaciones y normativas sobre esta. "
        
     if Gestion_de_acceso_a_datos_int >= 1 and Gestion_de_acceso_a_datos_int<2:
        nivel_dim7 = "Medio"
        texto_dim7 = "La organización esta demostrando que contar con reportes de acceso a los datos es un buen comienzo para monitorear y registrar las actividades relacionadas con el acceso a la información. Sin embargo, es importante tener un sistema de acceso robusto y seguro, implementado un control efectivo sobre quién tiene acceso a los datos y en qué circunstancias, ello fortalecerá la protección de los datos, reducirá los riesgos de acceso no autorizado y facilitará la administración y el monitoreo de los accesos, lo que resultará en una mayor eficiencia y cumplimiento normativo."
        
     if Gestion_de_acceso_a_datos_int >= 2 and Gestion_de_acceso_a_datos_int<3:
        nivel_dim7 = "Avanzado"
        texto_dim7 = "La organización implementa reportes de acceso a los datos y sistemas de acceso a la información. Estas medidas son fundamentales para garantizar la transparencia y la rendición de cuentas en el manejo de los datos.Continuar fortaleciendo estas prácticas a través de políticas claras, seguridad de datos, evaluaciones periódicas y capacitación adecuada ayudará a promover la transparencia, la seguridad y la confianza en la institución. "
        
     if Gestion_de_acceso_a_datos_int >= 3 and Gestion_de_acceso_a_datos_int<4:
        nivel_dim7 = "Experto"
        texto_dim7 = "La organización  logro una excelencia, un alto grado de madurez en la gestión del acceso a los datos e implementacion de prácticas sólidas y avanzadas para garantizar la seguridad y el acceso adecuado a la información. En pos de alcanzar el nivel máximo los alentamos a seguir mejorando las políticas y controles de acceso, actualizándose en las mejores prácticas y tecnologías. "
        
     if Gestion_de_acceso_a_datos_int >= 4 and Gestion_de_acceso_a_datos_int<=6:
        nivel_dim7 = "Mejora continua"
        texto_dim7 = "La organización demuestra una madurez y excelencia en el tratamiento y acceso seguro a los datos, mediante la implementación de prácticas sólidas, con políticas y controles eficientes para proteger y garantizar el acceso a los datos. Es importante mantener esta forma de trabajo, evaluando y actualizando políticas y controles, con las últimas tendencias y tecnologías en seguridad de datos promoviendo la capacitación y lineamientos sobre la protección de datos. Asimismo, recomendamos que en sus experiencias con otras áreas, fomenten una cultura de seguridad y colaboración en la gestión del acceso a los datos. "

######

     if Calidad_de_los_datos_int == 0:
        nivel_dim8 = "Cero"
        texto_dim8 = "Recomendamos realizar controles periódicos en la calidad de los datos, fundamentalmente, con una periodicidad adecuada. Esto implica establecer procesos y procedimientos claros para llevar a cabo estas revisiones, asignar responsabilidades y recursos y utilizar herramientas o técnicas adecuadas para realizar las verificaciones necesarias. A partir de ello, la organización mejorará la calidad de sus datos, fortalecerá su toma de decisiones y cumplirá con los estándares de calidad requeridos.  "
        
     if Calidad_de_los_datos_int > 0 and Calidad_de_los_datos_int<1:
        nivel_dim8 = "Inicial"
        texto_dim8 = "La organización tiene identificadas las diferentes dimensiones de los datos y es importante que avancen tanto en la implementación de controles de calidad, como en la identificación de las métricas de calidad que analizan esos controles. También, se sugiere documentar los procesos y procedimientos que analicen el grado de cumplimiento de las dimensiones definidas y perfiles profesionales/técnicos dedicados a evaluar periódicamente las métricas de calidad. "
        
     if Calidad_de_los_datos_int >= 1 and Calidad_de_los_datos_int<2:
        nivel_dim8 = "Medio"
        texto_dim8 = "La organización contribuye a generar confianza y eficiencia en la calidad de datos. Para mejorar es necesario definir métricas, documentar procesos y asignar recursos especializados que se dediquen a garantizar la precisión y el cumplimiento de los requisitos normativos y las expectativas de los usuarios. "
        
     if Calidad_de_los_datos_int >= 2 and Calidad_de_los_datos_int<3:
        nivel_dim8 = "Avanzado"
        texto_dim8 = "La organización realiza controles de revisión y usar métricas sólidas son fundamentales para evaluar y mejorar la calidad de los datos. Recomendamos que, en paralelo, documenten los procesos y procedimientos y destinen a esta tarea perfiles profesionales/técnicos que aseguren la consistencia y la mejora continua. "
        
     if Calidad_de_los_datos_int >= 3 and Calidad_de_los_datos_int<4:
        nivel_dim8 = "Experto"
        texto_dim8 = "La organización al encontrarse en este nivel demuestra que constantemente realizan mejoras e incorporan perfiles profesionales o técnicos dedicados a evaluar periódicamente las métricas de calidad. Estos expertos aportarán conocimientos especializados, garantizarán un monitoreo constante, establecerán responsabilidad y rendición de cuentas, fortaleciendo así la toma de decisiones informadas y confiables basadas en datos de alta calidad. "
        
     if Calidad_de_los_datos_int >= 4 and Calidad_de_los_datos_int<=6:
        nivel_dim8 = "Mejora continua"
        texto_dim8 = "La organización tiene un enfoque riguroso en la gestión de la calidad de los datos. Alentamos a que continúen trabajando en dicha mejora, para asegurar que lod datos sean precisos, relevantes y útiles para la toma de decisiones. Esto puede mejorar significativamente la capacidad de la organización para competir en el mercado y lograr sus objetivos. "

######

     if Reutilizacion_de_datos_int == 0:
        nivel_dim9 = "Cero"
        texto_dim9 = "Una organización gubernamental que no intercambia datos, que no tiene mecanismos definidos para compartirlos y carece de perfiles especializados en la reutilización de los mismos. Es complejo que puedan avanzar. Por lo cual es fundamental establecer políticas, marcos y capacidades para fomentar el intercambio seguro de datos y que puedan ser reutilizados. Además de promover esta cultura de reutilización, buscar colaboraciones externas, puede ayudar a avanzar hacia una gestión de datos más eficiente y efectiva."
        
     if Reutilizacion_de_datos_int > 0 and Reutilizacion_de_datos_int<1:
        nivel_dim9 = "Inicial"
        texto_dim9 = "La organización esta demostrando interes y cuidado al Intercambiar datos y fomentar su reutilización es valioso y puede generar beneficios significativos para el gobierno, las organizaciones y la sociedad. Es importante compartir los datos con áreas internas y usuarios externos a la organización, establecer mecanismos definidos y contar con perfiles profesionales o técnicos especializados en su reutilización. Esto les permitirá aprovechar al máximo su valor, promover la colaboración y la innovación, mejorar la calidad de la información, cumplir con los requisitos normativos y éticos y fomentar una cultura de datos en la organización. "
        
     if Reutilizacion_de_datos_int >= 1 and Reutilizacion_de_datos_int<2:
        nivel_dim9 = "Medio"
        texto_dim9 = "La organización al intercambiar datos y fomentar su reutilización es beneficioso para el gobierno y la sociedad. Es importante que trabajen en compartir los datos con usuarios externos a la organización, establecer mecanismos definidos y contar con perfiles profesionales especializados en su reutilización. Esto permitirá aprovechar al máximo su valor, promover la colaboración y la innovación, mejorar la calidad de la información, cumplir con los requisitos normativos y éticos y fomentar una cultura de datos en la organización. Recomendamos fortalecer estas prácticas a través de estándares abiertos, documentación clara, portales de datos abiertos, licencias adecuadas y colaboración activa, lo que ayudará a maximizar el potencial de los datos compartidos y promover una mayor innovación y transparencia. "
        
     if Reutilizacion_de_datos_int >= 2 and Reutilizacion_de_datos_int<3:
        nivel_dim9 = "Avanzado"
        texto_dim9 = "La organización demuestra un gran avance en el equipo y esto hace a la importancia de contar con profesionales y técnicos especializados en reutilización de datos para impulsar y gestionar de manera efectiva este proceso. Su conocimiento, experiencia en gobernanza, capacidad de análisis, habilidades de comunicación y enfoque innovador son indispensables para generar un beneficio significativo tanto para el gobierno como para la sociedad."
        
     if Reutilizacion_de_datos_int >= 3 and Reutilizacion_de_datos_int<4:
        nivel_dim9 = "Experto"
        texto_dim9 = "La organización tiene mecanismos definidos para que las personas de la organización compartan datos con un propósito determinado es esencial para el buen desempeño de una organización, promueve la transparencia, la colaboración, la toma de decisiones basadas en evidencia, la innovación y el desarrollo de servicios centrados en las personas, y se aprovechan al máximo los datos disponibles. Sería importante acompañar esto con profesionales y técnicos especializados en reutilización de datos que impulsen y gestionen de manera efectiva este proceso. Su conocimiento técnico, experiencia en gobernanza de datos, capacidad de análisis, habilidades de comunicación y enfoque innovador son indispensables para el valor de los datos y generar beneficios significativos tanto para la organización como para la sociedad."
        
     if Reutilizacion_de_datos_int >= 4 and Reutilizacion_de_datos_int<=6:
        nivel_dim9 = "Mejora continua"
        texto_dim9 = "La organización no tan solo tienen definidos los mecanismos para compartir datos con un propósito determinado, sino que cuentan con perfiles profesionales especializados en su reutilización. Esta combinación es altamente valiosa y brinda una base sólida para aprovechar al máximo los datos y promover la innovación y la transparencia. Continuar fortaleciendo estas prácticas y fomentando una cultura de reutilización de datos permitirá aprovechar plenamente el potencial de los datos, mejorar la prestación de servicios y promover la innovación en beneficio de la sociedad. "

######

     if Modelo_de_datos_int == 0:
        nivel_dim10 = "Cero"
        texto_dim10 = "Cuando una organización no cuenta con un modelo de datos bien documentado y recursos especializados en el tema es importante reconocer la necesidad de trabajar en estos aspectos. Priorizar la implementación de un modelo de datos, contratar o capacitar especialistas en el tema, realizar un análisis exhaustivo de los datos existentes, establecer estándares y mejores prácticas y fomentar la colaboración interdepartamental, ayudarán a mejorar la gestión de los datos y sentarán las bases para tomar decisiones informadas y eficientes."
        
     if Modelo_de_datos_int > 0 and Modelo_de_datos_int<1:
        nivel_dim10 = "Inicial"
        texto_dim10 = "La organización al tener este  Inicial, destaca la  necesidad e importancia de tener un modelo de datos definido que garantice la estructura e integridad de los datos. Recomendamos destinar recursos especializados para documentarlo. Estas acciones promueven la gestión efectiva de los datos y respaldan la toma de decisiones basadas en datos confiables. "
        
     if Modelo_de_datos_int >= 1 and Modelo_de_datos_int<2:
        nivel_dim10 = "Medio"
        texto_dim10 = "La organización en este Medio demuestra  la importancia de avanzar para lograr contar con un modelo de datos definido que garantice la estructura, organización e integridad de los datos. Recomendamos destinar recursos especializados para documentarlo. Estas acciones promueven la gestión efectiva de los datos y respaldan la toma de decisiones basadas en datos confiables. "
        
     if Modelo_de_datos_int >= 2 and Modelo_de_datos_int<3:
        nivel_dim10 = "Avanzado"
        texto_dim10 = "La organización demuestra que cuentan con un modelo de datos definido para garantizar la estructura, organización e integridad de los datos. Recomendamos destinar recursos especializados para implementar mejoras en el modelo de datos. Estas acciones fortalecerán la calidad y el valor de los datos de la organización. "
        
     if Modelo_de_datos_int >= 3 and Modelo_de_datos_int<4:
        nivel_dim10 = "Experto"
        texto_dim10 = "La organización en este nivel demuestra un gran compromiso, ya que  contar con un modelo de datos documentado facilita el diseño de sistemas, el mantenimiento y cumplimiento de los requisitos normativos. Recomendamos destinar recursos especializados en modelo de datos para garantizar un enfoque sólido y eficiente en el almacenamiento, acceso y uso de los datos. "
        
     if Modelo_de_datos_int >= 4 and Modelo_de_datos_int<=5:
        nivel_dim10 = "Mejora continua"
        texto_dim10 = "La organización tienen un modelo de datos bien documentado y cuentan con personas especializadas en el tema. Continúen trabajando en el mantenimiento, la colaboración, la promoción de buenas prácticas, la capacitación y el monitoreo, para seguir mejorando y maximizando el valor de su modelo de datos en beneficio de la organización. "

     if Promedio == 0:
         nivel_final = "Cero"
         texto_final = "Indica que la organización, no contempla lo suficiente el valor de los datos  en la toma de decisiones no es suficientemente apreciado y promovido en la organización. Estar en este nivel implica que la organización debe comenzar a tomar en cuenta la buena gestión de los datos para avanzar hacia los siguientes niveles de madurez. "

     if Promedio > 0 and Promedio< 1:
         nivel_final = "Inicial"
         texto_final = "Indica que la organización reconoce que los datos son un activo invaluable para la toma de decisiones. Para seguir creciendo en la madurez de los datos de la organización podría centrarse en aspectos como la calidad de los datos, la gestión de datos, el análisis de datos, la cultura de datos e innovación y mejora continua en la gestión de datos. "

     if Promedio >= 1 and Promedio< 2:
         nivel_final = "Medio"
         texto_final = "Indica que la  organización ha logrado una comprensión adecuada de la importancia de los datos como un activo fundamental. Es importante desarrolladar una conciencia sólida de los datos como un activo clave. Para seguir creciendo en la madurez de los datos en  la organización podría enfocarse en la gestión de datos, gobernanza de datos, calidad e integridad de los datos, el análisis de datos avanzado, impulsar una cultura de datos, un enfoque continuo en la mejorar las prácticas de gestión de datos y un impacto significativo en la toma de decisiones."
         
     if Promedio >= 2 and Promedio< 3:
         nivel_final = "Avanzado"
         texto_final = "Indica que la organización  ha logrado un reconocimiento pleno de la importancia de los datos para el éxito en la toma de decisiones basadas en datos. Para avanzar a un Experto recomendamos centrarse en la innovación en el uso de datos, la integración de datos, contar con lineamientos, procesos documentados para la gestión de riesgos y seguridad de datos. El enfoque en la mejora continua y aprendizaje."  
         
     if Promedio >= 3 and Promedio< 4:
         nivel_final = "Experto"
         texto_final = "Indica que la organización comprende plenamente la importancia de contar con una excelente infraestructura de datos en todos los niveles, que sus equipos están conformados por expertos en la materia y buscan tener  datos de calidad y reconocen que esto le proporciona una ventaja competitiva en la toma de decisiones.Para no descuidar el nivel logrado de madurez la organización debe enfocarse en la gobernanza de datos, la automatización y escalabilidad, la cultura de datos centrada en el valor, la innovación continua y la colaboración con los actores que sean necesarios, formar equipos interdisciplinarios para seguir mejorando sus prácticas de gestión de datos."
         
     if Promedio >= 4 and Promedio< 6:
         nivel_final = "Mejora continua"
         texto_final = "Indica que la organización implementa constantemente mecanismos para la buena gestion de los datos, busca  aprender de las experiencias, auditar y revisar los procesos y compartir las mejores prácticas. Estas acciones demuestran un enfoque constante en la mejora y la optimización de las prácticas de tratamiento de datos, lo que permite a la organización seguir evolucionando y alcanzar niveles más altos de madurez en el futuro"

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