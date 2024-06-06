class Animal:
    """
    Represents an animal in the zoo.

    Attributes:
        name (str): The name of the animal.
        hunger (int): The hunger level of the animal.
        zoo_name (str): The name of the zoo.
    """

    def __init__(self, name, hunger=0):
        """
        Initializes a new Animal object.

        Args:
            name (str): The name of the animal.
            hunger (int, optional): The initial hunger level of the animal. Defaults to 0.
        """
        self.name = name
        self.hunger = hunger
        self.zoo_name = "Hayaton"

    def is_hungry(self):
        """
        Checks if the animal is hungry.

        Returns:
            bool: True if the animal is hungry, False otherwise.
        """
        return self.hunger > 0

    def feed(self):
        """
        Reduces the hunger level of the animal by 1.
        """
        self.hunger -= 1

    def talk(self):
        """
        Prints a generic noise for the animal.
        """
        print("Animal noise")

    def special_method(self):
        pass



class Dog(Animal):
    """
    Represents a dog in the zoo.
    Inherits from the Animal class.

    Attributes:
        name (str): The name of the dog.
        hunger (int): The hunger level of the dog.
        zoo_name (str): The name of the zoo.
    """

    def __init__(self, name, hunger):
        """
        Initializes a new Dog object.

        Args:
            name (str): The name of the dog.
            hunger (int): The initial hunger level of the dog.
        """
        super().__init__(name, hunger)

    def fetch_stick(self):
        """
        special_method.
        """
        print("There you go, sir!")

    def special_method(self):
        """
        Calls the fetch_stick method.
        """
        self.fetch_stick()

    def talk(self):
        """
        Prints the sound a dog makes.
        """
        print("woof woof")


class Cat(Animal):
    """
    Represents a cat in the zoo.
    Inherits from the Animal class.

    Attributes:
        name (str): The name of the cat.
        hunger (int): The hunger level of the cat.
        zoo_name (str): The name of the zoo.
    """

    def __init__(self, name, hunger):
        """
        Initializes a new Cat object.

        Args:
            name (str): The name of the cat.
            hunger (int): The initial hunger level of the cat.
        """
        super().__init__(name, hunger)

    def chase_laser(self):
        """
        special_method.
        """
        print("Meeeeow")

    def special_method(self):
        """
        Calls the chase_laser method.
        """
        self.chase_laser()

    def talk(self):
        """
        Prints the sound a cat makes.
        """
        print("meow")


class Skunk(Animal):
    """
    Represents a skunk in the zoo.
    Inherits from the Animal class.

    Attributes:
        name (str): The name of the skunk.
        hunger (int): The hunger level of the skunk.
        stink_count (int): The number of times the skunk has sprayed.
        zoo_name (str): The name of the zoo.
    """

    def __init__(self, name, hunger, stink_count=6):
        """
        Initializes a new Skunk object.

        Args:
            name (str): The name of the skunk.
            hunger (int): The initial hunger level of the skunk.
            stink_count (int, optional): The initial stink count of the skunk. Defaults to 6.
        """
        super().__init__(name, hunger)
        self.stink_count = stink_count

    def stink(self):
        """
        special_method.
        """
        print("Dear lord!")

    def special_method(self):
        """
        Calls the stink method.
        """
        self.stink()

    def talk(self):
        """
        Prints the sound a skunk makes.
        """
        print("tsssss")


class Unicorn(Animal):
    """
    Represents a unicorn in the zoo.
    Inherits from the Animal class.

    Attributes:
        name (str): The name of the unicorn.
        hunger (int): The hunger level of the unicorn.
        zoo_name (str): The name of the zoo.
    """

    def __init__(self, name, hunger):
        """
        Initializes a new Unicorn object.

        Args:
            name (str): The name of the unicorn.
            hunger (int): The initial hunger level of the unicorn.
        """
        super().__init__(name, hunger)

    def sing(self):
        """
        special_method.
        """
        print("I’m not your toy...")

    def special_method(self):
        """
        Calls the sing method.
        """
        self.sing()

    def talk(self):
        """
        Prints the sound a unicorn makes.
        """
        print("Good day, darling")


class Dragon(Animal):
    """
    Represents a dragon in the zoo.
    Inherits from the Animal class.

    Attributes:
        name (str): The name of the dragon.
        hunger (int): The hunger level of the dragon.
        color (str): The color of the dragon.
        zoo_name (str): The name of the zoo.
    """

    def __init__(self, name, hunger, color="Green"):
        """
        Initializes a new Dragon object.

        Args:
            name (str): The name of the dragon.
            hunger (int): The initial hunger level of the dragon.
            color (str, optional): The color of the dragon. Defaults to "Green".
        """
        super().__init__(name, hunger)
        self.color = color

    def breath_fire(self):
        """
        special_method.
        """
        print("$@#$#@$")

    def special_method(self):
        """
        Calls the breath_fire method.
        """
        self.breath_fire()

    def talk(self):
        """
        Prints the sound a dragon makes.
        """
        print("Raaaawr")
