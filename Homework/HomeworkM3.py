# Problema 1:
# lista = ['abc',123,'1',1]
# counteri=0
# counterf=0
# counterlis=0
# counters= 0
# for obiect in lista:
#     print(f"Tipul obiectului {obiect} este {type(obiect).__name__}. ")
#
#     if type(obiect) == int:
#         counteri += 1
#     elif type(obiect) == str:
#         counters +=1
#
#     elif type(obiect) == float:
#         counterf += 1
#     elif type(obiect)== list:
#         counterlis +=1
# print(f"Sunt {counteri} obiecte de timp integer.")
# print(f"Sunt {counters} obiecte de tip string.")
# print(f"Sunt {counterf} obiecte de tip float.")
# print(f"Sunt {counterlis} obiecte de tip lista.")

#Problema 2

sir = list(input("Alege-ti un sir:"))

print(list)
counter = 0
for char in sir:
    if char in "aeiouAEIOU":
        counter +=1
print("Numarul vocalelor din lista este:", counter)