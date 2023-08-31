# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:44:56 2023
@author: 20171078343
https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python
https://docs.google.com/spreadsheets/d/1n9lBO6LBTYyAtcu2Sp1TC6_ZhNda5RNhIVaPuT6GW60/edit#gid=1986180379
PRIVADO
https://docs.google.com/spreadsheets/d/1DYWcyPsLZQcKAqGRPJkFD7lkXaUbKdGjxkQbzgb-fkE/edit?resourcekey#gid=1986180379
"""
import csv
import os
import sys
import pandas as pd
from os import system
import time

os.chdir("/home/eduardo/GCBA/Encuesta/")

colnames = ['fecha','score' ,'area' ,'nombre_preg_codigo','p1_recop_dat','p2_bases_dat','p3_control_base','p4_integr_dat','p5_tec_integr_dat','p6_documen_pol_int','p7_area_cienc_dat','p8_apli_tec_ciencia_dat','p9_herra_vis_dat','p10_apli_pred','p11_documen_proy_cie_dat','p12_tien_report','p13_act_report','p14_forma_act_report','p15_disp_dat','p16_lect_dat_stand','p17_api_dat','p18_norm_prot_dat','p19_tiemp_dat','p20_clasif_dat_sens','p21_dat_sens_consent','p22_destr_minim_dat','p23_espac_disc_prot_dat','p24_lineam_pro_dat','p25_roles_dat','p26_polit_uso_dat','p27_documen_cic_v_dat','p28_capac_pers_gobern_dat','p29_report_acc_dat','p30_sist_acc_info','p31_revis_cal_dat','p32_metr_cal_dat','p33_proc_cal_dat','p34_per_espec_cal_dat','p35_interc_dat','p36_mecan_prop_comp_dat','p37_pers_espec_reut_dat','p38_model_dat','p39_grad_documen_dat','p40_documen_mod_dat','p41_pers_espec_model_dat','sugerencias']
varnames = ['varpunkt_p1','varpunkt_p2','varpunkt_p3','varpunkt_p4','varpunkt_p5','varpunkt_p6','varpunkt_p7','varpunkt_p8','varpunkt_p9','varpunkt_p10','varpunkt_p11','varpunkt_p12','varpunkt_p13','varpunkt_p14','varpunkt_p15','varpunkt_p16','varpunkt_p17','varpunkt_p18','varpunkt_p19','varpunkt_p20','varpunkt_p21','varpunkt_p22','varpunkt_p23','varpunkt_p24','varpunkt_p25','varpunkt_p26','varpunkt_p27','varpunkt_p28','varpunkt_p29','varpunkt_p30','varpunkt_p31','varpunkt_p32__1','varpunkt_p32__2','varpunkt_p32__3','varpunkt_p32__4','varpunkt_p32__5','varpunkt_p32__6','varpunkt_p32__7','varpunkt_p32__8','varpunkt_p32__9','varpunkt_p32__10','varpunkt_p33','varpunkt_p34','varpunkt_p35','varpunkt_p36','varpunkt_p37','varpunkt_p38','varpunkt_p39','varpunkt_p40__1','varpunkt_p40__2','varpunkt_p40__3','varpunkt_p40__4','varpunkt_p40__5','varpunkt_p40__6','varpunkt_p40__7','varpunkt_p40__8','varpunkt_p40__9','varpunkt_p40__10','varpunkt_p41']
            
#SHEET_ID = '1n9lBO6LBTYyAtcu2Sp1TC6_ZhNda5RNhIVaPuT6GW60'
#SHEET_NAME = 'Matriz01'
#url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
#df = pd.read_csv(url, nrows=6,index_col=False, skiprows = 1)
#df.to_csv('file_name.csv', index=False, encoding='utf-8',sep=',')
#df = pd.read_csv("file_name.csv", names=colnames)
df= pd.read_csv("Responses_21_06.csv", encoding='utf-8',index_col=False)
df.to_csv('respuesta_final.csv', index=False, encoding='utf-8',sep=',')
df2 = pd.read_csv("respuesta_final.csv", names=colnames,index_col=False, encoding='utf-8')
df2 = df2.drop(labels=0, axis=0)
df2 = df2.fillna('None')  ## cambio los NaN por 0's
#print(df2.isnull().sum())
df2.to_csv('Responses.csv', index=False, encoding='utf-8',sep=',')


# Aislo el organismo emisor de las respuestas
organismos  = df2[["area", "nombre_preg_codigo"]]
## TENGO QUE REEMPLAZAR LAS RESPUESTAS CON LETRAS POR NUMEROS
codigos = pd.read_csv('libro_codigos_23_05.csv',sep=';', encoding='utf-8')

codigos2 = {}

for i in range(len(codigos)):
     pregunta = codigos.iloc[i]['nombre_pregunta']
     codigo     = codigos.iloc[i]['codigo']
     categoria=codigos.iloc[i]['categoria']
     key, value = pregunta+"-"+categoria, codigo
     codigos2.update({key: value})

"""
Test
print(codigos2.get("p1_recop_dat-No aplica porque no está dentro de las tareas recopilar datos"))
print(codigos2.get("p2_bases_dat-No sabe"))
"""

# print(len(df2))
# for i in range(len(df2)):
#     for j in range(46):
#         dia = (df2.iloc[i][j])
#         print(dia)
#sys.exit()


#sys.exit()

### Cargo las reglas de negocio en un vector
lista_acciones = []
df3= pd.read_csv("reglas_29_05.csv",sep=';', encoding='utf-8')

with open('reglas_29_05.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        pepe5 = "--------------"  
        pepe= str(row[1]).strip()
        #sys.exit()
        print(pepe+"\n") 
              
        if "reglas" in pepe:
               #print("eludo")
               continue
     
        if " | " in pepe:
               pepe = pepe.replace(" | ", " or ")
                    
        if not " ^" in pepe  :
                    pepe3 = "if  ("+pepe
                    pepe4 = pepe3.replace(",",".")
                    guion = pepe.find("_")
                    resp = pepe[:guion]
                    pepe4 = pepe3.replace(" = ", " ): varpunkt_"+resp+" = ")      
                    pepe5 = pepe4.replace(",",".")
                    #pepe5 = pepe5[:-1]
                    #print("original: ",pepe+"\n")                
                    #print("<<<<<transformada: ",pepe5+"\n")
                    
                    pepe5 = pepe5.replace("==1","=='1'")
                    pepe5 = pepe5.replace("==2","=='2'")
                    pepe5 = pepe5.replace("==3","=='3'")
                    pepe5 = pepe5.replace("==4","=='4'")
                    pepe5 = pepe5.replace("==5","=='5'")
                    pepe5 = pepe5.replace("==99","=='99'")

                    
                    lista_acciones.append(pepe5) 
                    #f.write(pepe5+"\n")
                    #sys.exit()
                    continue
      
        if  " ^" in pepe  :
                    corte = pepe.find(" ^")
                    trailer = pepe[corte:]
                    header = pepe[:corte]
                    trailer = trailer.replace(" ^","")
                    blanco =  trailer.rfind(" ",1)
                    ##### mal asignado el token
                    
                    token = trailer[:blanco]
                    asigna = trailer[blanco:]
                    rearmo = "if  ("+token+" in "+header+" ): varpunkt_"+asigna.strip().replace(".","__")
                    pepe5 = rearmo
                    #print("original: ",pepe+"\n")                
                    #print("<<<<<transformada: ",pepe5+"\n")
                    #pepe5 = pepe5[:-1]
                    pepe5 = pepe5.replace('"" ' ,'"')
                    lista_acciones.append(pepe5) 
                    #f.write(pepe5+"\n")
                    continue

#print('Reglas de Negocio cargadas.')

#sys.exit()




f = open("nuevo_df.csv", "w")

linea = 'fecha'+" ; "+'score' +" ; "+'area' +" ; "+'nombre_preg_codigo'+" ; "+'p1_recop_dat'+" ; "+'p2_bases_dat'+" ; "+'p3_control_base'+" ; "+'p4_integr_dat'+" ; "+'p5_tec_integr_dat'+" ; "+'p6_documen_pol_int'+" ; "+'p7_area_cienc_dat'+" ; "+'p8_apli_tec_ciencia_dat'+" ; "+'p9_herra_vis_dat'+" ; "+'p10_apli_pred'+" ; "+'p11_documen_proy_cie_dat'+" ; "+'p12_tien_report'+" ; "+'p13_act_report'+" ; "+'p14_forma_act_report'+" ; "+'p15_disp_dat'+" ; "+'p16_lect_dat_stand'+" ; "+'p17_api_dat'+" ; "+'p18_norm_prot_dat'+" ; "+'p19_tiemp_dat'+" ; "+'p20_clasif_dat_sens'+" ; "+'p21_dat_sens_consent'+" ; "+'p22_destr_minim_dat'+" ; "+'p23_espac_disc_prot_dat'+" ; "+'p24_lineam_pro_dat'+" ; "+'p25_roles_dat'+" ; "+'p26_polit_uso_dat'+" ; "+'p27_documen_cic_v_dat'+" ; "+'p28_capac_pers_gobern_dat'+" ; "+'p29_report_acc_dat'+" ; "+'p30_sist_acc_info'+" ; "+'p31_revis_cal_dat'+" ; "+'p32_metr_cal_dat'+" ; "+'p33_proc_cal_dat'+" ; "+'p34_per_espec_cal_dat'+" ; "+'p35_interc_dat'+" ; "+'p36_mecan_prop_comp_dat'+" ; "+'p37_pers_espec_reut_dat'+" ; "+'p38_model_dat'+" ; "+'p39_grad_documen_dat'+" ; "+'p40_documen_mod_dat'+" ; "+'p41_pers_espec_model_dat'+" ; "+'sugerencias'

f.write(linea+"\n")

for i in df2.index: 
    #print( df2['fecha'], df2['score' ], df2['area'][i]+" , "+df2['nombre_preg_codigo'][i]+" , "+df2['p1_recop_dat'][i]+" , "+df2['p2_bases_dat'][i]+" , "+df2['p3_control_base'][i]+" , "+df2['p4_integr_dat'][i]+" , "+df2['p5_tec_integr_dat'][i]+" , "+df2['p6_documen_pol_int'][i]+" , "+df2['p7_area_cienc_dat'][i]+" , "+df2['p8_apli_tec_ciencia_dat'][i]+" , "+df2['p9_herra_vis_dat'][i]+" , "+df2['p10_apli_pred'][i]+" , "+df2['p11_documen_proy_cie_dat'][i]+" , "+df2['p12_tien_report'][i]+" , "+df2['p13_act_report'][i]+" , "+df2['p14_forma_act_report'][i]+" , "+df2['p15_disp_dat'][i]+" , "+df2['p16_lect_dat_stand'][i]+" , "+df2['p17_api_dat'][i]+" , "+df2['p18_norm_prot_dat'][i]+" , "+df2['p19_tiemp_dat'][i]+" , "+df2['p20_clasif_dat_sens'][i]+" , "+df2['p21_dat_sens_consent'][i]+" , "+df2['p22_destr_minim_dat'][i]+" , "+df2['p23_espac_disc_prot_dat'][i]+" , "+df2['p24_lineam_pro_dat'][i]+" , "+df2['p25_roles_dat'][i]+" , "+df2['p26_polit_uso_dat'][i]+" , "+df2['p27_documen_cic_v_dat'][i]+" , "+df2['p28_capac_pers_gobern_dat'][i]+" , "+df2['p29_report_acc_dat'][i]+" , "+df2['p30_sist_acc_info'][i]+" , "+df2['p31_revis_cal_dat'][i]+" , "+df2['p32_metr_cal_dat'][i]+" , "+df2['p33_proc_cal_dat'][i]+" , "+df2['p34_per_espec_cal_dat'][i]+" , "+df2['p35_interc_dat'][i]+" , "+df2['p36_mecan_prop_comp_dat'][i]+" , "+df2['p37_pers_espec_reut_dat'][i]+" , "+df2['p38_model_dat'][i]+" , "+df2['p39_grad_documen_dat'][i]+" , "+df2['p40_documen_mod_dat'][i]+" , "+df2['p41_pers_espec_model_dat'][i])

    """
    Test
    resp = "p3_control_base"+"-"+df2['p3_control_base'][i]
    resp = "p1_recop_dat"+"-"+df2['p1_recop_dat'][i]  
    print("resppp")
    print(resp)
    print(codigos2.get(resp))
    """

    #inea = df2['fecha'][i]+" ; "+ df2['score' ][i] +" ; "+df2['area'][i]+" ; "+df2['nombre_preg_codigo'][i]+" ; "+str(codigos2.get('p1_recop_dat'+"-"+df2['p1_recop_dat'][i]))+" ; "+df2['p2_bases_dat'][i]+" ; "+df2['p3_control_base'][i]+" ; "+df2['p4_integr_dat'][i]+" ; "+df2['p5_tec_integr_dat'][i]+" ; "+df2['p6_documen_pol_int'][i]+" ; "+df2['p7_area_cienc_dat'][i]+" ; "+df2['p8_apli_tec_ciencia_dat'][i]+" ; "+df2['p9_herra_vis_dat'][i]+" ; "+df2['p10_apli_pred'][i]+" ; "+df2['p11_documen_proy_cie_dat'][i]+" ; "+df2['p12_tien_report'][i]+" ; "+df2['p13_act_report'][i]+" ; "+df2['p14_forma_act_report'][i]+" ; "+df2['p15_disp_dat'][i]+" ; "+df2['p16_lect_dat_stand'][i]+" ; "+df2['p17_api_dat'][i]+" ; "+df2['p18_norm_prot_dat'][i]+" ; "+df2['p19_tiemp_dat'][i]+" ; "+df2['p20_clasif_dat_sens'][i]+" ; "+df2['p21_dat_sens_consent'][i]+" ; "+df2['p22_destr_minim_dat'][i]+" ; "+df2['p23_espac_disc_prot_dat'][i]+" ; "+df2['p24_lineam_pro_dat'][i]+" ; "+df2['p25_roles_dat'][i]+" ; "+df2['p26_polit_uso_dat'][i]+" ; "+df2['p27_documen_cic_v_dat'][i]+" ; "+df2['p28_capac_pers_gobern_dat'][i]+" ; "+df2['p29_report_acc_dat'][i]+" ; "+df2['p30_sist_acc_info'][i]+" ; "+df2['p31_revis_cal_dat'][i]+" ; "+df2['p32_metr_cal_dat'][i]+" ; "+df2['p33_proc_cal_dat'][i]+" ; "+df2['p34_per_espec_cal_dat'][i]+" ; "+df2['p35_interc_dat'][i]+" ; "+df2['p36_mecan_prop_comp_dat'][i]+" ; "+df2['p37_pers_espec_reut_dat'][i]+" ; "+df2['p38_model_dat'][i]+" ; "+df2['p39_grad_documen_dat'][i]+" ; "+df2['p40_documen_mod_dat'][i]+" ; "+df2['p41_pers_espec_model_dat'][i]
   
    linea = df2['fecha'][i]+" ; "+str(codigos2.get('score'+"-"+df2['score'][i]))+";"+str(codigos2.get('area'+"-"+df2['area'][i]))+";"+str(codigos2.get('nombre_preg_codigo'+"-"+df2['nombre_preg_codigo'][i]))+";"+str(codigos2.get('p1_recop_dat'''+"-"+df2['p1_recop_dat'][i]))+";"+str(codigos2.get('p2_bases_dat'+"-"+df2['p2_bases_dat'][i]))+";"+str(codigos2.get('p3_control_base'+"-"+df2['p3_control_base'][i]))+";"+str(codigos2.get('p4_integr_dat'+"-"+df2['p4_integr_dat'][i]))+";"+str(codigos2.get('p5_tec_integr_dat'+"-"+df2['p5_tec_integr_dat'][i]))+";"+str(codigos2.get('p6_documen_pol_int'+"-"+df2['p6_documen_pol_int'][i]))+";"+str(codigos2.get('p7_area_cienc_dat'+"-"+df2['p7_area_cienc_dat'][i]))+";"+str(codigos2.get('p8_apli_tec_ciencia_dat'+"-"+df2['p8_apli_tec_ciencia_dat'][i]))+";"+str(codigos2.get('p9_herra_vis_dat'+"-"+df2['p9_herra_vis_dat'][i]))+";"+str(codigos2.get('p10_apli_pred'+"-"+df2['p10_apli_pred'][i]))+";"+str(codigos2.get('p11_documen_proy_cie_dat'+"-"+df2['p11_documen_proy_cie_dat'][i]))+";"+str(codigos2.get('p12_tien_report'+"-"+df2['p12_tien_report'][i]))+";"+str(codigos2.get('p13_act_report'+"-"+df2['p13_act_report'][i]))+";"+str(codigos2.get('p14_forma_act_report'+"-"+df2['p14_forma_act_report'][i]))+";"+str(codigos2.get('p15_disp_dat'+"-"+df2['p15_disp_dat'][i]))+";"+str(codigos2.get('p16_lect_dat_stand'+"-"+df2['p16_lect_dat_stand'][i]))+";"+str(codigos2.get('p17_api_dat'+"-"+df2['p17_api_dat'][i]))+";"+str(codigos2.get('p18_norm_prot_dat'+"-"+df2['p18_norm_prot_dat'][i]))+";"+str(codigos2.get('p19_tiemp_dat'+"-"+df2['p19_tiemp_dat'][i]))+";"+str(codigos2.get('p20_clasif_dat_sens'+"-"+df2['p20_clasif_dat_sens'][i]))+";"+str(codigos2.get('p21_dat_sens_consent'+"-"+df2['p21_dat_sens_consent'][i]))+";"+str(codigos2.get('p22_destr_minim_dat'+"-"+df2['p22_destr_minim_dat'][i]))+";"+str(codigos2.get('p23_espac_disc_prot_dat'+"-"+df2['p23_espac_disc_prot_dat'][i]))+";"+str(codigos2.get('p24_lineam_pro_dat'+"-"+df2['p24_lineam_pro_dat'][i]))+";"+str(codigos2.get('p25_roles_dat'+"-"+df2['p25_roles_dat'][i]))+";"+str(codigos2.get('p26_polit_uso_dat'+"-"+df2['p26_polit_uso_dat'][i]))+";"+str(codigos2.get('p27_documen_cic_v_dat'+"-"+df2['p27_documen_cic_v_dat'][i]))+";"+str(codigos2.get('p28_capac_pers_gobern_dat'+"-"+df2['p28_capac_pers_gobern_dat'][i]))+";"+str(codigos2.get('p29_report_acc_dat'+"-"+df2['p29_report_acc_dat'][i]))+";"+str(codigos2.get('p30_sist_acc_info'+"-"+df2['p30_sist_acc_info'][i]))+";"+str(codigos2.get('p31_revis_cal_dat'+"-"+df2['p31_revis_cal_dat'][i]))+";"+df2['p32_metr_cal_dat'][i]+";"+str(codigos2.get('p33_proc_cal_dat'+"-"+df2['p33_proc_cal_dat'][i]))+";"+str(codigos2.get('p34_per_espec_cal_dat'+"-"+df2['p34_per_espec_cal_dat'][i]))+";"+str(codigos2.get('p35_interc_dat'+"-"+df2['p35_interc_dat'][i]))+";"+str(codigos2.get('p36_mecan_prop_comp_dat'+"-"+df2['p36_mecan_prop_comp_dat'][i]))+";"+str(codigos2.get('p37_pers_espec_reut_dat'+"-"+df2['p37_pers_espec_reut_dat'][i]))+";"+str(codigos2.get('p38_model_dat'+"-"+df2['p38_model_dat'][i]))+";"+str(codigos2.get('p39_grad_documen_dat'+"-"+df2['p39_grad_documen_dat'][i]))+";"+df2['p40_documen_mod_dat'][i]+";"+str(codigos2.get('p41_pers_espec_model_dat'+"-"+df2['p41_pers_espec_model_dat'][i]))    
    f.write(linea+"\n")
    
f.close()    

df4 = pd.read_csv("nuevo_df.csv", names=colnames,index_col=False, encoding='utf-8',sep=';')
del df4['sugerencias']
#sys.exit()

#system("clear")
print("*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


#columns_names2 = df.columns.values


#system("clear")

f = open("Valores.csv", "w")
p = open("Puntajes.csv", "w")

titulo_puntaje = 'varpunkt_p1'+';'+'varpunkt_p2'+';'+'varpunkt_p3'+';'+'varpunkt_p4'+';'+'varpunkt_p5'+';'+'varpunkt_p6'+';'+'varpunkt_p7'+';'+'varpunkt_p8'+';'+'varpunkt_p9'+';'+'varpunkt_p10'+';'+'varpunkt_p11'+';'+'varpunkt_p12'+';'+'varpunkt_p13'+';'+'varpunkt_p14'+';'+'varpunkt_p15'+';'+'varpunkt_p16'+';'+'varpunkt_p17'+';'+'varpunkt_p18'+';'+'varpunkt_p19'+';'+'varpunkt_p20'+';'+'varpunkt_p21'+';'+'varpunkt_p22'+';'+'varpunkt_p23'+';'+'varpunkt_p24'+';'+'varpunkt_p25'+';'+'varpunkt_p26'+';'+'varpunkt_p27'+';'+'varpunkt_p28'+';'+'varpunkt_p29'+';'+'varpunkt_p30'+';'+'varpunkt_p31'+';'+'varpunkt_p32__1'+';'+'varpunkt_p32__2'+';'+'varpunkt_p32__3'+';'+'varpunkt_p32__4'+';'+'varpunkt_p32__5'+';'+'varpunkt_p32__6'+';'+'varpunkt_p32__7'+';'+'varpunkt_p32__8'+';'+'varpunkt_p32__9'+';'+'varpunkt_p32__10'+';'+'varpunkt_p33'+';'+'varpunkt_p34'+';'+'varpunkt_p35'+';'+'varpunkt_p36'+';'+'varpunkt_p37'+';'+'varpunkt_p38'+';'+'varpunkt_p39'+';'+'varpunkt_p40__1'+';'+'varpunkt_p40__2'+';'+'varpunkt_p40__3'+';'+'varpunkt_p40__4'+';'+'varpunkt_p40__5'+';'+'varpunkt_p40__6'+';'+'varpunkt_p40__7'+';'+'varpunkt_p40__8'+';'+'varpunkt_p40__9'+';'+'varpunkt_p40__10'+';'+'varpunkt_p41'+';'+'Nulo'
p.write(titulo_puntaje+"\n")


for i in df4.index: 
     #print("--p1_integra_datos"+ df["p1_integra_datos"][i]+ " valor :"+str(df["p2_recop_dat"][i]  ))
     if i==0:
         continue
     #print("---->"+ str(df["p5_cuales_bases"][i]))
     for k in varnames:
         myStr = k
         myTemplate = "{} = {} " 
         statement = myTemplate.format(myStr, 0)
         exec(statement)
         time.sleep(0.1)
     #sys.exit()    
      # limpio la corrida anterior   

     for j in range(4,45):
         #print(j)
         myStr = colnames[j]
         myVal = df4.iloc[:,j][i]
         myTemplate = "{} = \"{}\""
         statement = myTemplate.format(myStr, " ")
         #print(statement)
         exec(statement)
         time.sleep(0.1)
        # sys.exit()

     
     for j in range(4,45):
     #for j in range(4,5):
         
         #print(j)
         myStr = colnames[j]
         myVal = df4.iloc[:,j][i]
         myTemplate = "{} = \"{}\""
         statement = myTemplate.format(myStr, myVal)
         #print("campo valor-----------------------")
         f.write(statement+"\n")
         #print(statement)
         exec(statement)    
         #print("Fin campo valor-----------------------")
         time.sleep(0.1)
         #print("-------------------------reglas a aplicar")
         for t in lista_acciones:
             exec(t)
             time.sleep(0.1)
             
         print("FIN -------------------------reglas a aplicar")
         #sys.exit()
         
     # imprimo todas las variables de esa fila procesada...
     #p.write( "\tFila "+str(i)+"\n")
     for k in varnames:
         myStr = k
         myTemplate = "{} = {} " 
         statement = myTemplate.format(myStr, 0)
         p.write(str(eval(k))+";")
         #exec(statement)
         #time.sleep(0.2)
     #globals()
     p.write( "\t- "+"\n")       
         ### Ahora evaluo las puntuaciones por cada linea de respuestas.
   
   
f.close()    
p.close()    

final01 = pd.read_csv('Puntajes.csv',sep=';', encoding='utf-8',index_col=False)

# final01 = final01.reset_index()
# organismos = organismos.reset_index()

final01.reset_index(drop=True, inplace=True)
organismos.reset_index(drop=True, inplace=True)


final02 = final01.join(organismos)

final03 = final02.drop(['Nulo'], axis=1)

final03.to_csv('Scores_Totales.csv', index=False, encoding='utf-8',sep=';')


Scores01 = pd.read_csv('Scores_Totales.csv',sep=';', encoding='utf-8',index_col=False)
for i in Scores01.index: 
     #print("--p1_integra_datos"+ df["p1_integra_datos"][i]+ " valor :"+str(df["p2_recop_dat"][i]  ))
     if i==0:
         continue
     print("---->"+ str(Scores01["varpunkt_p40__5"][i]))
     # for k in varnames:
     #     myStr = k
     #     myTemplate = "{} = {} " 
     #     statement = myTemplate.format(myStr, 0)
     #     exec(statement)
     #     time.sleep(0.1)
     #sys.exit()    
      # limpio la corrida anterior   
sys.exit        




     #sys.exit()
     #print("--")
     #pass



# print("-.-------------------------------------\n-")    
# print(columns_names2[3])


# print("-.-------------------------------------\n-")    
# print(columns_names2[69])



# myStr = columns_names2[3]
# myVal = "Juan"
# myTemplate = "{} = \"{}\""
# statement = myTemplate.format(myStr, myVal)
# exec(statement)
# #print(domain)


