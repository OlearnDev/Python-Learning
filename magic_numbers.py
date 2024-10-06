import random

val_min = 10
val_max = 100
NB_CHANCE = 10

mystere = random.randint(val_min,val_max)

essai = 1
score = 100
essai_restant = NB_CHANCE

loop = True
loop2 = True
while loop:
    
    valeur_utilisateur = input(f"Veuillez entrer une valeur comprise entre {val_min} et {val_max} ! (Nb essais restants : {essai_restant} ) --> ")
    valeur_int = int(valeur_utilisateur)

    if 10<=valeur_int<=100:
        
        if essai < NB_CHANCE:
                if valeur_int > mystere:
                    print("Plus grand que le nombre mystere")
                    essai += 1
                    score -= 10
                    essai_restant -= 1
                elif valeur_int < mystere:
                    print("Plus petit que le nombre mystere")
                    essai += 1
                    score -= 10
                    essai_restant -= 1
                else:
                    print(f"Felicitation vous avez trouvé le nombre mystere, le nombre mystere est {valeur_int}")
                    print(f"Nombre d'essais : {essai} \nScore : {score}")
                    loop = False
        else:
                loop = False
                print(f"Désolé, nombre maximal de tentatives atteint ! Le nombre mystere était {mystere}")
                
            
            