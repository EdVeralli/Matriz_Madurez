import csv
import os
import sys
import pandas as pd
from os import system
import time


from dotenv import load_dotenv
import os

# from dotenv import dotenv_values
# load_dotenv()
# ultimo_proceso = os.getenv('FECHA')

os.chdir("/home/eduardo/GCBA/Encuesta/Matriz_Madurez/data/")

colnames = ['fecha','score','nombre_apellido','pertenece_gcba' ,'mail','cargo','secre_subse_area','p1_recop_dat','p2_bases_dat','p3_control_base','p4_integr_dat','p5_tec_integr_dat','p6_documen_pol_int','p7_area_cienc_dat','p8_apli_tec_ciencia_dat','p9_herra_vis_dat','p10_apli_pred','p11_documen_proy_cie_dat','p12_tien_report','p13_act_report','p14_forma_act_report','p15_disp_dat','p16_lect_dat_stand','p17_api_dat','p18_norm_prot_dat','p19_tiemp_dat','p20_clasif_dat_sens','p21_dat_sens_consent','p22_destr_minim_dat','p23_espac_disc_prot_dat','p24_lineam_pro_dat','p25_roles_dat','p26_polit_uso_dat','p27_documen_cic_v_dat','p28_capac_pers_gobern_dat','p29_report_acc_dat','p30_sist_acc_info','p31_revis_cal_dat','p32_metr_cal_dat','p33_proc_cal_dat','p34_per_espec_cal_dat','p35_interc_dat','p36_mecan_prop_comp_dat','p37_pers_espec_reut_dat','p38_model_dat','p39_grad_documen_dat','p40_documen_mod_dat','p41_pers_espec_model_dat','sugerencias']
varnames = ['varpunkt_p1','varpunkt_p2','varpunkt_p3','varpunkt_p4','varpunkt_p5','varpunkt_p6','varpunkt_p7','varpunkt_p8','varpunkt_p9','varpunkt_p10','varpunkt_p11','varpunkt_p12','varpunkt_p13','varpunkt_p14','varpunkt_p15','varpunkt_p16','varpunkt_p17','varpunkt_p18','varpunkt_p19','varpunkt_p20','varpunkt_p21','varpunkt_p22','varpunkt_p23','varpunkt_p24','varpunkt_p25','varpunkt_p26','varpunkt_p27','varpunkt_p28','varpunkt_p29','varpunkt_p30','varpunkt_p31','varpunkt_p32__1','varpunkt_p32__2','varpunkt_p32__3','varpunkt_p32__4','varpunkt_p32__5','varpunkt_p32__6','varpunkt_p32__7','varpunkt_p32__8','varpunkt_p32__9','varpunkt_p32__10','varpunkt_p33','varpunkt_p34','varpunkt_p35','varpunkt_p36','varpunkt_p37','varpunkt_p38','varpunkt_p39','varpunkt_p40__1','varpunkt_p40__2','varpunkt_p40__3','varpunkt_p40__4','varpunkt_p40__5','varpunkt_p40__6','varpunkt_p40__7','varpunkt_p40__8','varpunkt_p40__9','varpunkt_p40__10','varpunkt_p41']
            
#df= pd.read_csv("responses_master_SSPPBE.csv", encoding='utf-8',index_col=False)
#df= pd.read_csv("responses_master.csv", encoding='utf-8',index_col=False)

#df= pd.read_csv("Capacidades de datos-Matriz de Madurez 2023  (Respuestas) - Respuestas de formulario 1.csv", encoding='utf-8',index_col=False)

#df= pd.read_csv("Respuestas de formulario 05_10_2023_01.csv", encoding='utf-8',index_col=False)


#df= pd.read_csv("respuesta03.csv")

#df= pd.read_csv("malo.csv", low_memory=False)

#df = pd.read_excel('Capacidades de datos-Matriz de Madurez 2023_19_10_2023.xlsx')

df = pd.read_excel('primera_descarga_del_sitio_Web.xlsx')




#df = pd.read_excel('Matriz - pruebas.xlsx')




#print(df)
pepe = (df.columns)



df = df.drop(['ID de envío'], axis=1)
df = df.drop(['Submission URI'], axis=1)
df = df.drop(['Completado'], axis=1)
df = df.drop(['Modificado'], axis=1)
df = df.drop(['Es el borrador'], axis=1)
df = df.drop(['Página actual'], axis=1)
df = df.drop(['Remote IP address'], axis=1)
df = df.drop(['Submitted by: ID'], axis=1)
df = df.drop(['Submitted by: Título'], axis=1)
df = df.drop(['Submitted by: URL'], axis=1)
df = df.drop(['Idioma'], axis=1)
df = df.drop(['Submitted to: Entity type'], axis=1)
df = df.drop(['Submitted to: Entity ID'], axis=1)
df = df.drop(['Bloqueado'], axis=1)
df = df.drop(['Fijo en cabeza de las listas'], axis=1)
df = df.drop(['Notes'], axis=1)
df = df.drop(['Submitted to: Entity title'], axis=1)
df = df.drop(['Submitted to: Entity URL'], axis=1)
df = df.drop(['Serial number'], axis=1)
df = df.drop(['Nombre de la CIudad'], axis=1)
df = df.drop(['País'], axis=1)
df = df.drop(['Institución/empresa'], axis=1)
df = df.drop(['¿Cuál es el nombre del área de gobierno a la que pertenece (Coordinación, Dirección, etc)?  '], axis=1)
#df = df.drop(['País'], axis=1)
#df = df.drop(['País'], axis=1)


