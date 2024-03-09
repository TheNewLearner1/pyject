import matplotlib.pyplot as plt
z = [1,2,3,4,5]
y = []
for x in z:
    x *= x*x*x*x*x*x*x
    y.append(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(z, y)
plt.show()