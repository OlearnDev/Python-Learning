dictionnaire = [
    "test",
    "vie",
    "aimer",
    "secret",
    "mystere",
    "cacher"
]

mot = dictionnaire[3]
mot_len = len(mot)
mystere =""
loop = True


for i in range(mot_len):
    if i%2 == 0:
        mystere +=mot[i]
    else:
        mystere +="*"
        
while loop:
    print(mystere)         
    mot_utilisateur = input(f"Quel est le mot caché ? ")

    if not len(mot_utilisateur) == mot_len:
        print(f"Désolé, vous devez entrer un mot contenant {mot_len} caractères ! ")
    else:
        if mot_utilisateur != mot:
            mystere_backup = mystere
            mystere =""
            for i in range(mot_len):
                if mot_utilisateur[i] == mot[i]:
                    if i>0:
                        if mot[i-1]==mot_utilisateur[i-1]:
                            mystere += mot[i]
                        else:
                            mystere += mystere_backup[i]
                    else:
                        mystere += mystere_backup[i]
                else:
                    mystere += mystere_backup[i]
            print(f"Désolé, le mot entré ne correspond pas !")
        else:
            print(f"Félicitation, vous avez trouvé le mot caché : {mot}")
            loop = False