df.insert(1, "puntuacion",0)

pepe = (df.columns)


#df = df.reindex(["Creado","puntuacion","Apellido y Nombre","¿Pertenecés a un área del Gobierno de la Ciudad de Buenos Aires?"," Mail","Cargo/puesto que ocupa","¿De que secretaría o subsecretaría depende?","1- ¿Recopilan datos?","2- ¿Tiene Base de datos propias?","3- ¿Quién controla y gestiona la base de datos?","4- ¿Integran los datos de las distintas fuentes que disponen?","5- ¿Utilizan alguna tecnología para integrar  los datos, de diferentes fuentes y sistemas? (APIs, Middleware, Data Warehouse)","6- ¿Tienen documentadas las políticas de integración de datos?","7- ¿Tiene un área destinada a Ciencia de datos?","8- ¿Aplican técnicas estadísticas y modelos matemáticos para analizar los datos?","9- ¿Utilizan herramientas de visualización para crear gráficos y tablas que permitan mostrar el  resultado del análisis de los datos?","10.- ¿Se desarrollan y entrenan modelos de aprendizaje automático y análisis predictivo para predecir patrones y eventos futuros?","11.- ¿Tienen documentados los proyectos de ciencia de datos?","12.- ¿Tienen reportes?","13- ¿Con qué frecuencia actualizan los reportes?","14.- ¿Cuál es la forma de actualización de los reportes?","15.-¿ Los datos están disponibles para las áreas que los requieran?","16.- ¿Los datos se pueden leer usando alguno de los formatos estándares abiertos?","17.- ¿Tienen APIs desarrolladas para que usuarios externos puedan acceder a los datos?","18.- ¿Conoce la normativa de protección de Datos Personales?","19. ¿Está definido por cuánto tiempo se deben guardar los datos personales en el sistema?","20. ¿Tienen clasificados los datos sensibles?","21- ¿Los datos sensibles son recogidos con consentimiento?","22- ¿Existe un mecanismo de minimización o destrucción periódica de los datos?","23- ¿Se generan espacios de diálogos /comités para hablar sobre diferentes temas o evacuar dudas sobre políticas de datos?","24- ¿Tienen lineamientos de protección de datos definidos?","25- ¿Tienen relevados roles respecto a los datos?","26- ¿Existen políticas sobre quién puede utilizar los datos, cómo pueden usarlos, qué partes pueden usar y con qué propósitos?","27- ¿Tienen documentadas las etapas del ciclo de vida de los datos?","28- ¿Realizan capacitaciones para el personal en gobernanza de datos (clasificación, roles)?","29.- ¿Tienen reportes de acceso a los datos?","30.-¿Tienen implementado algún sistema de acceso a la información?","31-   ¿Realizan controles de revisión de la calidad de los datos con cierta periodicidad?","32-  ¿Qué métricas de calidad analizan esos controles?","33- ¿Tienen procesos y procedimientos documentados que analicen el grado de cumplimiento de las métricas de calidad definidas?","34- ¿Tienen perfiles profesionales/técnicos dedicados a evaluar con una periodicidad conocida métricas de calidad?","35- ¿Se intercambian datos...?","36- ¿Tienen definidos mecanismos para que las personas de la organización compartan los datos con un propósito determinado?","37- ¿Tienen perfiles profesionales/técnicos especializados en el tema?","38- ¿Tienen definido un modelo de datos?","39 ¿Qué tan bien documentados están los datos?","40 ¿Tienen documentación del modelo de datos que defina...","41- ¿Tienen personas trabajando que se especialicen en el tema?","Sugerencias"], axis=1)

df = df.iloc[:, [0,1,2,5,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]]

df.to_csv('respuesta_final.csv', index=False, encoding='utf-8',sep=',')

df2 = pd.read_csv("respuesta_final.csv", names=colnames,index_col=False, encoding='utf-8')

df2 = df2.drop(labels=0, axis=0)
df2 = df2.fillna('None')  ## cambio los NaN por 0's

df2.to_csv('Responses.csv', index=False, encoding='utf-8',sep=',')

# Aislo el organismo emisor de las respuestas
organismos  = df2[['fecha','score','nombre_apellido','pertenece_gcba' ,'mail','cargo','secre_subse_area']]
## TENGO QUE REEMPLAZAR LAS RESPUESTAS CON LETRAS POR NUMEROS
codigos = pd.read_csv('libro_codigos_31_07.csv',sep=',', encoding='utf-8')

codigos2 = {}

for i in range(len(codigos)):
     pregunta = codigos.iloc[i]['nombre_pregunta']
     codigo     = codigos.iloc[i]['codigo']
     categoria=codigos.iloc[i]['categoria']
     key, value = pregunta+"-"+categoria, codigo
     codigos2.update({key: value})

