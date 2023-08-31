# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:44:56 2023

@author: 20171078343


https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python


https://docs.google.com/spreadsheets/d/1n9lBO6LBTYyAtcu2Sp1TC6_ZhNda5RNhIVaPuT6GW60/edit#gid=1986180379


PRIVADO
https://docs.google.com/spreadsheets/d/1DYWcyPsLZQcKAqGRPJkFD7lkXaUbKdGjxkQbzgb-fkE/edit?resourcekey#gid=1986180379



##############################


misdatos <- misdatos %>% mutate(p1_integra_datos=case_when(r1=="En forma permanente"~1,
                                  r1=="Varias veces al día"~2,
                                  r1=="En forma diaria"~3,
                                  r1=="Cada pocos días"~4,
                                  r1=="Algunas veces al mes"~5,
                                  r1=="Nunca"~6,
                                  r1=="No aplica porque no está dentro de las tareas del área integrar los datos"~7)) %>% 
                        mutate(p2_recop_dat =case_when(r2=="Si" ~1,
                                  r2=="No" ~2,
                                  r2=="No sabe" ~3,
                                  r2=="No aplica porque no está dentro de las tareas del área recopilar datos" ~4)) %>% 
                        mutate(p3_como_recop=case_when(r3=="Prinicpalmente en papel" ~1,
                                  r3=="Formularios de google" ~2,
                                  r3=="Sistemas como lime survey/monkey survey y similares" ~3,
                                  r3=="Sistemas de recopilación diseñados ad/hoc" ~4,
                                  r3=="Toman datos de fuentes secundarias ya existentes" ~5)) %>%
                        mutate(p4_bases_prop=case_when(r4=="Si" ~1,
                                  r4=="No, pero es una tarea que el área debería realizar" ~2,
                                  r4=="No sabe" ~3,
                                  r4=="No aplica porque no está dentro de las tareas del área la construcción de una base de datos" ~4)) %>%
                        mutate(p6_cuanto_integ_dat=case_when(r6=="Completamente integrados" ~1,
                                  r6=="Bastante integrados" ~2,
                                  r6=="Poco integrados" ~3,
                                  r6=="Nada integrados" ~4,
                                  r6=="No aplica porque no está dentro de las tareas del área integrar datos" ~5)) %>%
                        mutate(p7_tec_integr_dat=case_when(r7=="Si" ~1,
                                  r7=="No" ~2,
                                  r7=="No sabe" ~3,
                                  r7=="No aplica porque no está dentro de las tareas del área integrar datos" ~4)) %>%
                        mutate(p8_documen_pol_int=case_when(r8=="Completamente documentada" ~1, 
                                  r8=="Bastante documentada" ~2,
                                  r8=="Poco documentada" ~3,
                                  r8=="Nada documentada" ~4,
                                  r8=="No aplica porque no está dentro de las tareas del área integrar datos" ~5))                                                               
                                                               
## ordeno las variables como están en lel formulario ##







####################################








