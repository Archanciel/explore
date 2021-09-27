import json

# illegal filePathName containing ':'
#filePathName = "D:\\Development\Python\explore\\from_trans_file_cloud\\test short_n\'ame pl, aylist: avec deux points_dic.txt"
filePathName = "D:\\Development\Python\explore\\from_trans_file_cloud\\test short_n\'ame pl, aylist avec deux points_dic.txt"

dic = { 'one': 'un',
		'two': 'deux'}

with open(filePathName, 'w') as f:
	json.dump(dic,
	          f,
	          indent=4,
	          sort_keys=True)
	

