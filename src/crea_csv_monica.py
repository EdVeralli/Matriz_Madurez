import pandas as pd

# $ pip install -U kaleido

#  https://plotly.com/python/radar-chart/


import os
import sys
os.chdir("/home/eduardo/GCBA/Encuesta/")


scores = pd.read_csv('Score_Final.csv',sep=';', encoding='utf-8')

for i in range(len(scores)):
     Area                              = str(scores.iloc[i]['Area'])
     Organismo                         = str(scores.iloc[i]['Organismo'])
     
     print("proceso",Area)


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
        nivel_dim1 = "Nivel cero"
        texto_dim1 = "En el camino de la mejora deberán desarrollar la Integración y recolección de datos para garantizar la consistencia y actualización de la información, poseer una base de datos propia con una tecnología que implemente esta integración y proceder a documentar las políticas de integración lo cual proporciona claridad, transparencia y garantiza el cumplimiento normativo entre otras. Ello les permitirá elaborar estrategias bien planificadas que impactarán en el rendimiento de la organización."

     if Fuente_de_informacion_Integracion_int > 0 and Fuente_de_informacion_Integracion_int<1:
        nivel_dim1 = "Nivel Inicial"
        texto_dim1 = "Al estar en un nivel inicial, la organización debe especializarse en la recopilación de datos. En paralelo, deberán implementar una estrategia de integración y aprovechamiento de la información. Esto implica contar con bases de datos propias para gestionar eficientemente los datos, mejorando su accesibilidad y análisis. Esta práctica le permitirá avanzar en el desarrollo de la integración de los datos."

     if Fuente_de_informacion_Integracion_int >= 1 and Fuente_de_informacion_Integracion_int<2:
        nivel_dim1 = "Nivel Medio"
        texto_dim1 = "Han alcanzado un nivel medio en la gestión de datos. Contar con bases de datos propias colabora a la integración de datos de diferentes fuentes. Tambien impulsa la toma de decisiones informadas y la identificación de patrones en los datos para obtener una ventaja competitiva."
        
     if Fuente_de_informacion_Integracion_int >= 2 and Fuente_de_informacion_Integracion_int<3:
        nivel_dim1 = "Nivel avanzado"
        texto_dim1 = "Han alcanzado el nivel Avanzado. Esto implica una estrategia de integración de datos que maximiza su valor, mejora la toma de decisiones y la eficiencia operativa. Bases de datos propias, gestión responsable y capacidad de integrar datos de múltiples fuentes, brindan ventajas competitivas. Documentar políticas de integración asegura consistencia, cumplimiento normativo, calidad de datos y comunicación efectiva."

     if Fuente_de_informacion_Integracion_int >= 3 and Fuente_de_informacion_Integracion_int<4:
        nivel_dim1 = "Nivel Experto"
        texto_dim1 = "Han alcanzado el nivel experto en la Integración de datos. Su progreso en el tratamiento de datos demuestra un enfoque destacado en la toma de decisiones. Una forma de seguir mejorando es mediante la evaluación constante, la adopción de tecnologías y la capacitación continua para cerrar la brecha hacia la máxima madurez en la gestión de datos."

     if Fuente_de_informacion_Integracion_int >= 4 and Fuente_de_informacion_Integracion_int<=5:
        nivel_dim1 = "Nivel Mejora continua"
        texto_dim1 = "Han alcanzado el nivel de mejora continua, esto refleja el compromiso de la organización con el tratamiento adecuado de los datos como un activo de valor. Se recomienda continuar trabajando en este camino para el logro de niveles aún más avanzados de madurez en la gestión de datos."



