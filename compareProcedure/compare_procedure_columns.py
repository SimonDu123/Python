import json
from pprint import pprint
from os import listdir
from os.path import isfile, join

mypath = "SQLServer_Spotlight\\"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)
# for files in onlyfiles:
# 	with open(mypath + files) as data_file:    
# 	    data = json.load(data_file)

# for each in data['Columns']:
# 	print(each['Name'])
	
with open('SQLServer_Spotlight\\FragmentationOverview.json') as data_file:
	data = json.load(data_file)
	print(data)
# for files in onlyfiles:
# 	print(mypath+files)