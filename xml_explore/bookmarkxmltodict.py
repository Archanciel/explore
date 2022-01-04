from abc import ABCMeta, abstractmethod

import json
import os
from os.path import sep
import xmltodict

class BookmarkDic(metaclass=ABCMeta):
	@staticmethod
	def _loadDicIfExist(dicFilePathName):
		"""
		If a file containing the dictionary data for the corresponding playlist
		exists, it is loaded using json.

		:param dicFilePathName:

		:return None or loaded dictionary
		"""
		dic = None
		
		if os.path.isfile(dicFilePathName):
			with open(dicFilePathName, 'r',  encoding='UTF-8') as f:
				xmlData = f.read()
				
			# avoiding a parsing error ...
			xmlData = xmlData.replace('&#', '\\ud')
			
			dic = xmltodict.parse(xmlData)
				
		return dic

if __name__ == '__main__':
	bookmarkXmlFileName = 'bookmarks.sabp.xml'
	bookmarkDic = BookmarkDic._loadDicIfExist(bookmarkXmlFileName)
	a = 1