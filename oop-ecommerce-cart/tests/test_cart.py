import unittest
from src.cart import ShoppingCart
from src.models import Product
from src.strategies import NoDiscount, PercentageDiscount


class TestCart(unittest.TestCase):

    def setUp(self):

        self.product1 = Product("P1","Laptop",1000)
        self.product2 = Product("P2","Mouse",50)

        self.cart = ShoppingCart(NoDiscount())

    def test_add_product(self):

        self.cart.add(self.product1,1)

        self.assertEqual(self.cart.subtotal(),1000)

    def test_add_multiple_qty(self):

        self.cart.add(self.product1,2)

        self.assertEqual(self.cart.subtotal(),2000)

    def test_remove_product(self):

        self.cart.add(self.product1,1)
        self.cart.remove("P1")

        self.assertEqual(self.cart.subtotal(),0)

    def test_percentage_discount(self):

        self.cart.add(self.product1,1)

        self.cart.strategy = PercentageDiscount(10)

        self.assertEqual(self.cart.total(),900)

    def test_no_discount(self):

        self.cart.add(self.product1,1)

        self.assertEqual(self.cart.total(),1000)

    def test_invalid_quantity(self):

        with self.assertRaises(ValueError):
            self.cart.add(self.product1,0)

    def test_invalid_discount(self):

        with self.assertRaises(ValueError):
            PercentageDiscount(200)

    def test_remove_invalid_product(self):

        with self.assertRaises(KeyError):
            self.cart.remove("X")


if __name__ == "__main__":
    unittest.main()