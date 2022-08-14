from primePy import primes
import random

def fun(x, y):
    if primes.check(x) == True and primes.check(y) == True:
        if x < y:
             z = random.randint(2, y)
             return (x ^ z) % y
        else:
            print("Valoarea lui x trebuie sa fie mai mica ca si valoarea lui y: \n")
    else:
        print("Nu s-au introdus numere prime")

x = int(input("Introduceti valoarea lui x: \n "))
y = int(input("Introduceti valoarea lui y: \n "))
print(fun(x, y))