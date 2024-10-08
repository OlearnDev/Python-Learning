nom = "John"  
prenom = "Lys"  
nom_complet = prenom + " " + nom  #--> Lys John
age=14

#chaine="{} {} a actuellement {} ans".format(prenom, nom, age)

chaine=f"{prenom} {nom} a actuellement {age} ans"
print(chaine)

def somme(*args):return sum(args)

s=somme(1,2,3)
print(str(s))

def create_dict(**args): print(args)

s=create_dict(nom="Jean", age=14, job="Devops")

print(s)