######

     if Ciencia_de_datos_int == 0:
        nivel_dim2 = "Nivel cero"
        texto_dim2 = "La ciencia de datos puede ser beneficiosa en muchos aspectos y su impacto en la toma de decisiones informadas es un atributo a considerar. Es importante que puedan identificar las oportunidades de mejora que se pueden alcanzar a partir de la implementación de capacidades en este tema."
        
     if Ciencia_de_datos_int > 0 and Ciencia_de_datos_int<1:
        nivel_dim2 = "Nivel Inicial"
        texto_dim2 = "Alcanzaron el nivel Inicial: El nivel Inicial es un paso importante para reconocer la importancia de la Ciencia de Datos. Sin embargo, sumar el desarrollo y entrenamiento de modelos de aprendizaje automático, análisis predictivo y su documentación fortalecerá la capacidad del organismo para tomar decisiones informadas y aprovechar al máximo el potencial de los datos disponibles."
        
     if Ciencia_de_datos_int >= 1 and Ciencia_de_datos_int<2:
        nivel_dim2 = "Nivel Medio"
        texto_dim2 = "Alcanzaron el nivel medio con un área dedicada a la ciencia de datos y aplicación de técnicas estadísticas, modelos de aprendizaje automático y análisis predictivo. También es crucial documentar los proyectos para garantizar replicabilidad, transferencia de conocimientos, cumplimiento normativo y mejora continua. Un proceso sistemático de documentación respalda el éxito y la transparencia de los proyectos de ciencia de datos."
        
     if Ciencia_de_datos_int >= 2 and Ciencia_de_datos_int<3:
        nivel_dim2 = "Nivel avanzado"
        texto_dim2 = "Alcanzaron el nivel avanzado en ciencias de datos. Recomendamos que continúen invirtiendo en habilidades técnicas, actualizándose en tendencias y colaborando con expertos externos para maximizar el valor de los datos para la toma de decisiones. Continúen construyendo sobre este pilar para lograr niveles más avanzados de madurez."
        
     if Ciencia_de_datos_int >= 3 and Ciencia_de_datos_int<4:
        nivel_dim2 = "Nivel Experto"
        texto_dim2 = "Alcanzaron el nivel experto en Ciencias de Datos. Este logro demuestra madurez y prácticas avanzadas en el tratamiento de datos. Recomendamos que continúen invirtiendo en capacitación, colaboración externa y seguimiento de avances para maximizar el valor de los datos para la toma de decisiones más eficientes para la organización."
        
     if Ciencia_de_datos_int >= 4 and Ciencia_de_datos_int<=5:
        nivel_dim2 = "Nivel Mejora continua"
        texto_dim2 = "Alcanzaron el nivel máximo de madurez mejora continua en Ciencias de Datos. Su dedicación y prácticas avanzadas en el tratamiento de los datos demuestran un grado muy avanzado de madurez. Recomendamos que continúen actualizándose y explorando nuevas aplicaciones para impulsar la innovación basada en datos."
        

######

     if Actualidad_de_Reportes_productos_int == 0:
        nivel_dim3 = "Nivel cero"
        texto_dim3 = "Nivel 0: Disponer de reportes actualizados es fundamental para garantizar la transparencia, la rendición de cuentas, la toma de decisiones informadas, la evaluación, así como la comunicación interna y externa efectiva. Es recomendable que se diseñe un sistema que contenga un componente para la generación y la publicación de reportes de forma regular, que reflejen sus actividades, resultados e impacto."
        
     if Actualidad_de_Reportes_productos_int > 0 and Actualidad_de_Reportes_productos_int<1:
        nivel_dim3 = "Nivel Inicial"
        texto_dim3 = "En el nivel Inicial se dispone de reportes de datos, pero es importante actualizarlos automatizadamente y con mayor frecuencia. Recopilar la opinión de los usuarios y ajustar los procesos de actualización mejora la toma de decisiones y la comunicación en la organización."
        
     if Actualidad_de_Reportes_productos_int >= 1 and Actualidad_de_Reportes_productos_int<2:
        nivel_dim3 = "Nivel Medio"
        texto_dim3 = "En el nivel medio, se generan reportes de datos actualizados regularmente pero se recomienda su automatización. Es esencial trabajar con las devoluciones de los usuarios para ajustar los procesos de actualización en función de sus experiencias de uso. Los informes precisos y accesibles son fundamentales para la toma de decisiones y la comunicación efectiva."
        
     if Actualidad_de_Reportes_productos_int >= 2 and Actualidad_de_Reportes_productos_int<3:
        nivel_dim3 = "Nivel avanzado"
        texto_dim3 = "En el nivel avanzado se generan reportes de datos actualizados y automatizados con frecuencia. Es recomendable recopilar la opinión de los usuarios y realizar ajustes en los procesos de actualización según sus comentarios. La retroalimentación de los usuarios es fundamental para mejorar los informes y demostrar que sus opiniones son valoradas."
        
     if Actualidad_de_Reportes_productos_int >= 3 and Actualidad_de_Reportes_productos_int<4:
        nivel_dim3 = "Nivel Experto"
        texto_dim3 = "Alcanzaron el nivel experto en la dimensión de Actualidad de Reportes y/o Productos. Este logro demuestra un alto grado de madurez en el tratamiento de los datos para generar reportes y productos actualizados. Han demostrado habilidades sólidas y conocimientos en la generación de reportes y productos basados en datos, estableciendo procesos eficientes. Para continuar avanzando es importante reconocer el progreso y la madurez obtenidos. Recomendamos que continúen evaluando y mejorando continuamente sus procesos, aprovechando las últimas tendencias y tecnologías en la generación de reportes y productos basados en datos."
        
     if Actualidad_de_Reportes_productos_int >= 4 and Actualidad_de_Reportes_productos_int<=5:
        nivel_dim3 = "Nivel Mejora continua"
        texto_dim3 = "Alcanzaron el nivel más alto de madurez mejora continua. Su madurez en el tratamiento de datos, generación de reportes relevantes y establecimiento de procesos sólidos reflejan un enfoque destacado en la toma de decisiones. Recomendamos que continúen en este camino mejorando y compartiendo mejores prácticas para impulsar la cultura de mejora continua."
        
