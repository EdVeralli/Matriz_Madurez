import pandas as pd
import boto3
import awswrangler as wr
import time
import os
import logging

s3_bucket_raw = os.environ.get('S3_BUCKET_RAW')
s3_bucket_consume = os.environ.get('S3_BUCKET_CONSUME')
s3_bucket_assets = os.environ.get('S3_BUCKET_ASSETS')
raw_db = os.environ.get('DL_RAW_DB')
consume_db = os.environ.get('DL_CONSUME_DB')
dynamodbtable = os.environ.get('DynamoDBTableName')

s3 = boto3.client('s3')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def read_csv_from_s3(key,colnames=None):
    response = s3.get_object(Bucket=s3_bucket_assets, Key=key)
    if colnames == None:
        df = pd.read_csv(response['Body'], index_col=False, encoding='utf-8')
    else: 
        df = pd.read_csv(response['Body'], names=colnames, index_col=False, encoding='utf-8')   
    return df


def lambda_handler(event, context):
    
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
    logger.info(os.environ['AWS_LAMBDA_LOG_STREAM_NAME'])
    logger.info('## EVENT')
    logger.info(event)
    
    query = f"""
    SELECT *
    FROM "{raw_db}"."matriz_madurez_webform_submission_data"
    WHERE fecha_ingesta = (SELECT MAX(fecha_ingesta) FROM "{raw_db}"."matriz_madurez_webform_submission_data")
    """
    
    df = wr.athena.read_sql_query(sql=query, database=raw_db, s3_output=f's3://{s3_bucket_assets}/matriz-madurez/athena-querys/')
    logger.info("Dataframe load successfully")
    
    logger.info("Reading codes")
    codigos_key = 'matriz-madurez/inputs/libro_codigos_31_07.csv'
    df_codigos = read_csv_from_s3(key=codigos_key)
    
    logger.info("Reading rules")
    reglas_key = 'matriz-madurez/inputs/reglas_10_07.csv'
    df_reglas = read_csv_from_s3(key=reglas_key)
   
    p7_area_cienc_dat  = 0
    p12_tien_report = 0
    p38_model_dat  = 0

    colnames = ['fecha_ingesta','score','nombre_apellido','pertenece_gcba' ,'mail','cargo','secre_subse_area','p1_recop_dat','p2_bases_dat','p3_control_base','p4_integr_dat','p5_tec_integr_dat','p6_documen_pol_int','p7_area_cienc_dat','p8_apli_tec_ciencia_dat','p9_herra_vis_dat','p10_apli_pred','p11_documen_proy_cie_dat','p12_tien_report','p13_act_report','p14_forma_act_report','p15_disp_dat','p16_lect_dat_stand','p17_api_dat','p18_norm_prot_dat','p19_tiemp_dat','p20_clasif_dat_sens','p21_dat_sens_consent','p22_destr_minim_dat','p23_espac_disc_prot_dat','p24_lineam_pro_dat','p25_roles_dat','p26_polit_uso_dat','p27_documen_cic_v_dat','p28_capac_pers_gobern_dat','p29_report_acc_dat','p30_sist_acc_info','p31_revis_cal_dat','p32_metr_cal_dat','p33_proc_cal_dat','p34_per_espec_cal_dat','p35_interc_dat','p36_mecan_prop_comp_dat','p37_pers_espec_reut_dat','p38_model_dat','p39_grad_documen_dat','p40_documen_mod_dat','p41_pers_espec_model_dat','sugerencias']
    varnames = ['varpunkt_p1','varpunkt_p2','varpunkt_p3','varpunkt_p4','varpunkt_p5','varpunkt_p6','varpunkt_p7','varpunkt_p8','varpunkt_p9','varpunkt_p10','varpunkt_p11','varpunkt_p12','varpunkt_p13','varpunkt_p14','varpunkt_p15','varpunkt_p16','varpunkt_p17','varpunkt_p18','varpunkt_p19','varpunkt_p20','varpunkt_p21','varpunkt_p22','varpunkt_p23','varpunkt_p24','varpunkt_p25','varpunkt_p26','varpunkt_p27','varpunkt_p28','varpunkt_p29','varpunkt_p30','varpunkt_p31','varpunkt_p32__1','varpunkt_p32__2','varpunkt_p32__3','varpunkt_p32__4','varpunkt_p32__5','varpunkt_p32__6','varpunkt_p32__7','varpunkt_p32__8','varpunkt_p32__9','varpunkt_p32__10','varpunkt_p33','varpunkt_p34','varpunkt_p35','varpunkt_p36','varpunkt_p37','varpunkt_p38','varpunkt_p39','varpunkt_p40__1','varpunkt_p40__2','varpunkt_p40__3','varpunkt_p40__4','varpunkt_p40__5','varpunkt_p40__6','varpunkt_p40__7','varpunkt_p40__8','varpunkt_p40__9','varpunkt_p40__10','varpunkt_p41']
    
    df = df.drop(['webform_id','property'], axis=1)
    df = df.sort_values(by='sid', ascending=True)
    
    for i in df.sid.unique():
        conteo_32 = len(df[(df['sid']==i) & (df['name']=='32_que_metricas_de_calidad_analizan_esos_controles_')])
        if conteo_32 == 0:
            continue
        else:
            index_32 = df[(df['sid']==i) & (df['name']=='32_que_metricas_de_calidad_analizan_esos_controles_')].index[0]
            df.at[index_32, 'value'] = str(conteo_32)
    
        conteo_40 = len(df[(df['sid']==i) & (df['name']=='40_tienen_documentacion_del_modelo_de_datos_que_defina_')])
        if conteo_40 == 0:
            continue
        else:
            index_40 = df[(df['sid']==i) & (df['name']=='40_tienen_documentacion_del_modelo_de_datos_que_defina_')].index[0]
            df.at[index_40, 'value'] = str(conteo_40)

    df_pivot = df.set_index(['sid','delta','fecha_ingesta']).pivot(columns='name',values='value')
    df_pivot = df_pivot.reset_index().groupby('sid').first().drop('delta',axis=1)
    
    columnas = {
        '_de_que_secretaria_o_subsecretaria_depende_' : 'secre_subse_area',
        '_perteneces_a_un_area_del_gobierno_de_la_ciudad_de_buenos_aires_' : 'pertenece_gcba',
        'apellido_y_nombre' : 'nombre_apellido',
        'cargo_puesto_que_ocupa' : 'cargo',
        'correo_electronico' : 'mail',
        '1_recopilan_datos_' : 'p1_recop_dat',
        '2_tiene_base_de_datos_propias_' : 'p2_bases_dat',
        '3_quien_controla_el_y_gestiona_la_base_de_datos_' : 'p3_control_base',
        '4_integran_los_datos_de_las_distintas_fuentes_que_disponen_' : 'p4_integr_dat',
        '5_utilizan_alguna_tecnologia_para_integrar_los_datos_de_diferent' : 'p5_tec_integr_dat',
        '6_tienen_documentadas_las_politicas_de_integracion_de_datos_' : 'p6_documen_pol_int',
        '7_tiene_un_area_destinada_a_ciencia_de_datos_' : 'p7_area_cienc_dat',
        '8_aplican_tecnicas_estadisticas_y_modelos_matematicos_para_anali' : 'p8_apli_tec_ciencia_dat',
        '9_utilizan_herramientas_de_visualizacion_para_crear_graficos_y_t' : 'p9_herra_vis_dat',
        '10_se_desarrollan_y_entrenan_modelos_de_aprendizaje_automatico_y' : 'p10_apli_pred',
        '11_tienen_documentados_los_proyectos_de_ciencia_de_datos_' : 'p11_documen_proy_cie_dat',
        '12_tienen_reportes_' : 'p12_tien_report',
        '13_con_que_frecuencia_actualizan_los_reportes_' : 'p13_act_report',
        '14_forma_reportes' : 'p14_forma_act_report',
        '15_los_datos_estan_disponibles_para_las_areas_que_los_requieran_' : 'p15_disp_dat',
        '16_los_datos_se_pueden_leer_usando_alguno_de_los_formatos_estand' : 'p16_lect_dat_stand',
        '17_tienen_apis_desarrolladas_para_que_usuarios_externos_puedan_a' : 'p17_api_dat',
        '18_conoce_la_normativa_de_proteccion_de_datos_personales_' : 'p18_norm_prot_dat',
        '19_esta_definido_por_cuanto_tiempo_se_deben_guardar_los_datos_pe' : 'p19_tiemp_dat',
        '20_tienen_clasificados_los_datos_sensibles_' : 'p20_clasif_dat_sens',
        '21_los_datos_sensibles_son_recogidos_con_consentimiento_' : 'p21_dat_sens_consent',
        '22_existe_un_mecanismo_de_minimizacion_o_destruccion_periodica_d' : 'p22_destr_minim_dat',
        '23_se_generan_espacios_de_dialogos_comites_para_hablar_sobre_dif' : 'p23_espac_disc_prot_dat',
        '24_tienen_lineamientos_de_proteccion_de_datos_definidos_' : 'p24_lineam_pro_dat',
        '25_tienen_relevados_roles_respecto_a_los_datos_' : 'p25_roles_dat',
        '26_existen_politicas_sobre_quien_puede_utilizar_los_datos_como_p' : 'p26_polit_uso_dat',
        '27_tienen_documentadas_las_etapas_del_ciclo_de_vida_de_los_datos' : 'p27_documen_cic_v_dat',
        '28_realizan_capacitaciones_para_el_personal_en_gobernanza_de_dat' : 'p28_capac_pers_gobern_dat',
        '29_tienen_reportes_de_acceso_a_los_datos_' : 'p29_report_acc_dat',
        '30_tienen_implementado_algun_sistema_de_acceso_a_la_informacion_' : 'p30_sist_acc_info',
        '31_realizan_controles_de_revision_de_la_calidad_de_los_datos_con' : 'p31_revis_cal_dat',
        '32_que_metricas_de_calidad_analizan_esos_controles_' : 'p32_metr_cal_dat',
        '33_tienen_procesos_y_procedimientos_documentados_que_analicen_el' : 'p33_proc_cal_dat',
        '34_tienen_perfiles_profesionales_tecnicos_dedicados_a_evaluar_co' : 'p34_per_espec_cal_dat',
        '35_se_intercambian_datos_' : 'p35_interc_dat',
        '36_tienen_definidos_mecanismos_para_que_las_personas_de_la_organ' : 'p36_mecan_prop_comp_dat',
        '37_tienen_perfiles_profesionales_tecnicos_especializados_en_el_t' : 'p37_pers_espec_reut_dat',
        '38_tienen_definido_un_modelo_de_datos_' : 'p38_model_dat',
        '39_que_tan_bien_documentados_estan_los_datos_' : 'p39_grad_documen_dat',
        '40_tienen_documentacion_del_modelo_de_datos_que_defina_' : 'p40_documen_mod_dat',
        '41_tienen_personas_trabajando_que_se_especialicen_en_el_tema_' : 'p41_pers_espec_model_dat',
        'sugerencias_' : 'sugerencias'
    }
    
    df_pivot = df_pivot.rename(columns=columnas)
    df_pivot = df_pivot.fillna('None')
    df_pivot['score'] = ''
    df = df_pivot.copy().reset_index()
    
    print('############################')
    print(df['sid'])
    
    df_column_id = df['sid']
    
    organismos  = df[['fecha_ingesta','score','nombre_apellido','pertenece_gcba' ,'mail','cargo','secre_subse_area']]
    #df_codigos = pd.read_csv('libro_codigos_31_07.csv',sep=',', encoding='utf-8')
    dict_codigos = {}
    for i in range(len(df_codigos)):
        
            pregunta = df_codigos.iloc[i]['nombre_pregunta']
            codigo = df_codigos.iloc[i]['codigo']
            categoria = df_codigos.iloc[i]['categoria']
            
            key, value = pregunta + "-" + categoria, codigo
        
            dict_codigos.update({key: value})
            
    lista_acciones = []
    
    #df_reglas = pd.read_csv('reglas_10_07.csv',sep=',', encoding='utf-8')
    
    for row in df_reglas['reglas']:
            if len(row)==0:
                break
            else:
                if " | " in row:
                    row = row.replace(" | ", " or ")
                if not " ^" in row  :
                    regla03 = "if  ("+row
                    regla04 = regla03.replace(",",".")
                    guion = row.find("_")
                    resp = row[:guion]
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
                if  " ^" in row  :
                    corte = row.find(" ^")
                    trailer = row[corte:]
                    header = row[:corte]
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
    colnames = ['fecha_ingesta','score','nombre_apellido','pertenece_gcba' ,'mail','cargo','secre_subse_area','p1_recop_dat','p2_bases_dat','p3_control_base','p4_integr_dat','p5_tec_integr_dat','p6_documen_pol_int','p7_area_cienc_dat','p8_apli_tec_ciencia_dat','p9_herra_vis_dat','p10_apli_pred','p11_documen_proy_cie_dat','p12_tien_report','p13_act_report','p14_forma_act_report','p15_disp_dat','p16_lect_dat_stand','p17_api_dat','p18_norm_prot_dat','p19_tiemp_dat','p20_clasif_dat_sens','p21_dat_sens_consent','p22_destr_minim_dat','p23_espac_disc_prot_dat','p24_lineam_pro_dat','p25_roles_dat','p26_polit_uso_dat','p27_documen_cic_v_dat','p28_capac_pers_gobern_dat','p29_report_acc_dat','p30_sist_acc_info','p31_revis_cal_dat','p32_metr_cal_dat','p33_proc_cal_dat','p34_per_espec_cal_dat','p35_interc_dat','p36_mecan_prop_comp_dat','p37_pers_espec_reut_dat','p38_model_dat','p39_grad_documen_dat','p40_documen_mod_dat','p41_pers_espec_model_dat','sugerencias']
    
    logger.info("Business rules loaded")
    
    df_nuevo = pd.DataFrame([], columns=colnames[:-1])
    
    for i in df.index:
        
        data = {
            'fecha_ingesta': df['fecha_ingesta'][i],
            'score': df['score'][i],
            'nombre_apellido': df['nombre_apellido'][i],
            'pertenece_gcba': df['pertenece_gcba'][i],
            'mail': df['mail'][i],
            'cargo': df['cargo'][i],
            'secre_subse_area': df['secre_subse_area'][i],
            'p1_recop_dat': str(dict_codigos.get('p1_recop_dat' + "-" + df['p1_recop_dat'][i])),
            'p2_bases_dat': str(dict_codigos.get('p2_bases_dat'+"-"+df['p2_bases_dat'][i])),
            'p3_control_base' : str(dict_codigos.get('p3_control_base'+"-"+df['p3_control_base'][i])),
            'p4_integr_dat' : str(dict_codigos.get('p4_integr_dat'+"-"+df['p4_integr_dat'][i])),
            'p5_tec_integr_dat' : str(dict_codigos.get('p5_tec_integr_dat'+"-"+df['p5_tec_integr_dat'][i])),
            'p6_documen_pol_int' : str(dict_codigos.get('p6_documen_pol_int'+"-"+df['p6_documen_pol_int'][i])),
            'p7_area_cienc_dat' : str(dict_codigos.get('p7_area_cienc_dat'+"-"+df['p7_area_cienc_dat'][i])),
            'p8_apli_tec_ciencia_dat' : str(dict_codigos.get('p8_apli_tec_ciencia_dat'+"-"+df['p8_apli_tec_ciencia_dat'][i])),
            'p9_herra_vis_dat' : str(dict_codigos.get('p9_herra_vis_dat'+"-"+df['p9_herra_vis_dat'][i])),
            'p10_apli_pred' : str(dict_codigos.get('p10_apli_pred'+"-"+df['p10_apli_pred'][i])),
            'p11_documen_proy_cie_dat' : str(dict_codigos.get('p11_documen_proy_cie_dat'+"-"+df['p11_documen_proy_cie_dat'][i])),
            'p12_tien_report' : str(dict_codigos.get('p12_tien_report'+"-"+df['p12_tien_report'][i])),
            'p13_act_report' : str(dict_codigos.get('p13_act_report'+"-"+df['p13_act_report'][i])),
            'p14_forma_act_report' : str(dict_codigos.get('p14_forma_act_report'+"-"+df['p14_forma_act_report'][i])),
            'p15_disp_dat' : str(dict_codigos.get('p15_disp_dat'+"-"+df['p15_disp_dat'][i])),
            'p16_lect_dat_stand' : str(dict_codigos.get('p16_lect_dat_stand'+"-"+df['p16_lect_dat_stand'][i])),
            'p17_api_dat' : str(dict_codigos.get('p17_api_dat'+"-"+df['p17_api_dat'][i])),
            'p18_norm_prot_dat' : str(dict_codigos.get('p18_norm_prot_dat'+"-"+df['p18_norm_prot_dat'][i])),
            'p19_tiemp_dat' : str(dict_codigos.get('p19_tiemp_dat'+"-"+df['p19_tiemp_dat'][i])),
            'p20_clasif_dat_sens' : str(dict_codigos.get('p20_clasif_dat_sens'+"-"+df['p20_clasif_dat_sens'][i])),
            'p21_dat_sens_consent' : str(dict_codigos.get('p21_dat_sens_consent'+"-"+df['p21_dat_sens_consent'][i])),
            'p22_destr_minim_dat' : str(dict_codigos.get('p22_destr_minim_dat'+"-"+df['p22_destr_minim_dat'][i])),
            'p23_espac_disc_prot_dat' : str(dict_codigos.get('p23_espac_disc_prot_dat'+"-"+df['p23_espac_disc_prot_dat'][i])),
            'p24_lineam_pro_dat' : str(dict_codigos.get('p24_lineam_pro_dat'+"-"+df['p24_lineam_pro_dat'][i])),
            'p25_roles_dat' : str(dict_codigos.get('p25_roles_dat'+"-"+df['p25_roles_dat'][i])),
            'p26_polit_uso_dat' : str(dict_codigos.get('p26_polit_uso_dat'+"-"+df['p26_polit_uso_dat'][i])),
            'p27_documen_cic_v_dat' : str(dict_codigos.get('p27_documen_cic_v_dat'+"-"+df['p27_documen_cic_v_dat'][i])),
            'p28_capac_pers_gobern_dat' : str(dict_codigos.get('p28_capac_pers_gobern_dat'+"-"+df['p28_capac_pers_gobern_dat'][i])),
            'p29_report_acc_dat' : str(dict_codigos.get('p29_report_acc_dat'+"-"+df['p29_report_acc_dat'][i])),
            'p30_sist_acc_info' : str(dict_codigos.get('p30_sist_acc_info'+"-"+df['p30_sist_acc_info'][i])),
            'p31_revis_cal_dat' : str(dict_codigos.get('p31_revis_cal_dat'+"-"+df['p31_revis_cal_dat'][i])),
            'p32_metr_cal_dat' : df['p32_metr_cal_dat'][i],
            'p33_proc_cal_dat' : str(dict_codigos.get('p33_proc_cal_dat'+"-"+df['p33_proc_cal_dat'][i])),
            'p34_per_espec_cal_dat' : str(dict_codigos.get('p34_per_espec_cal_dat'+"-"+df['p34_per_espec_cal_dat'][i])),
            'p35_interc_dat' : str(dict_codigos.get('p35_interc_dat'+"-"+df['p35_interc_dat'][i])),
            'p36_mecan_prop_comp_dat' : str(dict_codigos.get('p36_mecan_prop_comp_dat'+"-"+df['p36_mecan_prop_comp_dat'][i])),
            'p37_pers_espec_reut_dat' : str(dict_codigos.get('p37_pers_espec_reut_dat'+"-"+df['p37_pers_espec_reut_dat'][i])),
            'p38_model_dat' : str(dict_codigos.get('p38_model_dat'+"-"+df['p38_model_dat'][i])),
            'p39_grad_documen_dat' : str(dict_codigos.get('p39_grad_documen_dat'+"-"+df['p39_grad_documen_dat'][i])),
            'p40_documen_mod_dat' : df['p40_documen_mod_dat'][i],
            'p41_pers_espec_model_dat' : str(dict_codigos.get('p41_pers_espec_model_dat'+"-"+df['p41_pers_espec_model_dat'][i]))
        }
    
        df_nuevo.loc[len(df_nuevo)] = data
    
    logger.info("Building scores")
    
    print("Building scores -------",df_nuevo.columns)
    
    puntajes = pd.DataFrame([], columns=varnames)
    lista_noaplica = []
    lista_anula_p7  = []
    lista_anula_p12 = []
    lista_anula_p38 = []

    for i in df_nuevo.index:
        
        lista_puntaje = []

    
        for k in varnames:
            myStr = k
            myTemplate = "{} = {} " 
            statement = myTemplate.format(myStr, 0)
            exec(statement)
            time.sleep(0.1)
            
        for j in range(7,48):
            #print(j)
            myStr = colnames[j]
            myVal = df_nuevo.iloc[:,j][i]
            myTemplate = "{} = \"{}\""
            statement = myTemplate.format(myStr, " ")
            exec(statement)
            
        for j in range(7,48):
            myStr = colnames[j]
            myVal = df_nuevo.iloc[:,j][i]
            myTemplate = "{} = \"{}\""
            statement = myTemplate.format(myStr, myVal)
                
            if "-1" in statement:
                #print("***No Aplica..",statement)
                asacar = statement.replace(' = "-1"',"")
                lista_noaplica.append(str(i)+"-"+asacar)
                
                if asacar == "p7_area_cienc_dat":
                    lista_anula_p7.append(i)
                if asacar == "p12_tien_report":
                    lista_anula_p12.append(i)
                if asacar == "p38_model_dat":
                    lista_anula_p38.append(i)
                    
            exec(statement)    
            for t in lista_acciones:
                exec(t)
                
        for k in varnames:
            myStr = k
            myTemplate = "{} = {} " 
            statement = myTemplate.format(myStr, 0)
            lista_puntaje.append(str(eval(k)))
            
        puntajes.loc[len(puntajes)] = lista_puntaje
        
    
    """
    Ahora evaluo las puntuaciones por cada linea de respuestas
    """
    logger.info("Testing scores")
    puntajes = puntajes.reset_index(drop=True)
    organismos = organismos.reset_index(drop=True)
    
    final = puntajes.join(organismos)
    
    """
    Aca la lectura de los puntajes , acumular x cada dimension y generar CSV resultados
    """
    logger.info("Reading scores")
    Score_Final_titulo = ['fecha_ingesta','nombre_apellido','mail','cargo','organismo','fuente_de_informacion_integracion','ciencia_de_datos','actualidad_de_reportes_productos','disponibilizacion','proteccion_de_datos','gobernanza_de_datos','gestion_de_acceso_a_datos','calidad_de_los_datos','reutilizacion_de_datos','modelo_de_datos','dim_validas','p7','p12','p38']
    
    df_score_final = pd.DataFrame([], columns=Score_Final_titulo)
    
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
    
    for i in final.index: 
        #print(i,"la i")

        p7_area_cienc_dat = 0
        p12_tien_report = 0
        p38_model_dat = 0
    
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
            #print(token)
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
    
        for k in varnames:
            #print(k +"-"+str(df_dim[k][i]))
            guion =  k.rfind("__")
            if guion>0:
                command = k[:guion]
            else :
                command = k
        
            print(k,"k")
            print(i,"i")
            print(final[k][i],"final[k][i]")
            print("***************************")
            
            
            #match command:
    
            if command == 'varpunkt_p1':
                    sum_dim1 = sum_dim1 + float(final[k][i])
            if command == 'varpunkt_p2':
                    sum_dim1 = sum_dim1 + float(final[k][i])
            if command == 'varpunkt_p3':
                    sum_dim1 = sum_dim1 + float(final[k][i])
            if command == 'varpunkt_p4':
                    sum_dim1 = sum_dim1 + float(final[k][i])
            if command == 'varpunkt_p5':
                    sum_dim1 = sum_dim1 + float(final[k][i])
            if command == 'varpunkt_p6':
                    sum_dim1 = sum_dim1 + float(final[k][i])
                    
            if command == 'varpunkt_p7':
                    sum_dim2 = sum_dim2 + float(final[k][i])
            if command == 'varpunkt_p8':
                    sum_dim2 = sum_dim2 + float(final[k][i])
            if command == 'varpunkt_p9':
                    sum_dim2 = sum_dim2 + float(final[k][i])
            if command == 'varpunkt_p10':
                    sum_dim2 = sum_dim2 + float(final[k][i])
            if command == 'varpunkt_p11':
                    sum_dim2 = sum_dim2 + float(final[k][i])
                    
            if command == 'varpunkt_p12':
                    sum_dim3 = sum_dim3 + float(final[k][i])
            if command == 'varpunkt_p13':
                    sum_dim3 = sum_dim3 + float(final[k][i])
            if command == 'varpunkt_p14':
                    sum_dim3 = sum_dim3 + float(final[k][i])
                    
            if command == 'varpunkt_p15':
                    sum_dim4 = sum_dim4 + float(final[k][i])
            if command == 'varpunkt_p16':
                    sum_dim4 = sum_dim4 + float(final[k][i])
            if command == 'varpunkt_p17':
                    sum_dim4 = sum_dim4 + float(final[k][i])
                    
            if command == 'varpunkt_p18':
                    sum_dim5 = sum_dim5 + float(final[k][i])
            if command == 'varpunkt_p19':
                    sum_dim5 = sum_dim5 + float(final[k][i])
            if command == 'varpunkt_p20':
                    sum_dim5 = sum_dim5 + float(final[k][i])
            if command == 'varpunkt_p21':
                    sum_dim5 = sum_dim5 + float(final[k][i])
            if command == 'varpunkt_p22':
                    sum_dim5 = sum_dim5 + float(final[k][i])
            if command == 'varpunkt_p23':
                    sum_dim5 = sum_dim5 + float(final[k][i])
            if command == 'varpunkt_p24':
                    sum_dim5 = sum_dim5 + float(final[k][i])
                    
            if command == 'varpunkt_p25':
                    sum_dim6 = sum_dim6 + float(final[k][i])
            if command == 'varpunkt_p26':
                    sum_dim6 = sum_dim6 + float(final[k][i])
            if command == 'varpunkt_p27':
                    sum_dim6 = sum_dim6 + float(final[k][i])
            if command == 'varpunkt_p28':
                    sum_dim6 = sum_dim6 + float(final[k][i])
                    
            if command == 'varpunkt_p29':
                    sum_dim7 = sum_dim7 + float(final[k][i])
            if command == 'varpunkt_p30':
                    sum_dim7 = sum_dim7 + float(final[k][i])
                    
            if command == 'varpunkt_p31':
                    sum_dim8 = sum_dim8 + float(final[k][i])
            if command == 'varpunkt_p32':
                    sum32 = sum32 + float(final[k][i])
            if command == 'varpunkt_p33':
                    sum_dim8 = sum_dim8 + float(final[k][i])
            if command == 'varpunkt_p34':
                    sum_dim8 = sum_dim8 + float(final[k][i])
                    
            if command == 'varpunkt_p35':
                    sum_dim9 = sum_dim9 + float(final[k][i])
            if command == 'varpunkt_p36':
                    sum_dim9 = sum_dim9 + float(final[k][i])
            if command == 'varpunkt_p37':
                    sum_dim9 = sum_dim9 + float(final[k][i])
                    
            if command == 'varpunkt_p38':
                    sum_dim10 = sum_dim10 + float(final[k][i])
            if command == 'varpunkt_p39':
                    sum_dim10 = sum_dim10 + float(final[k][i])
            if command == 'varpunkt_p40':
                    sum40 = sum40 + float(final[k][i])
            if command == 'varpunkt_p41':
                    sum_dim10 = sum_dim10 + float(final[k][i])
        
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
        
        if (len(var_dim1) == noaplica_dim1) or (len(var_dim1) == 0):
            total_dim1 = 0
        else:
            total_dim1  = (sum_dim1  / (len(var_dim1) - noaplica_dim1))  *   len(var_dim1) 
        if (len(var_dim2) == noaplica_dim2) or (len(var_dim2) == 0):
            total_dim2 = 0
        else:
            total_dim2  = (sum_dim2  / (len(var_dim2) - noaplica_dim2))  *   len(var_dim2) 
        if (len(var_dim3) == noaplica_dim3) or (len(var_dim3) == 0):
            total_dim3 = 0
        else:
            total_dim3  = (sum_dim3  / (len(var_dim3) - noaplica_dim3))  *   len(var_dim3)  
        if (len(var_dim4) == noaplica_dim4) or (len(var_dim4) == 0):
            total_dim4 = 0
        else:
            total_dim4  = (sum_dim4  / (len(var_dim4) - noaplica_dim4))  *   len(var_dim4) 
        if (len(var_dim5) == noaplica_dim5) or (len(var_dim5) == 0):
            total_dim5 = 0
        else:
            total_dim5  = (sum_dim5  / (len(var_dim5) - noaplica_dim5))  *   len(var_dim5) 
        if (len(var_dim6) == noaplica_dim6) or (len(var_dim6) == 0):
            total_dim6 = 0
        else:
            total_dim6  = (sum_dim6  / (len(var_dim6) - noaplica_dim6))  *   len(var_dim6)  
        if (len(var_dim7) == noaplica_dim7) or (len(var_dim7) == 0):
            total_dim7 = 0
        else:
            total_dim7  = (sum_dim7  / (len(var_dim7) - noaplica_dim7))  *   len(var_dim7)
        if (len(var_dim8) == noaplica_dim8) or (len(var_dim8) == 0):
            total_dim8 = 0
        else:
            total_dim8  = (sum_dim8  / (len(var_dim8) - noaplica_dim8))  *   len(var_dim8)  
        if (len(var_dim9) == noaplica_dim9) or (len(var_dim9) == 0): 
            total_dim9 = 0  
        else:
            total_dim9  = (sum_dim9  / (len(var_dim9) - noaplica_dim9))  *   len(var_dim9)  
        if (len(var_dim10) == noaplica_dim10) or (len(var_dim10) == 0): 
            total_dim10 = 0
        else:
            total_dim10 = (sum_dim10 / (len(var_dim10)- noaplica_dim10)) *   len(var_dim10)
        
        dim_validas = 10
        
        if i in lista_anula_p7:
            dim_validas = dim_validas -1
            p7_area_cienc_dat = -1

        if i in lista_anula_p12:
            dim_validas = dim_validas -1
            p12_tien_report = -1        
        
        if i in lista_anula_p38:
            dim_validas = dim_validas -1
            p38_model_dat = -1

        logger.info("dimension 1:"+str(total_dim1))
        logger.info("dimension 2:"+str(total_dim2))
        logger.info("dimension 3:"+str(total_dim3))
        logger.info("dimension 4:"+str(total_dim4))
        logger.info("dimension 5:"+str(total_dim5))
        logger.info("dimension 6:"+str(total_dim6))
        logger.info("dimension 7:"+str(total_dim7))
        logger.info("dimension 8:"+str(total_dim8))
        logger.info("dimension 9:"+str(total_dim9))
        logger.info("dimension 10:"+str(total_dim10))
        
        #print("-----final de un registro---------------------")
        logger.info("End of one record")
        
        data = {
            'fecha_ingesta' : final['fecha_ingesta'][i],
            'nombre_apellido' : final['nombre_apellido'][i],
            'mail' : final['mail'][i],
            'cargo' : final['cargo'][i],
            'organismo' : final['secre_subse_area'][i],
            'fuente_de_informacion_integracion' : str(total_dim1),
            'ciencia_de_datos' : str(total_dim2),
            'actualidad_de_reportes_productos' : str(total_dim3),
            'disponibilizacion' : str(total_dim4),
            'proteccion_de_datos' : str(total_dim5),
            'gobernanza_de_datos' : str(total_dim6),
            'gestion_de_acceso_a_datos' : str(total_dim7),
            'calidad_de_los_datos' : str(total_dim8),
            'reutilizacion_de_datos' : str(total_dim9),
            'modelo_de_datos' : str(total_dim10),
            'dim_validas' : dim_validas,
            'p7' : p7_area_cienc_dat,
            'p12' : p12_tien_report,
            'p38' : p38_model_dat
        }    
        
        df_score_final.loc[len(df_score_final)] = data
    
    df_score_final['sid'] = df_column_id
    
    df_score_final['fecha_procesado'] = pd.Timestamp.today().strftime('%Y-%m-%d')
    df_score_final['fecha_ingesta'] = df_score_final['fecha_ingesta'].astype(str)
    
    #print("-----final del Proceso-------------------")
    logger.info("End of the process")
    
    s3_output_path = 's3://' + s3_bucket_consume + '/matriz-madurez/resultados_ponderados'

    wr.s3.to_parquet(
        df=df_score_final,
        path=s3_output_path,
        dataset=True,
        database=consume_db,
        table='matriz_madurez_resultados_ponderados',
        mode='append'
        )

    logger.info("Saved in datalake")

    # Rename column to ingest in dynamodb
    df_score_final = df_score_final.rename(columns={'fecha_procesado' : 'PK' , 'sid' : 'SK'})

    # Write in DynamoDB table  name of your DynamoDB table
    wr.dynamodb.put_df(df=df_score_final, table_name=dynamodbtable)
    
    logger.info("Dynamo table updated")
    
    return logger.info('updated')
