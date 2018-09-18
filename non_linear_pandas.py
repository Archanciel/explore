import pandas as pd
import matplotlib.pyplot as plt

def f(k, x):
    return (k * (x ** 2)) - 1


x1 = 0.987654321
x2 = 0.987654322
cols = ['x=' + str(x1), 'x=' + str(x2)]
k = 2
t = 50
idx = [x + 1 for x in range(t)]

data = []

for i in range(t):
    x1 = f(k, x1)
    x2 = f(k, x2)
    data.append([x1, x2])

nldf = pd.DataFrame(data, index=idx, columns=cols)
nldf.plot()
plt.show()