######

     if Disponibilizacion_int == 0:
        nivel_dim4 = "Nivel cero"
        texto_dim4 = "Los datos deberían estar disponibles para tomar decisiones informadas y realizar análisis. La disponibilidad de datos también debe estar en línea con las políticas de privacidad y seguridad de la información."
        
     if Disponibilizacion_int > 0 and Disponibilizacion_int<1:
        nivel_dim4 = "Nivel Inicial"
        texto_dim4 = "Están en nivel inicial, es importante asegurarse de tener los datos disponibles con regularidad y en formatos estándar abiertos como CSV, JSON, XML, KML, GEOJSON. Además, es importante desarrollar APIs para permitir el acceso externo y utilizar un lenguaje adecuado según la audiencia (demográfica, tributaria, etc.). Es fundamental que los datos estén disponibles para tomar decisiones informadas y realizar análisis pero también protegidos mediante políticas de seguridad de la información."
        
     if Disponibilizacion_int >= 1 and Disponibilizacion_int<2:
        nivel_dim4 = "Nivel Medio"
        texto_dim4 = "En el nivel medio los datos están disponibles. Es importante avanzar en formatos estándar abiertos como CSV, JSON, XML, KML, GEOJSON y desarrollar APIs para permitir el acceso externo y utilizar un lenguaje adecuado según la audiencia (demográfica, tributaria, etc.). Es fundamental que los datos estén disponibles para tomar decisiones informadas y realizar análisis pero también protegidos mediante políticas de seguridad de la información."
        
     if Disponibilizacion_int >= 2 and Disponibilizacion_int<3:
        nivel_dim4 = "Nivel avanzado"
        texto_dim4 = "Han alcanzado el nivel avanzado. Actualmente tienen disponibles los datos y utilizan algunos de los formatos estándares abiertos más conocidos para leerlos sin embargo sería importante disponer de API´s para que los usuarios externos puedan acceder a los datos. Asimismo, es importante difundir y utilizar el lenguaje adecuado para las distintas audiencias, en función de los datos y de lo que se produce con ellos (información demográfica, información tributaria, etc). Los datos deben estar disponibles oportunamente para tomar decisiones informadas y realizar análisis pero también deberían estar protegidos por políticas y procedimientos de seguridad de la información."
        
     if Disponibilizacion_int >= 3 and Disponibilizacion_int<4:
        nivel_dim4 = "Nivel Experto"
        texto_dim4 = "En el nivel experto los datos están disponibles pero es importante utilizar formatos estándar abiertos (CSV, JSON, XML, KML, GEOJSON) y desarrollar APIs para el acceso externo. Difundir y utilizar el lenguaje adecuado para diferentes audiencias (demográfica, tributaria, etc.) es esencial. Los datos deben estar disponibles para la toma decisiones informadas y análisis pero también deben estar protegidos con políticas y procedimientos de seguridad de la información."
        
     if Disponibilizacion_int >= 4 and Disponibilizacion_int<=5:
        nivel_dim4 = "Nivel Mejora continua"
        texto_dim4 = "Ha alcanzado el nivel mejora continua. Es una excelente práctica para la disponibilidad y transparencia de los datos. Tener los datos disponibles de forma permanente y en formatos abiertos mejora el acceso para usuarios externos y fomenta su reutilización."
        
