age=4

content = [
("Bébé Rockabye", "INCONNU", 0),
("Bébé des années 80", "Jammy Jams", 0),
("Les bébés deviennent Beatles","INCONNU", 0),
("Le Voyage de Chihiro", "Hayao Miyazaki", 1),
("Le Roi Lion", "Roger Allers et Rob Minkoff", 1),
("Aladin", "John Musker et Ron Clements", 1),
("One Piece", "Eiichiro Oda", 2),
("Death Note", "Tsugumi Ōba", 2),
("Fullmetal Alchemist", "Hiromu Arakawa", 2),
("OSS 117", "Michel Hazanavicius", 2),
(" La Descente","Neil Marshall", 4),
("La Ligne Rouge", "Terrence Malick", 4),
("Voyage au bout de l'enfer", "Michael Cimino",8),
("Persuasion", "Carrie Cracknell", 3),
("Livre d'Amour", "Analeine Cal y Mayor", 4)     
]

if age>=17:
    print("Vous etes adulte !")
    for item in content:
        if item[2]<=3:
            print(f"{item[0]} de {item[1]}")
elif 13<=age<=16:
    print("Vous etes adolescent !")
    for item in content:
        if item[2]<=2:
            print(f"{item[0]} de {item[1]}")
elif 16<=age<=12:
    print("Vous etes encore enfant !")
    for item in content:
        if item[2]<=1:
            print(f"{item[0]} de {item[1]}")
else:
    print("Vous etes un bébé !")
    for item in content:
        if item[2]<=0:
            print(f"{item[0]} de {item[1]}")