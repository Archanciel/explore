def f(k, x):
    return (k * (x ** 2)) - 1

print(f(1, 2))

x1 = 0.987654321
x2 = 0.987654322

k = 2

for i in range(50):
    x1 = f(k, x1)
    x2 = f(k, x2)
    print("{0}:\t{1:0.10f}\t{2:0.10f}".format(i + 1, x1, x2))
