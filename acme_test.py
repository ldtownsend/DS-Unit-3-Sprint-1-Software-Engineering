import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test the toy's weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_new_product_stealability(self):
        """test new product stealability to be 'Very stealable!'"""
        prod2 = Product("New Product", weight=1)
        self.assertEqual(prod2.stealability(), 'Very stealable!')

if __name__ == '__main__':
    unittest.main()
