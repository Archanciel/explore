n = 4
print('{} * {} subplots\n'.format(n, n))

for i in range(1, 5):
    for j in range(i + 1, 5):
        idx =  ((i - 1) * 3) + j - 1
        print(i, j, idx)

print('\n')

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        idx =  ((i - 1) * (n - 1)) + j - 1
        print(i, j, idx)

print('\n')

n = 5
print('{} * {} subplots\n'.format(n, n))

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        idx =  ((i - 1) * (n - 1)) + j - 1
        print(i, j, idx)

def subplotPos(classNumber):
    return ((i - 1) * (classNumber - 1)) + j - 1

print('\n')

n = 6
print('{} * {} subplots\n'.format(n, n))

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        idx = subplotPos(n)
        print(i, j, idx)
