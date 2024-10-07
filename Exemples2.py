
# for i in range(10):
#      print((i+1)**2)
    
# l=["Ted", 34, True, range(15)]

# print(l)

# print(l[0])

# for i in l:
#     if type(i) == str:
#         print(i.upper())
#     elif type(i) == int:
#         print(i**2)
#     else:
#         print(i)

def func_hello(nom, age=-1):  #age est une var optionnelle dans ce cas. On peut mettre age=None
    if age:
        print(f"Bonjour {nom} vous avez {age} ans !")
    else:
        print(f"Bonjour {nom} !")

func_hello ("John")
func_hello ("John", 14)             #Passage ordonné d'arguments
func_hello (age=17, nom="Pru")      #Passage nommé d'arguments

princesse = ("Marie", 11)
func_hello(*princesse)              #Unpacking : Passage des arguments d'une liste

princesse = ["Marie", 11]
func_hello(*princesse) 

dict_child={"nom":"Marie", "age":11}    #Dictionnaire :  formé de clé:valeur 
func_hello(**dict_child)                #La clé doit correxpondre au nom de la var dans la fonction

#---------  Return 1 seul élément
def func_hello(nom, age=-1):  #age est une var optionnelle dans ce cas. On peut mettre age=None
    result = None
    if age:
        result = f"Bonjour {nom} vous avez {age} ans !"
    else:
        result = f"Bonjour {nom} !"
    return result

print(func_hello ("John"))
dict_childr=func_hello(**dict_child)
print(dict_childr)

#---------  Return 2 éléments

def func_hello(nom, age=-1):  #age est une var optionnelle dans ce cas. On peut mettre age=None
    result = None
    majeur = False
    if age:
        result = f"Bonjour {nom} vous avez {age} ans !"
        if age>=18:
            majeur = True
    else:
        result = f"Bonjour {nom} !"
    return (result,majeur)
    #return result,majeur   NB: On peut enlever les () dans le tuple de retour

dict_childr=func_hello(**dict_child)
print(dict_childr)