######

     if Proteccion_de_datos_int == 0:
        nivel_dim5 = "Nivel cero"
        texto_dim5 = "Es importante conocer ambas normativas y asegurarse de cumplir con las obligaciones legales establecidas en cada una de ellas. Esto puede evitar posibles sanciones y multas por incumplimiento de las leyes de protección de datos y también ayuda a proteger la privacidad y seguridad de los datos personales de los titulares de los mismos."
        
     if Proteccion_de_datos_int > 0 and Proteccion_de_datos_int<1:
        nivel_dim5 = "Nivel Inicial"
        texto_dim5 = "En el nivel inicial es importante conocer y cumplir con las normativas legales para evitar sanciones y proteger la privacidad de los datos personales. Además, es importante establecer los límites de tiempo aceptables para la permanencia de los datos en los sistemas y evitar de esta forma riesgos innecesarios para la seguridad y privacidad de los titulares de los datos."
        
     if Proteccion_de_datos_int >= 1 and Proteccion_de_datos_int<2:
        nivel_dim5 = "Nivel Medio"
        texto_dim5 = "El nivel medio cumple con las obligaciones legales y cumple los tiempos adecuados en que deben permanecer los datos personales en los sistemas. La clasificación de datos sensibles y el consentimiento informado son considerados. Para mejorar, se sugiere implementar mecanismos de minimización o destrucción periódica de datos, establecer espacios de diálogo y comités para abordar temas de protección de datos. Asimismo, disponer de lineamientos definidos para garantizar la privacidad, seguridad y cumplimiento normativo."
        
     if Proteccion_de_datos_int >= 2 and Proteccion_de_datos_int<3:
        nivel_dim5 = "Nivel avanzado"
        texto_dim5 = "En el nivel avanzado, la organización cumple con las obligaciones legales, permanencia de los datos en los sistemas, clasificación y minimización. Para fortalecer aún más la protección de datos se recomienda generar espacios de diálogo, establecer lineamientos claros de protección de datos y actualizarlos regularmente para reflejar cambios normativos. Esto garantizará una mayor adhesión y fortaleza en la protección de datos."
        
     if Proteccion_de_datos_int >= 3 and Proteccion_de_datos_int<4:
        nivel_dim5 = "Nivel Experto"
        texto_dim5 = "En el nivel experto, la organización cumple con las obligaciones legales, permanencia de datos en los sistemas, clasificación y consentimiento. Se destaca la importancia de contar con lineamientos de protección de datos definidos, comunicados y actualizados periódicamente. Esto fortalecerá la protección de datos, promoverá la cultura de cumplimiento y seguridad en toda la organización."
        
     if Proteccion_de_datos_int >= 4 and Proteccion_de_datos_int<=5:
        nivel_dim5 = "Nivel Mejora continua"
        texto_dim5 = "En el nivel mejora continua la organización ha implementado prácticas sólidas de protección de datos y cuenta con lineamientos definidos. Esto garantiza un tratamiento coherente de los datos y cumplimiento normativo además de promover una cultura de responsabilidad. Se recomienda seguir fortaleciendo el enfoque mediante capacitación, evaluación continua y medidas adicionales según sea necesario para garantizar la protección y confianza en la privacidad de la información."

######

     if Gobernanza_de_datos_int == 0:
        nivel_dim6 = "Nivel cero"
        texto_dim6 = "Es importante conocer los roles de cada integrante de la organización respecto de los datos. Es recomendable que estén bien definidos y relevados ya que esto ayuda a garantizar la seguridad y privacidad de los datos personales y a asegurar el cumplimiento de las regulaciones y leyes aplicables. Contar con roles bien definidos facilita la asignación de responsabilidades específicas a los agentes de la organización e impulsa el sostenimiento de una estructura de gobernanza para la gestión de los datos personales."
        
     if Gobernanza_de_datos_int > 0 and Gobernanza_de_datos_int<1:
        nivel_dim6 = "Nivel Inicial"
        texto_dim6 = "En el nivel inicial es importante establecer políticas sobre el uso y acceso de los datos, garantizando la privacidad y seguridad de la información. Documentar el ciclo de vida de los datos y capacitar al personal en gobernanza de datos son acciones recomendadas para cumplir con las regulaciones y mejorar la eficiencia del trabajo."
        
     if Gobernanza_de_datos_int >= 1 and Gobernanza_de_datos_int<2:
        nivel_dim6 = "Nivel Medio"
        texto_dim6 = "En el nivel medio es importante contar con políticas que garanticen el uso ético y responsable de los datos personales, para la protección de la privacidad y los derechos de las personas. Documentar el ciclo de vida de los datos y capacitar al personal en gobernanza de datos son medidas adicionales recomendadas para cumplir con las regulaciones y mejorar la eficiencia en el manejo de los datos."
        
     if Gobernanza_de_datos_int >= 2 and Gobernanza_de_datos_int<3:
        nivel_dim6 = "Nivel avanzado"
        texto_dim6 = "Alcanzaron un nivel avanzado de madurez en datos. Es deseable documentar las etapas del ciclo de vida de los datos. Las capacitaciones en gobernanza de datos, en especial sobre clasificación y roles, son fundamentales para garantizar la privacidad y seguridad de los datos, proteger los derechos de las personas y cumplir con las regulaciones, mejorando la eficiencia de los agentes."
        
     if Gobernanza_de_datos_int >= 3 and Gobernanza_de_datos_int<4:
        nivel_dim6 = "Nivel Experto"
        texto_dim6 = "Alcanzaron un nivel experto de madurez en datos. Es recomendable documentar las etapas del ciclo de vida de los datos. Sugerimos contar con lineamientos implementados ya que redunda en una gestión eficiente y segura de los datos y la tecnología asociada a los procesos. Los lineamientos proporcionan coherencia, estandarización, reducen el riesgo y la incertidumbre, promueven la transparencia y la responsabilidad, además de aumentar la eficiencia y la productividad en toda la organización. Las capacitaciones en gobernanza de datos, en especial sobre clasificación y roles, son fundamentales para garantizar la privacidad y seguridad de los datos, proteger los derechos de las personas y cumplir con las regulaciones, mejorando la eficiencia del personal."
        
     if Gobernanza_de_datos_int >= 4 and Gobernanza_de_datos_int<=5:
        nivel_dim6 = "Nivel Mejora continua"
        texto_dim6 = "Alcanzaron el nivel mejora continua de madurez en datos. Esto implica que la organización tomó medidas significativas en la gobernanza de datos. Mantener un enfoque proactivo y fortalecer aspectos clave ayudará a maximizar el valor de los datos, garantizar el cumplimiento normativo y la confianza de los stakeholders."

