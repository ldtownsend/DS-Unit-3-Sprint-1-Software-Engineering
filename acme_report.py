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
        name = (adj[0]) + " " + (noun[0])

        price_i = randint(5, 100)
        weight_i = randint(5, 100)
        flammability_i = uniform(0.0, 2.5)

        product = Product(name, price=price_i, weight=weight_i,
                          flammability=flammability_i)

        products.append(product)

    return products


def inventory_report(products):

    n_unique = []
    for i in range(len(products)):
        next_name = products[i].name
        n_unique.append(next_name)
    unique_names = len(set(n_unique))

    prices = []
    for i in range(len(products)):
        next_price = products[i].price
        prices.append(next_price)
    average_price = sum(prices) / len(prices)

    weights = []
    for i in range(len(products)):
        next_weight = products[i].weight
        weights.append(next_weight)
    average_weight = sum(weights) / len(weights)

    flammabilities = []
    for i in range(len(products)):
        next_flammability = products[i].flammability
        flammabilities.append(next_flammability)
    average_flammability = sum(flammabilities) / len(flammabilities)

    return print(" ACME CORPORATION OFFICIAL INVENTORY REPORT \n",
                 "Unique product names:", unique_names, "\n",
                 "Average price:", average_price, "\n",
                 "Average weight:", average_weight, "\n",
                 "Average flammability:", average_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
