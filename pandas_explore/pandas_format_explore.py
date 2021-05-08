import pandas as pd

df = pd.DataFrame({'Unit': ['Bit', 'Nibble','Byte/Octet', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte'],
				   'Abbreviation': ['b', '-', 'B', 'KB', 'MB', 'GB', 'TB'],
				   'Storage': ['Binary digit, single 0 or 1', '4 bits', '8 bits', '1024 bytes', '1024 KB', '1024 MB', '1024 GB'],
				   'Value': [21,34,23,65,45,13,87],
				   'Percent': [1,2,3,4,5,6,7]})

dfCopy = df.copy()

print('df')
print(df)
print()

df.style.format("{:.2f}", subset=pd.IndexSlice[:,['Value']]) \
		.format("{:.2%}", subset=pd.IndexSlice[:,['Percent']])
df.style.bar(subset=['Abbreviation'], align='mid', color=['#d65f5f'])

print('df after setting style')
print(df)


dfCopy.style.format("{:.2f}", subset=pd.IndexSlice[:,'Value']) \
			.format("{:.2%}", subset=pd.IndexSlice[:,'Percent'])
dfCopy.style.bar(subset=['Abbreviation'], align='mid', color=['#d65f5f'])

print('\ndfCopy after setting style')
print(dfCopy)

# OUTPUT
'''
df
		 Unit Abbreviation                      Storage  Value  Percent
0         Bit            b  Binary digit, single 0 or 1     21        1
1      Nibble            -                       4 bits     34        2
2  Byte/Octet            B                       8 bits     23        3
3    Kilobyte           KB                   1024 bytes     65        4
4    Megabyte           MB                      1024 KB     45        5
5    Gigabyte           GB                      1024 MB     13        6
6    Terabyte           TB                      1024 GB     87        7

df after setting style
		 Unit Abbreviation                      Storage  Value  Percent
0         Bit            b  Binary digit, single 0 or 1     21        1
1      Nibble            -                       4 bits     34        2
2  Byte/Octet            B                       8 bits     23        3
3    Kilobyte           KB                   1024 bytes     65        4
4    Megabyte           MB                      1024 KB     45        5
5    Gigabyte           GB                      1024 MB     13        6
6    Terabyte           TB                      1024 GB     87        7

dfCopy after setting style
		 Unit Abbreviation                      Storage  Value  Percent
0         Bit            b  Binary digit, single 0 or 1     21        1
1      Nibble            -                       4 bits     34        2
2  Byte/Octet            B                       8 bits     23        3
3    Kilobyte           KB                   1024 bytes     65        4
4    Megabyte           MB                      1024 KB     45        5
5    Gigabyte           GB                      1024 MB     13        6
6    Terabyte           TB                      1024 GB     87        7
'''