######

     if Gestion_de_acceso_a_datos_int == 0:
        nivel_dim7 = "Nivel cero"
        texto_dim7 = "Es fundamental establecer políticas claras, implementar sistemas y mecanismos de gestión de acceso a datos, capacitar al personal, garantizar la seguridad y privacidad de los datos además de cumplir con las regulaciones aplicables. Estas acciones ayudarán a mejorar la transparencia, la seguridad y la gestión adecuada de los datos en la institución."
        
     if Gestion_de_acceso_a_datos_int > 0 and Gestion_de_acceso_a_datos_int<1:
        nivel_dim7 = "Nivel Inicial"
        texto_dim7 = "Alcanzaron el nivel inicial de madurez en datos. Tener implementado un sistema o una política de acceso a la información es fundamental para promover la transparencia, responsabilidad, eficiencia y protección de datos en una organización. Es importante destacar que la elección del sistema de acceso a la información dependerá del nivel de seguridad que se requiere para proteger la información. Recomendamos contar con reportes de acceso a datos ya que constituyen una importante herramienta para monitorear y mejorar la seguridad de la información en una organización y para cumplir con las regulaciones y normativas de seguridad de la información."
        
     if Gestion_de_acceso_a_datos_int >= 1 and Gestion_de_acceso_a_datos_int<2:
        nivel_dim7 = "Nivel Medio"
        texto_dim7 = "Alcanzaron un nivel medio de madurez en datos.Contar con reportes de acceso a los datos es un buen comienzo para monitorear y registrar las actividades relacionadas con el acceso a la información. Sin embargo, es importante destacar que tener un sistema de acceso a la información implementado un control efectivo y seguro sobre quién tiene acceso a los datos y en qué circunstancias. Implementar un sistema de acceso a la información robusto y seguro fortalecerá la protección de los datos y reducirá los riesgos de acceso no autorizado. Además, facilitará la administración y el monitoreo de los accesos, lo que resultará en una mayor eficiencia y cumplimiento normativo."
        
     if Gestion_de_acceso_a_datos_int >= 2 and Gestion_de_acceso_a_datos_int<3:
        nivel_dim7 = "Nivel avanzado"
        texto_dim7 = "Alcanzaron un nivel avanzado de madurez en datos. La organización implementa reportes de acceso a los datos y sistemas de acceso a la información. Estas medidas son fundamentales para garantizar la transparencia y la rendición de cuentas en el manejo de los datos.Continuar fortaleciendo estas prácticas a través de políticas claras, seguridad de datos, evaluaciones periódicas y capacitación adecuada ayudará a promover la transparencia, la seguridad y la confianza en la institución."
        
     if Gestion_de_acceso_a_datos_int >= 3 and Gestion_de_acceso_a_datos_int<4:
        nivel_dim7 = "Nivel Experto"
        texto_dim7 = "Alcanzaron un nivel experto de madurez en datos. Este logro demuestra un alto grado de madurez y excelencia en la gestión del acceso a los datos. implementaron prácticas sólidas y avanzadas para garantizar la seguridad y el acceso adecuado a la información. En pos de alcanzar el nivel máximo recomendamos seguir mejorando las políticas y controles de acceso, actualizándose en las mejores prácticas y tecnologías."
        
     if Gestion_de_acceso_a_datos_int >= 4 and Gestion_de_acceso_a_datos_int<=5:
        nivel_dim7 = "Nivel Mejora continua"
        texto_dim7 = "Alcanzaron el nivel más alto de madurez en datos denominado mejora continua. Este logro demuestra una madurez y excelencia destacadas en el tratamiento y acceso seguro de los datos. Implementaron prácticas sólidas y avanzadas, estableciendo políticas y controles eficientes para proteger y garantizar el acceso adecuado a los datos. Es importante mantener esta forma de trabajo, evaluando y actualizando políticas y controles. Recomendamos que sigan actualizándose con las últimas tendencias y tecnologías en seguridad de datos y promoviendo la capacitación y lineamientos sobre la protección de datos en toda la organización. Recomendamos que en sus experiencias con otras áreas fomenten una cultura de seguridad de datos y colaboración en la gestión del acceso a los datos."

