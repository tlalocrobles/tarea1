import random
caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
x=int(input("De cuantos caracteres quieres tu contraseña?"))
z=""
for i in range (x):
    z+=random.choice(caracteres)
print (z)
