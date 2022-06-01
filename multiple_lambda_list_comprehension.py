intLst = [1, 2, 3]
f1 = lambda x: x
f2 = lambda x: x * 10
newLst = [f(x) for x in intLst for f in [f1, f2]]

print(newLst) # [1, 10, 2, 20, 3, 30]

