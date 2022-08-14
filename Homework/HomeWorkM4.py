# #Ex1
#
# def fun(x):
#     y = 3 * x
#     rez = 3 * x ** 2 - 4 * y + 4
#     print("============= X = {}  ==================".format(x))
#     print("============= Y = {}  ==================".format(y))
#     print("Rezultatul functiei : {}".format(rez))
#
# for a in range(10, 21):
#     fun(x=a)
#
# #Ex:2

nr = input("Cati carti doriti sa adaugati in biblioteca?: \n ",  )
lista_carti = []
for i in range(int(nr)):
    nume_carte = input("Numele cartii:")
    nume_autor = input("Numele autorului:")
    anul_publicarii = input("Anul publicarii:")
    dict = {'nume':nume_carte, 'autor':nume_autor, 'an':anul_publicarii}
    lista_carti.append(dict)

print("Cartile dvs sunt:")
for i in range(len(lista_carti)):
    print(lista_carti[i])
# #Ex:3

publicatie = input("Introduce-ti anul: \n")
carti = []
carti_selectate = []
for x in range(len(lista_carti)):
    my_dict = lista_carti[x]
    if my_dict['an'] > publicatie:
        carti.append(my_dict['nume'])
for y in range(len(carti)):
    carti_selectate.append(carti[y])
for carte in carti_selectate:
    print(f"{carte} a fost publicat dupa {publicatie}")
