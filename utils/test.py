import unittest
from cart_list import Product, CartNode, CartList


class CartListUnitTest(unittest.TestCase):
    def test_product_field_assignement(self):
        fields = ["id", "name", "quality", "unit", "price", "link", "more"]
        product = Product(
            name="sugar",
            quality="Best",
            unit="Number",
            price=300,
            link="link",
            more="more information",
        )
        for f in fields:
            self.assertTrue(product[f] != None, f"{f} has value")

    def test_add_to_cart(self):
        cart = CartNode()
        product = Product(
            name="sugar",
            quality="Best",
            unit="Number",
            price=300,
            link="link",
        )
        self.assertEqual(cart.add(product), product)
        with self.assertRaises(TypeError):
            cart.add()

    def test_remove_to_cart(self):
        cart = CartNode()
        product = Product(
            name="sugar",
            quality="Best",
            unit="Number",
            price=300,
            link="link",
        )
        cart.add(product)
        self.assertFalse(cart.remove("sss"), "the product found")
        self.assertTrue(
            cart.remove(cart.id), "the product with id not found in dataset"
        )
        with self.assertRaises(TypeError):
            cart.remove()

    def test_get_cart(self):
        cartList = CartList()
        cart = CartNode()
        product = Product(
            name="sugar",
            quality="Best",
            unit="Number",
            price=300,
            link="link",
        )
        cart.add(product)
        cartList.add(cart)
        self.assertEqual(cart, cartList.getCart("not found"), "cart not found")
        self.assertTrue(cartList.getCart(cart.id) != False)


if __name__ == "__main__":
    unittest.main()
