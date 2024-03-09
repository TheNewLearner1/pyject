import matplotlib.pyplot as plt
z = list(range(150, 200))
y = []
for x in z:
    x *= x
    y.append(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(z, y)
plt.show()