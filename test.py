# # # https://github.com/kevinniel/Python-Lessons/wiki/1---variables
# # #1
# # # a = 5
# # # print(a)

# # # #2/3
# # # age = 18
# # # prenom = "JM"
# # # print("Je suis", prenom, " et j'ai", age, "ans")

# # # #4
# # # b = 10
# # # c = b*4
# # # print(c)

# # # #5
# # # d = 5
# # # d = d + 2 - 1
# # # print(d)
# # # d = d + 1
# # # print(d)

# # # #6

# # # d = 5
# # # d = d -2 +1 
# # # print(d)
# # # d = d - 1
# # # print(d)

# # # #7

# # # #8

# # # #9
# # # a = 5
# # # b = 10
# # # c = a
# # # a = b
# # # b = c
# # # print(a, b)

# # # #10
# # # a = 2
# # # b = 5
# # # c = 11
# # # a = a * 5
# # # b = b + 5
# # # c = c - 1
# # # print(a, b, c)

# # # #11
# # # a = 10
# # # print(a)
# # # a = a / 2
# # # print(a)
# # # a = a // 2
# # # print(a)
# # # a = a / 2
# # # print(a)
# # # a = a*a*a
# # # print(a)

# # # #12
# # # HT = int(input("Entrer le prix HT"))
# # # nbart = int(input("Entrer le nombre d'article"))
# # # TVA = 1.2
# # # prixfinal = (HT * nbart) * TVA
# # # print(prixfinal)

# # #Les Listes

# # #13
# # liste = [4, 5]
# # print(liste)

# # #14
# # liste1 = ["Je", "suis", 18, 20]
# # print(liste1)
# # print(liste1[0])
# # print(liste1[2])

# # #15
# # x = [5, 10]
# # y = [15, 20]
# # z = x + y
# # print(z)

# # #16
# # x = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9]
# # print(x[3])
# # print(x[3], x[4])
# # for i in range (2,7, 2) :
# #     print(x[i])
# # print(len(x))
# # minimum = 0
# # maximum = 0
# # somme = 0
# # for i in range (0, 9) :
# #     if   x[i] < minimum :
# #         minimum = x[i]
# #     if x[i] > maximum :
# #         maximum = x[i]
# #     somme = somme + x[i]

# # print("Le minimum est",minimum)
# # print("Le maximum est", maximum)
# # print("La somme totale est :", somme)

# # del x[3]
# # del x[4]
# # print(x)

# # #17
# # x = ["ok", 4, 2, 78, "bonjour"]
# # print(x[3])
# # x[1] = "toto"
# # print(x)

# # #18
# # l1 = [0, 1, 2, 3, 4, 5]
# # l2 = []

# # for i in range (0,6) :
# #     l2 += [i]    
# # print(l2)

# # #19
# # x= {
# #      "key":"valeur",
# #      "key2":"valeur2" 
# # }
# # print(x["key"])

# # x["titi"] = "toto"
# # print(x)
# # x["tata"] = x["titi"]
# # print(x)
# # del x["titi"]
# # print(x)
# # key = x["key"]
# # del x["key"]
# # print(key)
# # print(x)
# # y= x
# # print("Dictionnaire y : ",y)

# #20
# x = [("x", "y"), ("x", "y"), ("x", "y"), ("x", "y")]
# print(x)
# x.append("a")
# print(x)
# x.extend("b")
# print(x)
# y = [1, 2, 3]
# x = x + y
# print(x)
# x.insert(4, 2)
# print(x)
# del x[4]
# print(x)
# print(y)
# z = y
# print(z)
# del y[:]
# print(y)

# #2 TEST

# #1
# # a= int(input("Entrer le premier nombre"))
# # b= int(input("Entrer le deuxième nombre"))
# # c = a*b
# # if c > 0 :
# #     print("positif")
# # elif c < 0 :
# #     print("Négatif")
# # else :
# #     print("nul")


# # #2
# # age = int(input('quel est ton age'))
# # if age > 18 :
# #     print("majeur")
# # else :
# #     print("mineur")

# # #3
# # nb = int(input("donne un nombre"))
# # if nb == 6 or nb == 7 or nb == 8 or nb == 9 :
# #     print("Vrai")
# # else :
# #    print("Faux")

# # nb = int(input("donne un nombre"))
# # if nb >5 and nb <10 :
# #     print("Vrai")
# # else :
# #     print("Faux")

# #3 BOUCLES

# #1
# # for i in range (0, 6) :
# #     print(i)

# #2
# liste = ["Je", "suis", "JM"]
# for element in liste :
#     print(len(element))

#3
# x = "anticonstitutionnellement"
# for i in range (len(x)) :
#     print(x[i])

#4
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(x)


#5
# x = [1,10,20,30,40,50]
# a = 0
# b = 0
# for i in range (len(x)) :
#     a = a + x[i]
# print(a)
# for element in x :
#     b = b + element
# print(b)

# #6
# for i in range (5, -1, -1) :
#     print(i)

# #7
# for i in range(1, 10) :
#     if i > 3 :
#         break
#     else : 
#         print(i) 

#8
# for i in range (1,10) :
#     a 

#9

#10
# i =0
# ordi = ["apple", "asus", "dell", "samsung"]
# while i < (len(ordi)) :
#     print(ordi[i])
#     i = i + 1

#11
# text = input("Ecire un mot")
# while text != "exit" :
#     text = input("Ecrire un mot")
# print(text)

#12
# i = 0
# while i <=100 :
#     print(i)
#     i = i + 5

#4 FONCTIONS

#1
# def fct(nb,) :
#     print(nb*5)
# fct(10) 

#2

# def fct(nb) :
#     if nb%2 == 0 :
#         print("pair")
#     else :
#         print("pas pair")

# fct(15)

#3


# def fiba(nb,) :
#     n1 = 0
#     n2 = 1
#     for i in range(2, nb):
#         suivant = n1 + n2
#         print(suivant, end=", ")
#         n1 = n2
#         n2 = suivant
# fiba(20)

4#
def voy(mot) :
    liste_voyelles=["a","e","i","o","u","y"]
    nb_voyelles = 0
    for lettre in mot : 
        if lettre in liste_voyelles :
            nb_voyelles+=1
    print(nb_voyelles)

voy("azerty")

#5
def factor(nb) :
    while nb != 1 :
        nb = nb*(nb-1)


  

    










