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

proc_aardvark_column_dic = {}

for file in os.listdir("xmlfiles"):
	if file.lower().startswith('sqlserver_spotlight'):
		sql_proc = file[file.index('-')+1:file.index('.')]
		proc_name = 'xmlfiles\\SQLServer_SpotLight-'+ sql_proc + '.xml'
		tree = etree.parse(proc_name)
		root = tree.getroot()
		column_names = []
		column_name = []

		for column_oopcollect in root.iter('procedureColumn'):
			column_names.append(column_oopcollect.attrib['name'].lower())
			proc_aardvark_column_dic[sql_proc] = sorted(column_names)	
		print(proc_aardvark_column_dic)
	
