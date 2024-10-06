""" Commentaire sur plusieurs lignes

On va créer des tuples :
boissons = [(name,age_min)]
repas = [(nom, (heure_min, heure_max), age)]

"""

plats=[
    ("Pizza", (0, 23), 10),
    ("Hamburger", (7, 22), 8),
    ("Riz", (0, 23), 5),
    ("Spaguetti blanc", (11, 19), 0),
    ("Salade de fruit", (0, 23), 0),
    
    ("Cafe", (6, 16), 16),
    ("Expresso", (6, 14), 19),
    ("Cappucino", (6, 16), 16),
    
    ("Soupe au legume", (16, 23), 10),
    ("Soupe de boeuf", (16, 21), 10)
]

boissons=[
    ("Coca Cola", 10),
    ("Lait", 0),
    ("Jus naturel de mangue", 12),
    ("Sprite", 10),
    ("Jack Danniels", 19),
    ("Champagne", 25)
]

age = 8
heure = 10

print()
print("---------- Le Menu du Jour ----------")

for plat in plats:
    if age >= plat[2]:
        print(plat[0])

print()
print("---------- Les Boissons du Jour ----------")
        
for boisson in boissons:
    if age >= boisson[1]:
        print(boisson[0])
