import re
import requests
import json
ds_id = '5210c65f-5362-475a-8a50-a4a656cd4f2e'
old_guid = 'bfa74586-cbc1-4ae2-98e1-64ef240b394f'
new_guid = 'e475bcae-fd1b-4fd7-9f04-015095e81e53'
conn_name = 'zhuw12r2spl500_sql2016_sqlserver'
url = 'https://testapi.spotlightessentials.com/api/v2/'
url_ds = url + 'diagnostic-servers'
url_conn = url + 'connections?dsid=' + ds_id + '&me=' + conn_name
url_proc = url + 'procedure?dsid=' + ds_id + '&me=' + conn_name + '&pack=sqlserver_spotlight&proc='
x_user_token = '64ecca1929f64c3a849d04b9ce652912'
headers = {'x-user-token': x_user_token}
procedures = ['HealthCheckAdhocWorkloadConfiguration',
			  'HealthCheckDatabaseBackups',
			  'HealthCheckDatabases',
			  'healthcheckdataspaces',
			  'HealthCheckGuestAccess',
			  'HealthCheckMasterFiles',
			  'HealthCheckMissingIndexes',
			  'HealthCheckOSProcessMemory',
			  'HealthCheckOSSystemMemory',
			  'HealthCheckSQLLogins',
			  'HealthCheckSysInfo',
			  'HealthCheckSysObjects',
			  'HealthCheckSystemConfiguration',
			  'HealthCheckVirtualFileStats',
			  'HealthCheckWaitStatistics',
			  'HealthCheckSQLLogins']
regexp = {re.compile(r'31090\b'):'29939',re.compile(old_guid):new_guid,
		re.compile(r'[0-9]{13}'):'{{timeStamp}}',re.compile(r'20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z'):'{{isoTimeStamp}}'}

def replace(text):
	for pattern, key in regexp.items():
		text = re.sub(pattern,key,text)
	return text

def get_json_content(filename,url):
	response = requests.get(url,headers = headers)
	if response.status_code != 200:
		print(url + "\nreturn status code " + str(response.status_code))
		return(response.text)
	return replace(response.text)	
			
def process_ds_conn(jsonfile):
	ds_text = ''
	ds_text = get_json_content(jsonfile,url_ds)
	ds_object = json.loads(ds_text)
	for element in ds_object:
		element.pop('CreateDateUtc')
		element.pop('MonitoringConfig',None)
		element.pop('UpdateDateUtc')
		element.pop('UserAgent')
	ds_text = ''.join(str(e) for e in ds_object)
	with open(jsonfile,'w') as text_file:
		text_file.write(ds_text.lower())

def process_proc(jsonfile):
	proc_text = ''
	for proc in procedures:	
		proc_text += get_json_content(jsonfile,url_proc + proc) + ','
	proc_text = proc_text[:-1]
	proc_text = '[' + proc_text + ']'
	with open(jsonfile,'w') as text_file:
		text_file.write(proc_text)
 
process_ds_conn('UpdateDS.json')
process_ds_conn('UpdateConnection.json')
process_proc('Procedure.json')