######

     if Calidad_de_los_datos_int == 0:
        nivel_dim8 = "Nivel cero"
        texto_dim8 = "Recomendamos realizar controles periódicos en la calidad de los datos. Es importante implementar estos controles con una periodicidad adecuada. Esto implica establecer procesos y procedimientos claros para llevar a cabo estas revisiones, asignar responsabilidades y recursos y utilizar herramientas o técnicas adecuadas para realizar las verificaciones necesarias. A partir de ello la organización mejorará la calidad de sus datos, fortalecerá su toma de decisiones y cumplirá con los estándares de calidad requeridos."
        
     if Calidad_de_los_datos_int > 0 and Calidad_de_los_datos_int<1:
        nivel_dim8 = "Nivel Inicial"
        texto_dim8 = "Alcanzaron un nivel inicial de madurez en datos. Tienen identificadas las diferentes dimensiones de los datos y es importante que avancen en implementar controles de calidad de los datos e identificar las métricas de calidad que analizan esos controles. Por otro lado, documentar los procesos y procedimientos que analicen el grado de cumplimiento de las dimensiones definidas y perfiles profesionales/técnicos dedicados a evaluar periódicamente las métricas de calidad."
        
     if Calidad_de_los_datos_int >= 1 and Calidad_de_los_datos_int<2:
        nivel_dim8 = "Nivel Medio"
        texto_dim8 = "Alcanzaron un nivel medio en madurez en datos, esto contribuye a generar confianza y eficiencia dentro de la organización. Para mejorar es necesario definir métricas, documentar procesos y asignar recursos especializados que se dediquen a garantizar la precisión y el cumplimiento de los requisitos normativos y las expectativas de los usuarios."
        
     if Calidad_de_los_datos_int >= 2 and Calidad_de_los_datos_int<3:
        nivel_dim8 = "Nivel avanzado"
        texto_dim8 = "Alcanzaron un nivel avanzado de madurez en datos. Realizar controles de revisión y usar métricas sólidas son fundamentales para evaluar y mejorar la calidad de los datos. Recomendamos que en paralelo documenten los procesos y procedimientos y destinen a esta tarea perfiles profesionales/técnicos que aseguren la consistencia y la mejora continua."
        
     if Calidad_de_los_datos_int >= 3 and Calidad_de_los_datos_int<4:
        nivel_dim8 = "Nivel Experto"
        texto_dim8 = "Alcanzaron un nivel experto de madurez en datos. Para continuar realizando mejoras es importante incorporar perfiles profesionales o técnicos dedicados a evaluar periódicamente las métricas de calidad. Estos expertos aportarán conocimientos especializados, garantizarán un monitoreo constante, establecerán responsabilidad y rendición de cuentas, fortaleciendo así la toma de decisiones informadas y confiables basadas en datos de alta calidad."
        
     if Calidad_de_los_datos_int >= 4 and Calidad_de_los_datos_int<=5:
        nivel_dim8 = "Nivel Mejora continua"
        texto_dim8 = "Alcanzaron un nivel de mejora continua en madurez en datos. La organización tiene un enfoque riguroso en la gestión de la calidad de los datos. Recomendamos que continúen trabajando en la mejora de la calidad de los datos para asegurar que sean precisos, relevantes y útiles para la toma de decisiones. Esto puede mejorar significativamente la capacidad de la organización para competir en el mercado y lograr sus objetivos"

