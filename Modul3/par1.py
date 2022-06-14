#EX1 IF,ELIF,ELSE
# my_age = 25
# if my_age >= 18:
#     print("Esti Adult")
# elif my_age >= 13:
#     print()
# elif my_age >= 0:
#     print("Esti copil")
# else:
#     print("Numerele negative nu sunt permise")
# print("Done")

# Ex 2 while

# a= ""
# b= 3
# if a:
#     print(b)
# else:
#     print(a)
# print(a and b)

# if a:
#     print(a)
# else:
#     print(b)
# print(a or b)

#Ex3 conditie
# a= "a"
# b= "b"
#
# print(a and b)
# print(bool(a and b))
# print(bool(a))

#Problema 1

# my_cnp= input("Introdu primele 7 cifre din cnp: ")
# anul_nasterii=int(my_cnp[1:3])
# anul_curent=2022
# if int(my_cnp[0])>2:
#     anul_nasterii+=2000
# else:
#     anul_nasterii+=1900
# print(anul_nasterii)
#
# if anul_curent-anul_nasterii>18:
#     print("Esti major")
# else:
#     print("Esti minor")

#Problema 2
# numar= int(input("Alege un Numar: "))
# inceput =0
# while inceput <= numar:
#     inceput +=2
#     print(inceput)
#     if inceput == numar:
#         break
#
#
# print('Done')

#WHILE
# depends_on = 1
# while depends_on !=2 :
#     print('Running')
# depends_on = 2
# print('Done')

#Problema 3
optiuni = input('Cappucino......4 lei\nExpreso......3.5lei\nCe optiune alegeti?:[1,2]:')
bani = int(input("Introduceti bancnota [5,10]:"))
var1= '1'
var2= '2'
ban = 5
ban1 = 10
pret1 =4
pret2 = 3.5
if optiuni == var1 and bani == (ban or ban1) :

    print("Vei primi restul de:",bani- pret1 )
elif optiuni== var2 and bani == (ban or ban1):

    print("Vei primi restul de:",bani- pret2 )
# elif optiuni != (var1 and var2):
#     print("Alegere gresita!")
else:
    print('Alegere gresita!')