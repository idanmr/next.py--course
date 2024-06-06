from Animal import Animal, Dog, Cat, Skunk, Unicorn, Dragon


zoo_lst = [
    Dog("Brownie", 10),
    Cat("Zelda", 3),
    Skunk("Stinky", 0),
    Unicorn("Keith", 7),
    Dragon("Lizzy", 1450)
]

doggo = Dog("Doggo", 80)
kitty = Cat("Kitty", 80)
stinky_jr = Skunk("Stinky Jr.", 80)
clair = Unicorn("Clair", 80)
mcfly = Dragon("McFly", 80)

zoo_lst.extend([doggo, kitty, stinky_jr, clair, mcfly])

for animal in zoo_lst:
    if animal.is_hungry():
        print(type(animal).__name__ + " " + animal.name)
        while animal.is_hungry():
            animal.feed()
    animal.talk()
    animal.special_method()

print(animal.zoo_name)
