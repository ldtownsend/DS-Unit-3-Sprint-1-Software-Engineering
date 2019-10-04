# Part 1
import random
import unittest

class Product:

    def __init__(self, name, price = 10, weight = 20, flammability = 0.5,
                 identifier = random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price / self.weight < 0.5:
            return "Not so stealable..."
        elif self.price / self.weight < 1:
            return "Kinda stealable"
        else:
            return "Very stealable!"

    def explode(self):
        if self.flammability * self.weight < 10:
            return "...fizzle"
        elif self.flammability * self.weight < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):
    """
    Boxing glove sub class of product
    """

    def __init__(self, name, price = 10, weight = 10, flammability = 0.5,
                 identifier = random.randint(1000000,9999999)):
        super().__init__(name, price, weight, flammability, identifier)
        self.weight = weight


    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH"
