import random
lower = 'abcdefghijklmnopqrstuvxwyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%&*-:;'
tg = lower + upper + numbers + symbols
lenght = 16
password = "".join(random.sample(tg,lenght))
print(password)
