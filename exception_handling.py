monDictionnaire = {'clef1': 1, 'clef2': 2, 'clef3': 3}

def maFonctionSansTraitementKeyError(dictionnaire, clef):
	valeur = dictionnaire[clef]
	
	return valeur

def maFonctionAvecTraitementKeyError(dictionnaire, clef):
	valeur = None # la variable doit être définie avec une valeur par défaut
	
	try:
		valeur = dictionnaire[clef]
	except KeyError as e:
		print(e)
		print("code ici ce que ton programme doit faire en cas d'erreur ou de timeout ...")
	
	return valeur
	
print('valeur: ', maFonctionAvecTraitementKeyError(monDictionnaire,'clef4'))
print()
print('valeur: ', maFonctionSansTraitementKeyError(monDictionnaire, 'clef4'))