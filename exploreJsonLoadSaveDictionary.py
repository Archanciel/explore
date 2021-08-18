import json

CONTACT_NAME_KEY = 'name'
CONTACT_EMAIL_KEY = 'email'
CONTACT_PHONE_NUMBER_KEY = 'phoneNumber'

items = [{CONTACT_NAME_KEY: 'Jean-Pierre Schnyder', CONTACT_EMAIL_KEY: 'jp.schnyder@gmail.com',
          CONTACT_PHONE_NUMBER_KEY: '+41768224987'},
         {CONTACT_NAME_KEY: 'Tamara Jagne', CONTACT_EMAIL_KEY: 'tamara.jagne@gmail.com',
          CONTACT_PHONE_NUMBER_KEY: '+41764286884'}
         ]

dic = {}
i = 1

for item in items:
	strKey = str(i)
	dic[strKey] = item
	i += 1

# saving dic to file
with open("contact_dic_saved.txt", 'w') as f:
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
	with open("contact_dic_saved.txt", 'r') as f:
		reloaded_dic = json.load(f)
except Exception as e:
	print(e)

print(reloaded_dic)