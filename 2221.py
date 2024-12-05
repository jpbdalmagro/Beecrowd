class Pomekon:
    def __init__(self, bonus, power, defense, level):
        self.bonus = bonus
        self.power = power
        self.defense = defense
        self.level = level
        strength = (power + defense) / 2
        if level % 2 == 0:
            strength += bonus
        self.strength = strength
        
    def __str__(self):
        return f"{self.name} {self.strength:.0f}"
    
instances = int(input())

for _ in range(instances):
    bonus = int(input())

    for _ in range(2):
        if _ == 0:
            inputs = list(map(int, input().split()))
            power, defense, level = inputs
            Dabriel = Pomekon(bonus, power, defense, level)
        else:
            inputs = list(map(int, input().split()))
            power, defense, level = inputs
            Guarte = Pomekon(bonus, power, defense, level)

    if Dabriel.strength > Guarte.strength:
        print("Dabriel")
    elif Dabriel.strength < Guarte.strength:
        print("Guarte")
    else:
        print("Empate")