######

     if Reutilizacion_de_datos_int == 0:
        nivel_dim9 = "Nivel cero"
        texto_dim9 = "Una organización gubernamental que no intercambia datos no tiene mecanismos definidos para compartirlos y carece de perfiles especializados en la reutilización de los mismos. Es fundamental darle valor a que puedan ser reutilizados y establecer políticas, marcos y capacidades para fomentar el intercambio seguro de datos. Además, promover una cultura de reutilización de datos y buscar colaboraciones externas pueden ayudar a avanzar hacia una gestión de datos más eficiente y efectiva."
        
     if Reutilizacion_de_datos_int > 0 and Reutilizacion_de_datos_int<1:
        nivel_dim9 = "Nivel Inicial"
        texto_dim9 = "Alcanzaron el nivel inicial en madurez en datos. Intercambiar datos y fomentar su reutilización es valioso y puede generar beneficios significativos para el gobierno y la sociedad civil. Es importante compartir los datos con áreas internas y usuarios externos a la organización, establecer mecanismos definidos y contar con perfiles profesionales o técnicos especializados en la reutilización de datos. Esto les permitirá aprovechar al máximo el valor de los datos, promover la colaboración y la innovación, mejorar la calidad de la información, cumplir con los requisitos normativos y éticos y fomentar una cultura de datos en la organización."
        
     if Reutilizacion_de_datos_int >= 1 and Reutilizacion_de_datos_int<2:
        nivel_dim9 = "Nivel Medio"
        texto_dim9 = "Alcanzaron el nivel medio de madurez en datos. Intercambiar datos y fomentar su reutilización es valioso y puede generar beneficios significativos para la organización gubernamental y la sociedad civil. Es importante que trabajen en compartir los datos con usuarios externos a la organización, establecer mecanismos definidos y contar con perfiles profesionales especializados en la reutilización de datos. Esto permitirá aprovechar al máximo el valor de los datos, promover la colaboración y la innovación, mejorar la calidad de la información, cumplir con los requisitos normativos y éticos y fomentar una cultura de datos en la organización. Recomendamos fortalecer estas prácticas a través de estándares abiertos, documentación clara, portales de datos abiertos, licencias adecuadas y colaboración activa. Estos elementos ayudarán a maximizar el potencial de los datos compartidos y promover una mayor innovación y transparencia."
        
     if Reutilizacion_de_datos_int >= 2 and Reutilizacion_de_datos_int<3:
        nivel_dim9 = "Nivel avanzado"
        texto_dim9 = "Alcanzaron un nivel avanzado de madurez en datos. Es importante contar con profesionales y técnicos especializados en reutilización de datos para impulsar y gestionar de manera efectiva este proceso. Su conocimiento técnico, experiencia en gobernanza de datos, capacidad de análisis, habilidades de comunicación y enfoque innovador son indispensables para generar un beneficio significativo tanto para el gobierno como para la sociedad civil."
        
     if Reutilizacion_de_datos_int >= 3 and Reutilizacion_de_datos_int<4:
        nivel_dim9 = "Nivel Experto"
        texto_dim9 = "Sería importante acompañar esto con profesionales y técnicos especializados en reutilización de datos que impulsen y gestionen de manera efectiva este proceso. Su conocimiento técnico, experiencia en gobernanza de datos, capacidad de análisis, habilidades de comunicación y enfoque innovador son indispensables para el valor de los datos y generar beneficios significativos tanto para la organización como para la sociedad civil."
        
     if Reutilizacion_de_datos_int >= 4 and Reutilizacion_de_datos_int<=5:
        nivel_dim9 = "Nivel Mejora continua"
        texto_dim9 = "Alcanzaron el nivel Mejora Continua. Tienen definidos los mecanismos para compartir datos con un propósito determinado y cuentan con perfiles profesionales especializados en su reutilización. Esta combinación es altamente valiosa y brinda una base sólida para aprovechar al máximo los datos y promover la innovación y la transparencia. Continuar fortaleciendo estas prácticas y fomentando una cultura de reutilización de datos permitirá aprovechar plenamente el potencial de los datos, mejorar la prestación de servicios y promover la innovación en beneficio de la sociedad civil."