### Cargo las reglas de negocio en un vector
lista_acciones = []
with open('reglas_10_07.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        regla05 = "--------------"  
        if len(row)==0:
            break
        
        regla0= str(row[0]).strip()
        if "reglas" in regla0:
               #print("eludo")
               continue
        if " | " in regla0:
               regla0 = regla0.replace(" | ", " or ")
        if not " ^" in regla0  :
                    regla03 = "if  ("+regla0
                    regla04 = regla03.replace(",",".")
                    guion = regla0.find("_")
                    resp = regla0[:guion]
                    regla04 = regla03.replace(" = ", " ): varpunkt_"+resp+" = ")      
                    regla05 = regla04.replace(",",".")
                    regla05 = regla05.replace("==1","=='1'")
                    regla05 = regla05.replace("==2","=='2'")
                    regla05 = regla05.replace("==3","=='3'")
                    regla05 = regla05.replace("==4","=='4'")
                    regla05 = regla05.replace("==5","=='5'")
                    regla05 = regla05.replace("==99","=='99'")

                    lista_acciones.append(regla05) 
                    continue
      
        if  " ^" in regla0  :
                    corte = regla0.find(" ^")
                    trailer = regla0[corte:]
                    header = regla0[:corte]
                    trailer = trailer.replace(" ^","")
                    blanco =  trailer.rfind(" ",1)
                    token = trailer[:blanco]
                    asigna = trailer[blanco:]
                    rearmo = "if  ("+token+" in "+header+" ): varpunkt_"+asigna.strip().replace(".","__")
                    regla05 = rearmo
                    regla05 = regla05.replace('"" ' ,'"')
                    lista_acciones.append(regla05) 
                    continue
"""
Reglas de Negocio cargadas.
"""

f = open("nuevo_df.csv", "w")
linea = 'fecha'+";"+'score'+";"+'nombre_apellido'+";"+'pertenece_gcba'+";"+'mail'+";"+"cargo"+";"+'secre_subse_area'+" ; "+'p1_recop_dat'+" ; "+'p2_bases_dat'+" ; "+'p3_control_base'+" ; "+'p4_integr_dat'+" ; "+'p5_tec_integr_dat'+" ; "+'p6_documen_pol_int'+" ; "+'p7_area_cienc_dat'+" ; "+'p8_apli_tec_ciencia_dat'+" ; "+'p9_herra_vis_dat'+" ; "+'p10_apli_pred'+" ; "+'p11_documen_proy_cie_dat'+" ; "+'p12_tien_report'+" ; "+'p13_act_report'+" ; "+'p14_forma_act_report'+" ; "+'p15_disp_dat'+" ; "+'p16_lect_dat_stand'+" ; "+'p17_api_dat'+" ; "+'p18_norm_prot_dat'+" ; "+'p19_tiemp_dat'+" ; "+'p20_clasif_dat_sens'+" ; "+'p21_dat_sens_consent'+" ; "+'p22_destr_minim_dat'+" ; "+'p23_espac_disc_prot_dat'+" ; "+'p24_lineam_pro_dat'+" ; "+'p25_roles_dat'+" ; "+'p26_polit_uso_dat'+" ; "+'p27_documen_cic_v_dat'+" ; "+'p28_capac_pers_gobern_dat'+" ; "+'p29_report_acc_dat'+" ; "+'p30_sist_acc_info'+" ; "+'p31_revis_cal_dat'+" ; "+'p32_metr_cal_dat'+" ; "+'p33_proc_cal_dat'+" ; "+'p34_per_espec_cal_dat'+" ; "+'p35_interc_dat'+" ; "+'p36_mecan_prop_comp_dat'+" ; "+'p37_pers_espec_reut_dat'+" ; "+'p38_model_dat'+" ; "+'p39_grad_documen_dat'+" ; "+'p40_documen_mod_dat'+" ; "+'p41_pers_espec_model_dat'+" ; "+'sugerencias'
f.write(linea+"\n")


for i in df2.index: 
    # print(df2['p1_recop_dat'][i])
    # print(codigos2.get('p1_recop_dat'''+"-"+df2['p1_recop_dat'][i]))
    # print(str(codigos2.get('p1_recop_dat'''+"-"+df2['p1_recop_dat'][i])))
    
    # print("**********")
    linea = df2['fecha'][i]+" ; "+df2['score'][i]+";"+df2['nombre_apellido'][i]+";"+df2['pertenece_gcba'][i]+";"+df2['mail'][i]+";"+df2['cargo'][i]+";"+df2['secre_subse_area'][i]+";"+str(codigos2.get('p1_recop_dat'''+"-"+df2['p1_recop_dat'][i]))+";"+str(codigos2.get('p2_bases_dat'+"-"+df2['p2_bases_dat'][i]))+";"+str(codigos2.get('p3_control_base'+"-"+df2['p3_control_base'][i]))+";"+str(codigos2.get('p4_integr_dat'+"-"+df2['p4_integr_dat'][i]))+";"+str(codigos2.get('p5_tec_integr_dat'+"-"+df2['p5_tec_integr_dat'][i]))+";"+str(codigos2.get('p6_documen_pol_int'+"-"+df2['p6_documen_pol_int'][i]))+";"+str(codigos2.get('p7_area_cienc_dat'+"-"+df2['p7_area_cienc_dat'][i]))+";"+str(codigos2.get('p8_apli_tec_ciencia_dat'+"-"+df2['p8_apli_tec_ciencia_dat'][i]))+";"+str(codigos2.get('p9_herra_vis_dat'+"-"+df2['p9_herra_vis_dat'][i]))+";"+str(codigos2.get('p10_apli_pred'+"-"+df2['p10_apli_pred'][i]))+";"+str(codigos2.get('p11_documen_proy_cie_dat'+"-"+df2['p11_documen_proy_cie_dat'][i]))+";"+str(codigos2.get('p12_tien_report'+"-"+df2['p12_tien_report'][i]))+";"+str(codigos2.get('p13_act_report'+"-"+df2['p13_act_report'][i]))+";"+str(codigos2.get('p14_forma_act_report'+"-"+df2['p14_forma_act_report'][i]))+";"+str(codigos2.get('p15_disp_dat'+"-"+df2['p15_disp_dat'][i]))+";"+str(codigos2.get('p16_lect_dat_stand'+"-"+df2['p16_lect_dat_stand'][i]))+";"+str(codigos2.get('p17_api_dat'+"-"+df2['p17_api_dat'][i]))+";"+str(codigos2.get('p18_norm_prot_dat'+"-"+df2['p18_norm_prot_dat'][i]))+";"+str(codigos2.get('p19_tiemp_dat'+"-"+df2['p19_tiemp_dat'][i]))+";"+str(codigos2.get('p20_clasif_dat_sens'+"-"+df2['p20_clasif_dat_sens'][i]))+";"+str(codigos2.get('p21_dat_sens_consent'+"-"+df2['p21_dat_sens_consent'][i]))+";"+str(codigos2.get('p22_destr_minim_dat'+"-"+df2['p22_destr_minim_dat'][i]))+";"+str(codigos2.get('p23_espac_disc_prot_dat'+"-"+df2['p23_espac_disc_prot_dat'][i]))+";"+str(codigos2.get('p24_lineam_pro_dat'+"-"+df2['p24_lineam_pro_dat'][i]))+";"+str(codigos2.get('p25_roles_dat'+"-"+df2['p25_roles_dat'][i]))+";"+str(codigos2.get('p26_polit_uso_dat'+"-"+df2['p26_polit_uso_dat'][i]))+";"+str(codigos2.get('p27_documen_cic_v_dat'+"-"+df2['p27_documen_cic_v_dat'][i]))+";"+str(codigos2.get('p28_capac_pers_gobern_dat'+"-"+df2['p28_capac_pers_gobern_dat'][i]))+";"+str(codigos2.get('p29_report_acc_dat'+"-"+df2['p29_report_acc_dat'][i]))+";"+str(codigos2.get('p30_sist_acc_info'+"-"+df2['p30_sist_acc_info'][i]))+";"+str(codigos2.get('p31_revis_cal_dat'+"-"+df2['p31_revis_cal_dat'][i]))+";"+df2['p32_metr_cal_dat'][i].replace(";", " - ")+";"+str(codigos2.get('p33_proc_cal_dat'+"-"+df2['p33_proc_cal_dat'][i]))+";"+str(codigos2.get('p34_per_espec_cal_dat'+"-"+df2['p34_per_espec_cal_dat'][i]))+";"+str(codigos2.get('p35_interc_dat'+"-"+df2['p35_interc_dat'][i]))+";"+str(codigos2.get('p36_mecan_prop_comp_dat'+"-"+df2['p36_mecan_prop_comp_dat'][i]))+";"+str(codigos2.get('p37_pers_espec_reut_dat'+"-"+df2['p37_pers_espec_reut_dat'][i]))+";"+str(codigos2.get('p38_model_dat'+"-"+df2['p38_model_dat'][i]))+";"+str(codigos2.get('p39_grad_documen_dat'+"-"+df2['p39_grad_documen_dat'][i]))+";"+df2['p40_documen_mod_dat'][i].replace(";", " - ")+";"+str(codigos2.get('p41_pers_espec_model_dat'+"-"+df2['p41_pers_espec_model_dat'][i]))    
    f.write(linea+"\n")
f.close()    



df4 = pd.read_csv("nuevo_df.csv", names=colnames,index_col=False, encoding='utf-8',sep=';')

del df4['sugerencias']

print("*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

f = open("Valores.csv", "w")
p = open("Puntajes.csv", "w")

titulo_puntaje = 'varpunkt_p1'+';'+'varpunkt_p2'+';'+'varpunkt_p3'+';'+'varpunkt_p4'+';'+'varpunkt_p5'+';'+'varpunkt_p6'+';'+'varpunkt_p7'+';'+'varpunkt_p8'+';'+'varpunkt_p9'+';'+'varpunkt_p10'+';'+'varpunkt_p11'+';'+'varpunkt_p12'+';'+'varpunkt_p13'+';'+'varpunkt_p14'+';'+'varpunkt_p15'+';'+'varpunkt_p16'+';'+'varpunkt_p17'+';'+'varpunkt_p18'+';'+'varpunkt_p19'+';'+'varpunkt_p20'+';'+'varpunkt_p21'+';'+'varpunkt_p22'+';'+'varpunkt_p23'+';'+'varpunkt_p24'+';'+'varpunkt_p25'+';'+'varpunkt_p26'+';'+'varpunkt_p27'+';'+'varpunkt_p28'+';'+'varpunkt_p29'+';'+'varpunkt_p30'+';'+'varpunkt_p31'+';'+'varpunkt_p32__1'+';'+'varpunkt_p32__2'+';'+'varpunkt_p32__3'+';'+'varpunkt_p32__4'+';'+'varpunkt_p32__5'+';'+'varpunkt_p32__6'+';'+'varpunkt_p32__7'+';'+'varpunkt_p32__8'+';'+'varpunkt_p32__9'+';'+'varpunkt_p32__10'+';'+'varpunkt_p33'+';'+'varpunkt_p34'+';'+'varpunkt_p35'+';'+'varpunkt_p36'+';'+'varpunkt_p37'+';'+'varpunkt_p38'+';'+'varpunkt_p39'+';'+'varpunkt_p40__1'+';'+'varpunkt_p40__2'+';'+'varpunkt_p40__3'+';'+'varpunkt_p40__4'+';'+'varpunkt_p40__5'+';'+'varpunkt_p40__6'+';'+'varpunkt_p40__7'+';'+'varpunkt_p40__8'+';'+'varpunkt_p40__9'+';'+'varpunkt_p40__10'+';'+'varpunkt_p41'+';'+'Nulo'
p.write(titulo_puntaje+"\n")

lista_noaplica = []

for i in df4.index: 
     if i==0:
         continue

     for k in varnames:
         myStr = k
         myTemplate = "{} = {} " 
         statement = myTemplate.format(myStr, 0)
         exec(statement)
         time.sleep(0.1)
     
     for j in range(7,48):
         #print(j)
         myStr = colnames[j]
         myVal = df4.iloc[:,j][i]
         #sys.exit()
         myTemplate = "{} = \"{}\""
         statement = myTemplate.format(myStr, " ")
         #print(statement)
         exec(statement)
     
     for j in range(7,48):
         myStr = colnames[j]
         myVal = df4.iloc[:,j][i]
         myTemplate = "{} = \"{}\""
         statement = myTemplate.format(myStr, myVal)
         f.write(statement+"\n")
         
         if "-1" in statement:
             print("***No Aplica..",statement)
             asacar = statement.replace(' = "-1"',"")
             lista_noaplica.append(str(i-1)+"-"+asacar) 
             
         exec(statement)    
         for t in lista_acciones:
             exec(t)

     for k in varnames:
         myStr = k
         myTemplate = "{} = {} " 
         statement = myTemplate.format(myStr, 0)
         p.write(str(eval(k))+";")

     p.write( "\t- "+"\n")       

   
   
f.close()    
p.close()    



"""
Ahora evaluo las puntuaciones por cada linea de respuestas
"""


final01 = pd.read_csv('Puntajes.csv',sep=';', encoding='utf-8',index_col=False)

final01.reset_index(drop=True, inplace=True)
organismos.reset_index(drop=True, inplace=True)


final02 = final01.join(organismos)

final03 = final02.drop(['Nulo'], axis=1)
final03.to_csv('Scores_Totales.csv', index=False, encoding='utf-8',sep=';')


"""
Aca la lectura de los puntajes , acumular x cada dimension y generar CSV resultados
"""

p = open("Score_Final.csv", "w")
Score_Final_titulo = 'Fecha'+";"+"NombreApellido"+";"+"mail"+";"+'cargo'+";"+"Organismo"+";"+'Fuente de información/Integración'+';'+'Ciencia de datos'+';'+'Actualidad de Reportes/productos'+';'+'Disponibilización'+';'+'Protección de datos'+";"+'Gobernanza de datos'+';'+'Gestión de acceso a datos'+';'+'Calidad de los datos'+';'+'Reutilización de datos'+';'+'Modelo de datos'
p.write(Score_Final_titulo+"\n")


var_dim1 = ['p1_recop_dat','p2_bases_dat','p3_control_base','p4_integr_dat','p5_tec_integr_dat','p6_documen_pol_int']
var_dim2 = ['p7_area_cienc_dat','p8_apli_tec_ciencia_dat','p9_herra_vis_dat','p10_apli_pred','p11_documen_proy_cie_dat']
var_dim3 = ['p12_tien_report','p13_act_report','p14_forma_act_report']
var_dim4 = ['p15_disp_dat','p16_lect_dat_stand','p17_api_dat']
var_dim5 = ['p18_norm_prot_dat','p19_tiemp_dat','p20_clasif_dat_sens','p21_dat_sens_consent','p22_destr_minim_dat','p23_espac_disc_prot_dat','p24_lineam_pro_dat']
var_dim6 = ['p25_roles_dat','p26_polit_uso_dat','p27_documen_cic_v_dat','p28_capac_pers_gobern_dat']
var_dim7 = ['p29_report_acc_dat','p30_sist_acc_info']
var_dim8 = ['p31_revis_cal_dat','p32_metr_cal_dat','p33_proc_cal_dat','p34_per_espec_cal_dat']
var_dim9 = ['p35_interc_dat','p36_mecan_prop_comp_dat','p37_pers_espec_reut_dat']
var_dim10 = ['p38_model_dat','p39_grad_documen_dat','p40_documen_mod_dat','p41_pers_espec_model_dat']

df_dim = pd.read_csv("Scores_Totales.csv",index_col=False, encoding='utf-8',sep=';')
df_dim.fillna(0, inplace=True)

#print(df_dim.index,"///////////")
    
for i in df_dim.index: 
    #print(i,"la i")

    noaplica_dim1 = 0
    noaplica_dim2 = 0
    noaplica_dim3 = 0
    noaplica_dim4 = 0
    noaplica_dim5 = 0
    noaplica_dim6 = 0
    noaplica_dim7 = 0
    noaplica_dim8 = 0
    noaplica_dim9 = 0
    noaplica_dim10 = 0
    
    lista_noaplica2 = []
    for u in lista_noaplica:
        #print(u,"ññññññññññññ")
        lugar = u.find("-")
        fila = int(u[:lugar])
        token = u[lugar+1:]
        #print(token,"pppppppppppp")       
        #print(fila,"999999999999999")
        if fila == i:
            lista_noaplica2.append(token.strip())    

    for k in lista_noaplica2:
        if k in var_dim1:
            noaplica_dim1 = noaplica_dim1 +1         
        if k in var_dim2:
            noaplica_dim2 = noaplica_dim2 +1         
        if k in var_dim3:
            noaplica_dim3 = noaplica_dim3 +1         
        if k in var_dim4:
            noaplica_dim4 = noaplica_dim4 +1         
        if k in var_dim5:
            noaplica_dim5 = noaplica_dim5 +1         
        if k in var_dim6:
            noaplica_dim6 = noaplica_dim6 +1         
        if k in var_dim7:
            noaplica_dim7 = noaplica_dim7 +1         
        if k in var_dim8:
            noaplica_dim8 = noaplica_dim8 +1         
        if k in var_dim9:
            noaplica_dim9 = noaplica_dim9 +1         
        if k in var_dim10:
            noaplica_dim10 = noaplica_dim10 +1         
    
    
    sum_dim1 = 0
    sum_dim2 = 0
    sum_dim3 = 0
    sum_dim4 = 0
    sum_dim5 = 0
    sum_dim6 = 0
    sum_dim7 = 0
    sum_dim8 = 0
    sum_dim9 = 0
    sum_dim10 = 0
    
    sum32 = 0
    sum40 = 0
   
    
    varnames = ['varpunkt_p1','varpunkt_p2','varpunkt_p3','varpunkt_p4','varpunkt_p5','varpunkt_p6','varpunkt_p7','varpunkt_p8','varpunkt_p9','varpunkt_p10','varpunkt_p11','varpunkt_p12','varpunkt_p13','varpunkt_p14','varpunkt_p15','varpunkt_p16','varpunkt_p17','varpunkt_p18','varpunkt_p19','varpunkt_p20','varpunkt_p21','varpunkt_p22','varpunkt_p23','varpunkt_p24','varpunkt_p25','varpunkt_p26','varpunkt_p27','varpunkt_p28','varpunkt_p29','varpunkt_p30','varpunkt_p31','varpunkt_p32__1','varpunkt_p32__2','varpunkt_p32__3','varpunkt_p32__4','varpunkt_p32__5','varpunkt_p32__6','varpunkt_p32__7','varpunkt_p32__8','varpunkt_p32__9','varpunkt_p32__10','varpunkt_p33','varpunkt_p34','varpunkt_p35','varpunkt_p36','varpunkt_p37','varpunkt_p38','varpunkt_p39','varpunkt_p40__1','varpunkt_p40__2','varpunkt_p40__3','varpunkt_p40__4','varpunkt_p40__5','varpunkt_p40__6','varpunkt_p40__7','varpunkt_p40__8','varpunkt_p40__9','varpunkt_p40__10','varpunkt_p41']
    for k in varnames:
        #print(k +"-"+str(df_dim[k][i]))
        guion =  k.rfind("__")
        if guion>0:
            command = k[:guion]
        else :
            command = k
    
        print(k,"k")
        print(i,"i")
        print(df_dim[k][i],"df_dim[k][i]")
        print("***************************")
        #sys.exit()
        
        
        match command:
            case 'varpunkt_p1':
                sum_dim1 = sum_dim1 + df_dim[k][i]
            case 'varpunkt_p2':
                sum_dim1 = sum_dim1 + df_dim[k][i]
            case 'varpunkt_p3':
                sum_dim1 = sum_dim1 + df_dim[k][i]
            case 'varpunkt_p4':
                sum_dim1 = sum_dim1 + df_dim[k][i]
            case 'varpunkt_p5':
                sum_dim1 = sum_dim1 + df_dim[k][i]
            case 'varpunkt_p6':
                sum_dim1 = sum_dim1 + df_dim[k][i]
                
            case 'varpunkt_p7':
                sum_dim2 = sum_dim2 + df_dim[k][i]
            case 'varpunkt_p8':
                sum_dim2 = sum_dim2 + df_dim[k][i]
            case 'varpunkt_p9':
                sum_dim2 = sum_dim2 + df_dim[k][i]
            case 'varpunkt_p10':
                sum_dim2 = sum_dim2 + df_dim[k][i]
            case 'varpunkt_p11':
                sum_dim2 = sum_dim2 + df_dim[k][i]
                
            case 'varpunkt_p12':
                sum_dim3 = sum_dim3 + df_dim[k][i]
            case 'varpunkt_p13':
                sum_dim3 = sum_dim3 + df_dim[k][i]
            case 'varpunkt_p14':
                sum_dim3 = sum_dim3 + df_dim[k][i]
                
            case 'varpunkt_p15':
                sum_dim4 = sum_dim4 + df_dim[k][i]
            case 'varpunkt_p16':
                sum_dim4 = sum_dim4 + df_dim[k][i]
            case 'varpunkt_p17':
                sum_dim4 = sum_dim4 + df_dim[k][i]
                
            case 'varpunkt_p18':
                sum_dim5 = sum_dim5 + df_dim[k][i]
            case 'varpunkt_p19':
                sum_dim5 = sum_dim5 + df_dim[k][i]
            case 'varpunkt_p20':
                sum_dim5 = sum_dim5 + df_dim[k][i]
            case 'varpunkt_p21':
                sum_dim5 = sum_dim5 + df_dim[k][i]
            case 'varpunkt_p22':
                sum_dim5 = sum_dim5 + df_dim[k][i]
            case 'varpunkt_p23':
                sum_dim5 = sum_dim5 + df_dim[k][i]
            case 'varpunkt_p24':
                sum_dim5 = sum_dim5 + df_dim[k][i]
               
            case 'varpunkt_p25':
                sum_dim6 = sum_dim6 + df_dim[k][i]
            case 'varpunkt_p26':
                sum_dim6 = sum_dim6 + df_dim[k][i]
            case 'varpunkt_p27':
                sum_dim6 = sum_dim6 + df_dim[k][i]
            case 'varpunkt_p28':
                sum_dim6 = sum_dim6 + df_dim[k][i]
                
            case 'varpunkt_p29':
                sum_dim7 = sum_dim7 + df_dim[k][i]
            case 'varpunkt_p30':
                sum_dim7 = sum_dim7 + df_dim[k][i]
                
            case 'varpunkt_p31':
                sum_dim8 = sum_dim8 + df_dim[k][i]
            case 'varpunkt_p32':
                sum32 = sum32 + df_dim[k][i]
            case 'varpunkt_p33':
                sum_dim8 = sum_dim8 + df_dim[k][i]
            case 'varpunkt_p34':
                sum_dim8 = sum_dim8 + df_dim[k][i]
                
            case 'varpunkt_p35':
                sum_dim9 = sum_dim9 + df_dim[k][i]
            case 'varpunkt_p36':
                sum_dim9 = sum_dim9 + df_dim[k][i]
            case 'varpunkt_p37':
                sum_dim9 = sum_dim9 + df_dim[k][i]
                
            case 'varpunkt_p38':
                sum_dim10 = sum_dim10 + df_dim[k][i]
            case 'varpunkt_p39':
                sum_dim10 = sum_dim10 + df_dim[k][i]
            case 'varpunkt_p40':
                sum40 = sum40 + df_dim[k][i]
            case 'varpunkt_p41':
                sum_dim10 = sum_dim10 + df_dim[k][i]
                
    if sum32 == 1:
        sum_dim8 = sum_dim8 + 0.7
    if sum32 == 2:
        sum_dim8 = sum_dim8 + 0.8
    if sum32 == 3:
        sum_dim8 = sum_dim8 + 0.9
    if sum32 == 4:
        sum_dim8 = sum_dim8 + 1        
    if sum32 == 5:
        sum_dim8 = sum_dim8 + 1.2
    if sum32 == 6:
        sum_dim8 = sum_dim8 + 1.3
    if sum32 == 7:
        sum_dim8 = sum_dim8 + 1.4
    if sum32 == 8:
        sum_dim8 = sum_dim8 + 1.5 
        
        
    if sum40 == 1:
        sum_dim10 = sum_dim10 + 0.7
    if sum40 == 2:
        sum_dim10 = sum_dim10 + 0.8
    if sum40 == 3:
        sum_dim10 = sum_dim10 + 0.9
    if sum40 == 4:
        sum_dim10 = sum_dim10 + 1        
    if sum40 == 5:
        sum_dim10 = sum_dim10 + 1.2
    if sum40 == 6:
        sum_dim10 = sum_dim10 + 1.3
    if sum40 == 7:
        sum_dim10 = sum_dim10 + 1.4
   
    if sum32 >= 100:
        sum32 = 0
   
    if sum40 >= 100:
        sum40 = 0
   
    if (len(var_dim1) - noaplica_dim1) >0:
        total_dim1  = (sum_dim1  / (len(var_dim1) - noaplica_dim1))  *   len(var_dim1)
    else:
        total_dim1 = 0

    if (len(var_dim2) - noaplica_dim2) >0:
        total_dim2  = (sum_dim2  / (len(var_dim2) - noaplica_dim2))  *   len(var_dim2)
    else:
        total_dim2 = 0

    if (len(var_dim3) - noaplica_dim3) >0:
        total_dim3  = (sum_dim3  / (len(var_dim3) - noaplica_dim3))  *   len(var_dim3)
    else:
        total_dim3 = 0

    if (len(var_dim4) - noaplica_dim4) >0:
        total_dim4  = (sum_dim4  / (len(var_dim4) - noaplica_dim4))  *   len(var_dim4)
    else:
        total_dim4 = 0

    if (len(var_dim5) - noaplica_dim5) >0:
        total_dim5  = (sum_dim5  / (len(var_dim5) - noaplica_dim5))  *   len(var_dim5)
    else:
        total_dim5 = 0

    if (len(var_dim6) - noaplica_dim6) >0:
        total_dim6  = (sum_dim6  / (len(var_dim6) - noaplica_dim6))  *   len(var_dim6)
    else:
        total_dim6 = 0

    if (len(var_dim7) - noaplica_dim7) >0:
        total_dim7  = (sum_dim7  / (len(var_dim7) - noaplica_dim7))  *   len(var_dim7)
    else:
        total_dim7 = 0

    if (len(var_dim8) - noaplica_dim8) >0:
        total_dim8  = (sum_dim8  / (len(var_dim8) - noaplica_dim8))  *   len(var_dim8)
    else:
        total_dim8 = 0

    if (len(var_dim9) - noaplica_dim9) >0:
        total_dim9  = (sum_dim9  / (len(var_dim9) - noaplica_dim9))  *   len(var_dim9)
    else:
        total_dim9 = 0

    if (len(var_dim10) - noaplica_dim10) >0:
        total_dim10  = (sum_dim10  / (len(var_dim10) - noaplica_dim10))  *   len(var_dim10)
    else:
        total_dim10 = 0







    # total_dim2  = (sum_dim2  / (len(var_dim2) - noaplica_dim2))  *   len(var_dim2) 
    # total_dim3  = (sum_dim3  / (len(var_dim3) - noaplica_dim3))  *   len(var_dim3)  
    # total_dim4  = (sum_dim4  / (len(var_dim4) - noaplica_dim4))  *   len(var_dim4)  
    # total_dim5  = (sum_dim5  / (len(var_dim5) - noaplica_dim5))  *   len(var_dim5) 
    
    
    # # jj = (len(var_dim6) - noaplica_dim6)
    # # if jj == 0:
    # #     total_dim6 = 0
    # # else:
        
    # print("sum_dim6",sum_dim6)
    # print("len(var_dim6)",len(var_dim6))
    # print("noaplica_dim6",noaplica_dim6)
    # print("(len(var_dim6) - noaplica_dim6)",(len(var_dim6) - noaplica_dim6))
    
    # total_dim6  = (sum_dim6  / (len(var_dim6) - noaplica_dim6))  *   len(var_dim6)  
        
    # total_dim7  = (sum_dim7  / (len(var_dim7) - noaplica_dim7))  *   len(var_dim7)  
    # total_dim8  = (sum_dim8  / (len(var_dim8) - noaplica_dim8))  *   len(var_dim8)  
    # total_dim9  = (sum_dim9  / (len(var_dim9) - noaplica_dim9))  *   len(var_dim9)  
    # total_dim10 = (sum_dim10 / (len(var_dim10)- noaplica_dim10)) *   len(var_dim10)
   
    print("dimension 1:"+str(total_dim1))
    print("dimension 2:"+str(total_dim2))
    print("dimension 3:"+str(total_dim3))
    print("dimension 4:"+str(total_dim4))
    print("dimension 5:"+str(total_dim5))
    print("dimension 6:"+str(total_dim6))
    print("dimension 7:"+str(total_dim7))
    print("dimension 8:"+str(total_dim8))
    print("dimension 9:"+str(total_dim9))
    print("dimension 10:"+str(total_dim10))
    print("-----final de un registro---------------------")

    #p.write(df_dim['fecha'][i]+";"+df_dim['nombre_apellido'][i]+";"+df_dim['mail'][i]+";"+str(df_dim['cargo'][i])+";"+str(df_dim['secre_subse_area'][i])) # +";"+str(total_dim1)+";"+str(total_dim2)+";"+str(total_dim3)+";"+str(total_dim4)+";"+str(total_dim5)+";"+str(total_dim6)+";"+str(total_dim7)+";"+str(total_dim8)+";"+str(total_dim9)+";"+str(total_dim10)+"\n")
    
    p.write(df_dim['fecha'][i]+";"+df_dim['nombre_apellido'][i]+";"+df_dim['mail'][i]+";"+str(df_dim['cargo'][i])+";"+str(df_dim['secre_subse_area'][i])+";"+str(total_dim1)+";"+str(total_dim2)+";"+str(total_dim3)+";"+str(total_dim4)+";"+str(total_dim5)+";"+str(total_dim6)+";"+str(total_dim7)+";"+str(total_dim8)+";"+str(total_dim9)+";"+str(total_dim10)+"\n")
         

p.close()    
print("-----final del Proceso-------------------")