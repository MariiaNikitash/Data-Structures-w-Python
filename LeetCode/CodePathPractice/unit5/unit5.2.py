# Linked Lists part 2


class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
#write a method attack() that takes in a Pokemon object opponent and decreases
# opponent's hp by their self's damage amount.

#If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the
# opponent's hp to 0 and print out "<Opponent name> fainted>.
#otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>"		
	def attack(self, opponent):
		opponent.hp -= self.damage
		if opponent.hp <= 0:
			opponent.hp = 0
			print(f"{opponent.name} fainted")
		else:
			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
	
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

