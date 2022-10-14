

from unittest import TestCase

from code.ut_app.cart_item import (
    CartItem, PriceLessThanZeroError)


class TestCartItemErrors(TestCase):
    """ test cart item errors class """

    def test_cart_item_price_err(self) -> None:
        """ test cart item price error """

        with self.assertRaises(PriceLessThanZeroError):
            CartItem("apples", -1, 5)
