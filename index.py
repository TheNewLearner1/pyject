from numpy import random
chars = "`1234567890-=qwertyuiopasdfghjklzxcvbnm"
i = 0
m = 0
password = []
x = int(input("length of password: "))
while i < x:
    xo = random.randint(0, len(chars)-1)
    xoo = chars[xo]
    password.append(xoo)
    i += 1
while m < len(password):
    print(password[m], end="")
    m += 1
print('\n done')
