import re

playlistNamePattern = r'([a-zaA-Z_]+)([\(se\d:\- \)]*)'
timeGroupPattern = r'(\([se\d:\- ]*\) ?)'
timeInfoPattern = r'([\dsSeE:-]*)'

text = 'The_playlist (s01:05:52-01:07:23 e01:15:52-01:17:23 e01:15:52-01:17:23) (s1:05:52-1:07:23)'


def extractTimeInfo(pattern, subPattern, text):
	i = 1
	for match in re.finditer(pattern, text):
		for subGroup in match.groups():
			print('subgroup {} '.format(i), subGroup)
			for mat in re.finditer(subPattern, subGroup):
				for subGro in mat.groups():
					print(subGro)
		i += 1
					


match = re.match(playlistNamePattern, text)

print(match.group(1), '\n')
#print(match.group(2))
extractTimeInfo(timeGroupPattern, timeInfoPattern, match.group(2))