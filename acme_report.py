

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):

    products = []

    for i in range(num_products):
        adj = sample(ADJECTIVES, 1)
        noun = sample(NOUNS, 1)
        name = (adj[0]) +" "+ (noun[0])

        price_i = randint(5, 100)
        weight_i = randint(5, 100)
        flammability_i = uniform(0.0, 2.5)

        product = Product(name, price=price_i, weight=weight_i,
                          flammability=flammability_i)

        products.append(product)


    return products


def inventory_report(products):
    n_unique = len(set(products.name))
    return n_unique




if __name__ == '__main__':
    inventory_report(generate_products())



    return
