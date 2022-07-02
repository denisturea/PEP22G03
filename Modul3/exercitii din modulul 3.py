#Exercitiu 1
# income = float(input("Enter the annual income: "))
# # Write your code here.
# if income <= 85528:
#     tax = (income * 18/100) - 556.2
# elif income > 85528:
#     tax = ( 14839.2 + (income-85528)*32/100)
# else:
#     print('Suma Incorecta')
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

#Exercitiu 2
# year = int(input("Enter a year: "))
#
# if year // 4 == 1:
#     print("THis is a common year")
# elif year // 100 == 1:
#     print('This is leap year')
# elif year // 400 == 1:
#     print('This is a common year')
# else:
#     print('This is a leap year')


#Exercitiu 3
#
# A)
# secret_number = 7
# a = True
#
# while a:
#     numar_ales = int(input("Alege-ti numraul norocos:"))
#     if numar_ales != secret_number:
#         print('Haha you are stuck in my loop:')
#         continue
#     a = False
#
# print("Well done, muggle! You are free now.")

# B)
# secret_number = 777
#
# sn = int(input("input here:"))
#
# while sn != secret_number:
#     print("Haha you stuck in my loop")
#     sn = int(input("input here:"))
#
# print("You are out of the loop")

#Exercitiul 4
import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.
# for mis in range(1,6):
#     x= [1,2,3,4,5,6]
#     print(f'{mis} Mississippi')
#     time.sleep(1)

#Exercitiul 5
# cuv= "chupacabra"
# secret = input('Alege cuvantul secret: ')
#
# while secret:
#     if secret == cuv:
#         break
#     secret = input('Alege cuvantul secret: ')
# print('You ve successfully left the loop. ')
#

#Exercitiul 6

# word = input('Introdu-ce-ti cuvantul: ').upper()
# for litera in word:
#     if litera in 'A':
#         continue
#     elif litera in "E":
#         continue
#     elif litera in "I":
#         continue
#     elif litera in "O":
#         continue
#     elif litera in "U":
#         continue
#     print(litera)

#Exercitiul 7
# nou=""
# char = 'AEIOU'
# word = input('Introdu-ce-ti cuvantul: ').upper()
# for litera in word:
#     if litera in char:
#         continue
#     elif litera != char:
#         nou += litera
#
# print(nou)

# Exercitiul 7
# block = int(input('Number of blocks: '))
# layers = 1
# height = 0
# while layers <= block:
#     height +=1
#     block -= layers
#     layers += 1
# print("The height the pyramid is: ", height)

c0 = int(input("Introdu numarul: "))
step =0
while c0 !=1 and c0 > 0:
    if c0%2==0:
        c0 = c0// 2
        print(c0)
        step += 1
    elif c0%2==1:
        c0=3*c0+1
        print(c0)
        step +=1
    continue
print("A fost necesat sdas:", step)
