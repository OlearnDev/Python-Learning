from model.player import Player
from model.weapon import Weapon

player1 = Player("John", 20, 3)
player2 = Player("Marie", 20, 5)
player1.attack_player(player2)

print(player1.get_pseudo(), "attaque ", player2.get_pseudo())

print("Bienvenue au joueur",player1.get_pseudo(), "/ Points de vie:", player1.get_health(), "/ Attaque: ", player1.get_attack_value())
print("Bienvenue au joueur",player2.get_pseudo(), "/ Points de vie:", player2.get_health(), "/ Attaque: ", player2.get_attack_value())
