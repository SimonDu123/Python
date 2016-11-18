import re
import requests
import json
from collections import defaultdict
import xml.etree.ElementTree as etree
import re
import os
import time
from dictdiffer import diff, patch, swap, revert
from requests.exceptions import Timeout, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError

ds_id = 'cc9d5515-e050-4872-be40-1a795a265988'
guid = '1aae7aed-7c2f-414e-9450-6f563e4a6388'
conn_name = 'zhuw12r2spl500_sql2016_sqlserver'
url = 'https://testapi.spotlightessentials.com/api/v2/procedure?' + 'dsid=' + ds_id + '&me=' + conn_name + '&pack=sqlserver_spotlight&proc='
x_user_token = '15fe71b191b04a51a232de7d6a6144b0'
headers = {'x-user-token': x_user_token}
sqlserver_spotlight_list = []
proc_cloud_column_dic = {}
fail_proc_names = []
fail_sqlserver_count = 0
proc_aardvark_column_dic = {}
proc_cloud_column_dic = {}

try:
	os.remove('fail_compare_column.txt')
	os.remove('unresponse_procedure.txt')
except OSError:
	pass

def get_json_content(url,sql_proc):
	try:
		response = requests.get(url+sql_proc,headers = headers)
		if response.status_code != 200:
			#print(url + sql_proc + "\nreturn status code " + str(response.status_code))
			with open('unresponse_procedure.txt','a') as text_file:
				text_file.write(sql_proc+'\n')
		else:
			return response.json()
	except(ReadTimeoutError, ConnectionError) as exc:
		pass

def get_proc_column_names(sql_proc):
	column_names = []
	proc_text_json = get_json_content(url,sql_proc)
	time.sleep(5)
	if proc_text_json:			
		for each in proc_text_json['Columns']:
			column_names.append(each['Name'].lower().replace('iso8601',''))
			proc_cloud_column_dic[sql_proc] = sorted(column_names)
	return(proc_cloud_column_dic)

for file in os.listdir("xmlfiles"):
	if file.lower().startswith('sqlserver_spotlight'):
		sql_proc = file[file.index('-')+1:file.index('.')]
		proc_name = 'xmlfiles\\SQLServer_SpotLight-'+ sql_proc + '.xml'
		tree = etree.parse(proc_name)
		root = tree.getroot()
		column_names = []
		column_name = []
		for column_backgroup in root.iter('component'):
			column_name.append(column_backgroup.attrib)
			alwaysSaveToLucy = column_name[0]['alwaysSaveToLucy']
		# for column_backgroup in root.findall(".//component[@class='com.quest.adk.configuration.component.ProcedureScheduleComponent']"):
		# 	procedure_schedule = column_backgroup.attrib['enabled']

		for column_oopcollect in root.iter('procedureColumn'):
			if column_oopcollect.attrib['sentToProjectLucy'] == 'true' or alwaysSaveToLucy == 'true': 
				column_names.append(column_oopcollect.attrib['name'].lower())
		if column_names:
			proc_aardvark_column_dic[sql_proc] = sorted(column_names)	
		proc_cloud_column_dic = get_proc_column_names(sql_proc)
		result = diff(proc_aardvark_column_dic, proc_cloud_column_dic)
		result_string = ','.join(str(s) for s in list(result))
		if result_string != '':
			# print('true')
			# print(result_string)
			print(sql_proc + '\n')
			print(proc_aardvark_column_dic[sql_proc])
			print('\n')
			print(sql_proc + '\n')
			print(proc_cloud_column_dic[sql_proc])
			print('\n')