######

     if Modelo_de_datos_int == 0:
        nivel_dim10 = "Nivel cero"
        texto_dim10 = "Cuando una organización no cuenta con un modelo de datos bien documentado y recursos especializados en el tema es importante reconocer la necesidad de trabajar en estos aspectos. Priorizar la implementación de un modelo de datos, contratar o capacitar especialistas en el tema, realizar un análisis exhaustivo de los datos existentes, establecer estándares y mejores prácticas y fomentar la colaboración interdepartamental. Estos pasos ayudarán a mejorar la gestión de los datos y sentarán las bases para tomar decisiones informadas y eficientes en la organización."
        
     if Modelo_de_datos_int > 0 and Modelo_de_datos_int<1:
        nivel_dim10 = "Nivel Inicial"
        texto_dim10 = "En el nivel inicial se destaca la importancia de tener un modelo de datos definido que garantice la estructura e integridad de los datos. Recomendamos destinar recursos especializados para documentar el modelo de datos definido. Estas acciones promueven la gestión efectiva de los datos y respaldan la toma de decisiones basadas en datos confiables."
        
     if Modelo_de_datos_int >= 1 and Modelo_de_datos_int<2:
        nivel_dim10 = "Nivel Medio"
        texto_dim10 = "En el nivel medio se destaca la importancia de contar con un modelo de datos definido que garantice la estructura, organización e integridad de los datos. Recomendamos destinar recursos especializados para documentar el modelo de datos. Estas acciones promueven la gestión efectiva de los datos y respaldan la toma de decisiones basadas en datos confiables."
        
     if Modelo_de_datos_int >= 2 and Modelo_de_datos_int<3:
        nivel_dim10 = "Nivel avanzado"
        texto_dim10 = "Se destaca la importancia de contar con un modelo de datos definido para garantizar la estructura, organización e integridad de los datos. Recomendamos destinar recursos especializados para implementar mejoras en el modelo de datos. Estas acciones fortalecerán la calidad y el valor de los datos de la organización."
        
     if Modelo_de_datos_int >= 3 and Modelo_de_datos_int<4:
        nivel_dim10 = "Nivel Experto"
        texto_dim10 = "En el nivel experto de madurez en datos, contar con un modelo de datos documentado facilita el diseño de sistemas, el mantenimiento y cumplimiento de los requisitos normativos. Recomendamos destinar recursos especializados en modelo de datos para garantizar un enfoque sólido y eficiente en el almacenamiento, acceso y uso de los datos."
        
     if Modelo_de_datos_int >= 4 and Modelo_de_datos_int<=5:
        nivel_dim10 = "Nivel Mejora continua"
        texto_dim10 = "Ha alcanzado el nivel mejora continua. Tienen un modelo de datos bien documentado y cuentan con personas especializadas en el tema. Continúen en este camino, trabajando en el mantenimiento, la colaboración, la promoción de buenas prácticas, la capacitación y el monitoreo para seguir mejorando y maximizando el valor de su modelo de datos en beneficio de la organización."

     if Promedio == 0:
         nivel_final = "Nivel cero"
         texto_final = "El valor de los datos en la toma de decisiones no es suficientemente apreciado y promovido en la organización. Estar en este nivel implica que la organización debe comenzar a tomar en cuanta la buena gestión de los datos para avanzar hacia los siguientes niveles de madurez. "

     if Promedio > 0 and Promedio< 1:
         nivel_final = "Nivel Inicial"
         texto_final = "La organización reconoce que los datos son un activo invaluable para la toma de decisiones. Para avanzar en los demás niveles de madurez, la organización podría centrarse en aspectos como la calidad de los datos, la gestión de datos, el análisis de datos, la cultura de datos e innovación y mejora continua en la gestión de datos."

     if Promedio >= 1 and Promedio< 2:
         nivel_final = "Nivel Medio"
         texto_final = "Indica que la organización ha logrado una comprensión adecuada de la importancia de los datos como un activo fundamental. Existe una conciencia respecto del valor estratégico de los datos y se reconoce que su adecuada manipulación puede tener un impacto significativo en la toma de decisiones. En el nivel Medio de madurez la organización ha desarrollado una conciencia sólida de la importancia de los datos como un activo clave. Para avanzar hacia los demás niveles de madurez la organización podría enfocarse en la gestión de datos, gobernanza de datos, calidad e integridad de los datos, el análisis de datos avanzado, impulsar una cultura de datos y enfoque continuo en la mejorar las prácticas de gestión de datos."
         
     if Promedio >= 2 and Promedio< 3:
         nivel_final = "Nivel avanzado"
         texto_final = "Indica que la organización ha logrado un reconocimiento pleno de la importancia de los datos para el éxito organizacional en la toma de desiciones basadas en datos. Para lograr un nivel experto recomendamos centrarse en la innovación en el uso de datos, la integración de datos, contar con lineamientos, procesos documentados para la gestión de riesgos y seguridad de datos. El enfoque en la mejora continua y aprendizaje."  
         
     if Promedio >= 3 and Promedio< 4:
         nivel_final = "Nivel Experto"
         texto_final = "En este nivel indica que la organización comprende plenamente la importancia de contar con una excelente infraestructura de datos en todos los niveles, que sus equipos están conformados por expertos en la materia y buscan tener datos de calidad y reconocen que esto le proporciona una ventaja competitiva en la toma de decisiones. Para no descuidar el nivel logrado de madurez la organización debe enfocarse en la gobernanza de datos, la automatización y escalabilidad, la cultura de datos centrada en el valor, la innovación continua y la colaboración con los actores que sean necesarios, formar equipos interdisciplinarios para seguir mejorando sus prácticas de gestión de datos."
         
     if Promedio >= 4 and Promedio< 6:
         nivel_final = "Nivel Mejora continua"
         texto_final = "Indica que la organización implementa constantemente mecanismos para la buena gestion de los datos, busca aprender de las experiencias, auditar y revisar los procesos y compartir las mejores prácticas. Estas acciones demuestran un enfoque constante en la mejora y la optimización de las prácticas de tratamiento de datos, lo que permite a la organización seguir evolucionando y alcanzar niveles más altos de madurez en el futuro."
         
p = open("textos_monica.csv", "w")
titulo = 'Nivel 1'+";"+"Texto Nivel 1"+";"+'Nivel 2'+";"+"Texto Nivel 2"+";"+'Nivel 3'+";"+"Texto Nivel 3"+";"+'Nivel 4'+";"+"Texto Nivel 4"+";"+'Nivel 5'+";"+"Texto Nivel 5"+";"+'Nivel 6'+";"+"Texto Nivel 6"+";"+'Nivel 7'+";"+"Texto Nivel 7"+";"+'Nivel 8'+";"+"Texto Nivel 8"+";"+'Nivel 9'+";"+"Texto Nivel 9"+";"+'Nivel 10'+";"+"Texto Nivel 10"+"\n"
p.write(titulo)
p.write(nivel_dim1+";"+texto_dim1+";"+nivel_dim2+";"+texto_dim2+";"+nivel_dim3+";"+texto_dim3+";"+nivel_dim4+";"+texto_dim4+";"+nivel_dim5+";"+texto_dim5+";"+nivel_dim6+";"+texto_dim6+";"+nivel_dim7+";"+texto_dim7+";"+nivel_dim8+";"+texto_dim8+";"+nivel_dim9+";"+texto_dim9+";"+nivel_dim10+";"+texto_dim10+";"+"\n")
p.write(";"+"\n")
p.write(";"+"\n")
p.write(";"+"\n")
p.write("Valores Finales ;"+"\n")

p.write(nivel_final+";"+texto_final+"\n")
p.close()