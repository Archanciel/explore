import numpy as np

lst1 = [2,3,4]
lst2 = [4,4.5,5]

matrix = np.array([lst1, lst2])
print('matrix')
print(matrix)
print(matrix[:,:-1])
print(matrix[:,:2])

vector1 = np.array(lst1)
vector2 = np.array(lst2.append(np.NaN))
print('\nvector1')
print(vector1)
print('vector2')
print(vector2)
print('vector 2 sum')
print(np.nansum(vector2))
print('((vector2 - vector1) / vector1) * 100')
print(((vector2 - vector1) / vector1) * 100)

