import xml.etree.ElementTree as etree
import re
import os
from dictdiffer import diff, patch, swap, revert
from dictdiffer.utils import dot_lookup

# def get_proc_aardvark_column_dic():
# 	proc_aardvark_column_dic = {}
# 	for file in os.listdir("xmlfiles1"):
# 		if file.lower().startswith('sqlserver_spotlight'):
# 			filename = file[file.index('-')+1:file.index('.')]
# 			proc_name = 'xmlfiles\\SQLServer_SpotLight-'+ filename + '.xml'
# 			tree = etree.parse(proc_name)
# 			root = tree.getroot()
# 			column_names = []
			
# 			for column in root.iter('procedureColumn'):
# 				if column.attrib['sentToProjectLucy'] == 'true':
# 					column_names.append(column.attrib['name'])
# 			if column_names:
# 				proc_aardvark_column_dic[filename] = column_names
# 	return(proc_aardvark_column_dic)

# print(get_proc_aardvark_column_dic())


# proc_advard = {'HealthCheckDatabaseBackups': ['backup_finish_date', 'backup_set_id', 'backup_set_uuid', 'backup_size', 'backup_start_date', 'begins_log_chain', 'catalog_family_number', 'catalog_media_number', 'checkpoint_lsn', 'code_page', 'collation_name', 'compatibility_level', 'compressed_backup_size', 'database_backup_lsn', 'database_creation_date', 'database_guid', 'database_id', 'database_name', 'database_version', 'description', 'device_type', 'diagnostic_server', 'differential_base_guid', 'differential_base_lsn', 'expiration_date', 'family_guid', 'family_sequence_number', 'first_family_number', 'first_lsn', 'first_media_number', 'first_recovery_fork_guid', 'flags', 'fork_point_lsn', 'has_backup_checksums', 'has_bulk_logged_data', 'has_incomplete_metadata', 'instance', 'instance_start_time_utc', 'is_copy_only', 'is_damaged', 'is_force_offline', 'is_password_protected', 'is_readonly', 'is_single_user', 'is_snapshot', 'last_family_number', 'last_lsn', 'last_media_number', 'last_recovery_fork_guid', 'logical_device_name', 'machine_name', 'media_count', 'media_family_id', 'media_set_id', 'mirror', 'mtf_minor_version', 'name', 'physical_block_size', 'physical_device_name', 'position', 'recovery_model', 'rownum', 'server_name', 'service', 'software_build_version', 'software_major_version', 'software_minor_version', 'software_vendor_id', 'sort_order', 'time_zone', 'type', 'unicode_compare_style', 'unicode_locale', 'user_name']}
# proc_cloud =  {'HealthCheckDatabaseBackups': [ 'backup_set_id', 'backup_set_uuid', 'backup_size', 'backup_start_date', 'begins_log_chain', 'catalog_family_number', 'catalog_media_number', 'checkpoint_lsn', 'code_page', 'collation_name', 'compatibility_level', 'compressed_backup_size', 'database_backup_lsn', 'database_creation_date', 'database_guid', 'database_id', 'database_name', 'database_version', 'description', 'device_type', 'diagnostic_server','differential_base_guid', 'differential_base_lsn', 'expiration_date', 'family_guid', 'family_sequence_number', 'first_family_number', 'first_lsn', 'first_media_number', 'first_recovery_fork_guid', 'flags', 'fork_point_lsn', 'has_backup_checksums', 'has_bulk_logged_data', 'has_incomplete_metadata', 'instance', 'instance_start_time_utc', 'is_copy_only', 'is_damaged', 'is_force_offline', 'is_password_protected', 'is_readonly', 'is_single_user', 'is_snapshot', 'last_family_number', 'last_lsn', 'last_media_number', 'last_recovery_fork_guid', 'logical_device_name', 'machine_name', 'media_count', 'media_family_id', 'media_set_id', 'mirror', 'mtf_minor_version', 'name', 'physical_block_size', 'physical_device_name', 'position', 'recovery_model', 'rownum', 'server_name', 'service', 'software_build_version', 'software_major_version', 'software_minor_version', 'software_vendor_id', 'sort_order', 'time_zone', 'type', 'unicode_compare_style', 'unicode_locale', 'user_name']}
# dot_lookup(proc_advard['HealthCheckDatabaseBackups'], proc_cloud['HealthCheckDatabaseBackups'])
# result = diff(proc_advard, proc_cloud)
# print(list(result))

# proc_aardvark_column_dic = {}
# for file in os.listdir("xmlfiles1"):
# 	if file.lower().startswith('sqlserver_spotlight'):
# 		filename = file[file.index('-')+1:file.index('.')]
# 		proc_name = 'xmlfiles1\\SQLServer_SpotLight-'+ filename + '.xml'
# 		tree = etree.parse(proc_name)
# 		root = tree.getroot()
# 		column_names = []
# 		column_name = []
		
# 		for column_backgroup in root.iter('component'):
# 			column_name.append(column_backgroup.attrib)
# 			#print(column_name[0]['alwaysSaveToLucy'])
# 			alwaysSaveToLucy = column_name[0]['alwaysSaveToLucy']
# 		#print(alwaysSaveToLucy)

# 		for column_oopcollect in root.iter('procedureColumn'):
# 			#print(column_oopcollect.attrib['sentToProjectLucy'])
# 			if column_oopcollect.attrib['sentToProjectLucy'] == 'true' or 'alwaysSaveToLucy' == alwaysSaveToLucy: 
# 				column_names.append(column_oopcollect.attrib['name'].lower())
# 		if column_names:
# 			proc_aardvark_column_dic[filename] = sorted(column_names)

# print(proc_aardvark_column_dic)

proc_aardvark_column_dic = {}
for file in os.listdir("xmlfiles1"):
	if file.lower().startswith('sqlserver_spotlight'):
		filename = file[file.index('-')+1:file.index('.')]
		proc_name = 'xmlfiles1\\SQLServer_SpotLight-'+ filename + '.xml'
		tree = etree.parse(proc_name)
		root = tree.getroot()
		column_names = []
		column_name = []
		for column_backgroup in root.findall(".//component[@class='com.quest.adk.configuration.component.ProcedureScheduleComponent']"):
			print(column_backgroup.attrib['enabled'])
			

		# for column_oopcollect in root.iter('procedureColumn'):
		# 	if column_oopcollect.attrib['sentToProjectLucy'] == 'true' or 'alwaysSaveToLucy' == alwaysSaveToLucy: 
		# 		column_names.append(column_oopcollect.attrib['name'].lower())
		# if column_names:
		# 	proc_aardvark_column_dic[filename] = sorted(column_names)		

