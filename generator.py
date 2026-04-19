import random
import string
import pyperclip

print("Generatore di Password")

print("inserisci il minimo")
min = int(input())

print("inserisci il massimo")
max = int(input())

random.randint(min,max)

l = random.randint(min,max)

c = string.ascii_letters + string.digits + string.punctuation

p = ''.join(random.choices(c, k=l))

print("password generata! ",p)

pyperclip.copy(p)

# print(pyperclip)
# print(random)
# print(string)