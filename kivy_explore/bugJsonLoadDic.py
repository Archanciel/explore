import json

dic = {}

dic[str(1)] = {}
dic[str(1)][1] = 'one_one'
dic[str(1)][2] = 'one_two'

# saving dic to file
with open("dic_saved.txt", 'w') as f:
	try:
		json.dump(dic,
		          f,
		          indent=4,
		          sort_keys=True)
	except Exception as e:
		print(e)

reloaded_dic = None

# loading dic from file
try:
	with open("dic_saved.txt", 'r') as f:
		reloaded_dic = json.load(f)
except Exception as e:
	print(e)

print(reloaded_dic)