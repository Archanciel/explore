import re

partialDate_date_only_1 = '-d12'
partialDate_date_only_2 = '-d11/1'
partialDate_date_only_3 = '-d02/10/20'
partialDate_date_only_4 = '-d2/02/2021'
partialDate_date_time_1 = '-d12 08:45'
partialDate_date_time_2 = '-d12/11 8:05'
partialDate_date_time_3 = '-d02/08/21 18:45'
partialDate_date_time_4 = '-d2/5/2021 08:45'
partialDate_date_time_5 = '-d2/5/2021 08:45 -ebittrex'

# the idea is to order the 'or' dateTimePatterns, placing the most restrictive (for
# '-d2/5/2021 08:45' or '-d02/08/21 18:45' --> "^-d(\d+/\d+/\d+ \d+:\d+)") in first
# position in the pattern definition
dateTimePattern = r"^-d(\d+/\d+/\d+ \d+:\d+)|^-d(\d+/\d+ \d+:\d+)|^-d(\d+ \d+:\d+)|^-d(\d+/\d+/\d+)|^-d(\d+/\d+)|^-d(\d+)"

def doPrintRegexpResults(pattern, strToParse):
	print(strToParse)
	
	for grps in re.finditer(pattern, strToParse):
		print(grps.groups())
		for elem in grps.groups():
			if elem is not None:
				print(elem)
			
	print()

doPrintRegexpResults(dateTimePattern, partialDate_date_only_1)
doPrintRegexpResults(dateTimePattern, partialDate_date_only_2)
doPrintRegexpResults(dateTimePattern, partialDate_date_only_3)
doPrintRegexpResults(dateTimePattern, partialDate_date_only_4)
doPrintRegexpResults(dateTimePattern, partialDate_date_time_1)
doPrintRegexpResults(dateTimePattern, partialDate_date_time_2)
doPrintRegexpResults(dateTimePattern, partialDate_date_time_3)
doPrintRegexpResults(dateTimePattern, partialDate_date_time_4)
doPrintRegexpResults(dateTimePattern, partialDate_date_time_5)
