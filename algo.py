#Tri liste

# import random
# list1=[]
# a=0
# max=20
# list1=[max]
# while a < max:
#     list1.append(random.randint(1,50))
#     a += 1

# stockage = 0


	
# permute = True
# while permute == True :
#     permute = False
#     for i in range (0,20) :
#         if list1[i] > list1[i+1] :
#             stockage = list1[i]
#             list1[i] = list1[i+1]
#             list1[i+1] = stockage
#             permute = True

# print(list1)


#Tableau multidimentionnel

#ex 26

# a = 0

# tableau = []
# for i in range (0,6): 
#     for j in range (0,13) :
#         tableau[i][j] = a
#         a = a +1
        
# print(tableau)

tabl = []        
capacite = 63
redim tabl[63, 63]
val = 1
for i in range (0, capacité) :
    for j in range(0, capacite) :
        tabl[i][j] = val
        val = val*2
for i in range (0, capacite) :
    for j in range(0, capacite) :
        print(tabl[i][j])
       
      
    