"""


import csv
import os
import sys
import pandas as pd

os.chdir("/home/eduardo/GCBA/Encuesta/")

f = open("nuevas reglas.csv", "w")



#colnames = ['caso','fecha','puntua','p1_integra_datos','p2_recop_dat','p3_como_recop','p4_bases_prop','p5_cuales_bases','p6_cuanto_integ_dat','p7_tec_integr_dat','p8_documen_pol_int','p9_report_dat','p10_cuales_rep','p11_apli_tec_ciencia_dat','p12_cuales_tecn_cd','p13_proc_automat','p14_frec_aplic','p15_documen_proy_cd','p16_tien_report','p17_act_report','p18_forma_act_report','p19_satisf_usu_report','p20_modif_report','p21_disp_dat','p22_frec_disp_dat','p23_lect_dat_stand','p24_api_dat','p25_leng_adec','p26_norm_prot_dat','p27_tiemp_dat','p28_clasif_dat_sens','p29_dat_sens_consent','p30_destr_dat_sens','p31_frec_destr_dat_sens','p32_espac_dial_prot_dat','p33_lineam_pro_dat','p34_roles_dat','p35_cuales_roles','p36_polit_uso_dat','p37_aud_vpn_acc','p38_documen_cic_v_dat','p39_lineam_implem','p40_capac_pers_gobern_dat','p41_polit_acc_inf','p42_como_acc','p43_report_acc','p44_audit_acc','p45_automat_audit','p46_protoc_acc','p47_arq_dat','p48_arq_fis_log','p49_reposit_almac_dat','p50_def_semant_dat','p51_arq_metadat','p52_pers_espec_arq','p53_dimens_cal_dat','p54_revis_cal_dat','p55_metr_cal_dat','p56_proc_cal_dat','p57_per_espec_cal_dat','p58_interc_dat','p59_comp_dat_inter','p60_comp_dat_exter','p61_mecan_prop_comp_dat','p62_pers_espec_reut_dat','p63_model_dat','p64_model_dat_documen','p65_grad_documen_dat','p66_documen_mod_dat','p67_pers_espec_model_dat']
colnames = ['fecha','score' ,'area' ,'nombre_preg_codigo','p1_recop_dat','p2_bases_dat','p3_control_base','p4_integr_dat','p5_tec_integr_dat','p6_documen_pol_int','p7_area_cienc_dat','p8_apli_tec_ciencia_dat','p9_herra_vis_dat','p10_apli_pred','p11_documen_proy_cie_dat','p12_tien_report','p13_act_report','p14_forma_act_report','p15_disp_dat','p16_lect_dat_stand','p17_api_dat','p18_norm_prot_dat','p19_tiemp_dat','p20_clasif_dat_sens','p21_dat_sens_consent','p22_destr_minim_dat','p23_espac_disc_prot_dat','p24_lineam_pro_dat','p25_roles_dat','p26_polit_uso_dat','p27_documen_cic_v_dat','p28_capac_pers_gobern_dat','p29_report_acc_dat','p30_sist_acc_info','p31_revis_cal_dat','p32_metr_cal_dat','p33_proc_cal_dat','p34_per_espec_cal_dat','p35_interc_dat','p36_mecan_prop_comp_dat','p37_pers_espec_reut_dat','p38_model_dat','p39_grad_documen_dat','p40_documen_mod_dat','p41_pers_espec_model_dat','sugerencias']

#SHEET_ID = '1n9lBO6LBTYyAtcu2Sp1TC6_ZhNda5RNhIVaPuT6GW60'
#SHEET_NAME = 'Matriz01'
#url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
#df = pd.read_csv(url, nrows=6,index_col=False, skiprows = 1)
#df.to_csv('file_name.csv', index=False, encoding='utf-8',sep=',')
#df = pd.read_csv("file_name.csv", names=colnames)
df= pd.read_csv("respuestas_10_05.csv", encoding='utf-8',index_col=False)
df.to_csv('file_name.csv', index=False, encoding='utf-8',sep=',')
df2 = pd.read_csv("file_name.csv", names=colnames,index_col=False, encoding='utf-8')
df2 = df2.drop(labels=0, axis=0)
lista_acciones = []

# print(len(df2))
# for i in range(len(df2)):
#     for j in range(46):
#         dia = (df2.iloc[i][j])
#         print(dia)
#sys.exit()
df3= pd.read_csv("reglas_11_5.csv",sep=';', encoding='utf-8')
#sys.exit()
pepe5 = "--------------"  

with open('reglas_11_5.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        pepe5 = "--------------"  
        pepe= str(row[1]).strip()
        #sys.exit()
        #print(pepe+"\n",line_count) 
        if line_count == 0:
                #print(f'Columnas son {", ".join(row)}')
               line_count += 1
               
               
        if "reglas " in pepe:
               continue

        if " | " in pepe:
               pepe = pepe.replace(" | ", " or ")
                    
        if not " ^" in pepe  :
                    pepe3 = "if  ("+pepe
                    pepe4 = pepe3.replace(" = ", " ): var_punkt"+str(line_count).zfill(4)+" = ")
                    pepe5 = pepe4.replace(",",".")
                    #print("\n**************************"+ pepe5+"------------------\n") 
  
        if  " ^" in pepe  :
                    corte = pepe.find(" ^")
                    trailer = pepe[corte:]
                    header = pepe[:corte]
                    trailer = trailer.replace(" ^","")
                    blanco =  trailer.find(" ",2)
                    token = trailer[:blanco]
                    asigna = trailer[blanco:]
                    rearmo = "if  ("+token+" in "+header+" ): var_punkt"+str(line_count).zfill(4)+" = "+asigna
                    pepe5 = rearmo
                    print("\n**************************"+ pepe5+"------------------\n") 
                    
             
              
        print("original: ",pepe+"\n")                
        #pepe5 = pepe4.replace(",",".")
        print("<<<<<transformada: ",pepe5+"\n")
        lista_acciones.append(pepe5+"------------"+pepe) 
        f.write(pepe5+"\n")
        #sys.exit()
 
        line_count += 1
         #print(f' {line_count} Reglas de Negocio cargadas.')


columns_names2 = df.columns.values

f.close()
sys.exit()

for i in df.index: 
     #print("--p1_integra_datos"+ df["p1_integra_datos"][i]+ " valor :"+str(df["p2_recop_dat"][i]  ))
           
     #print("---->"+ str(df["p5_cuales_bases"][i]))
     for j in range(3,69):
         #print(j)
         myStr = columns_names2[j]
         myVal = df.iloc[:,j][i]
         myTemplate = "{} = \"{}\""
         statement = myTemplate.format(myStr, myVal)
         print(statement)
         exec(statement)        
         #sys.exit        

     #sys.exit()
     #print("--")
     #pass



# print("-.-------------------------------------\n-")    
# print(columns_names2[3])


# print("-.-------------------------------------\n-")    
# print(columns_names2[69])



myStr = columns_names2[3]
myVal = "Juan"
myTemplate = "{} = \"{}\""
statement = myTemplate.format(myStr, myVal)
exec(statement)
#print(domain)


