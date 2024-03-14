import unittest
from back_to_the_future import DVDStore, ShoppingCart


class TestBackToTheFuture(unittest.TestCase):
    """Class to test the back_to_the_future.py program."""

    def setUp(self):
        self.dvd_store = DVDStore()
        self.shopping_cart = ShoppingCart()

    def test_calculate_total_price_example_1(self):
        """Test the calculate_total_price with two identical films plus one diffrent of the saga."""

        # Add movies to the shopping cart
        self.shopping_cart.add_movie("back to the future 1")
        self.shopping_cart.add_movie("back to the future 2")
        self.shopping_cart.add_movie("back to the future 3")

        # Calculate the total price
        total_price = self.dvd_store.calculate_total_price(
            self.shopping_cart.get_cart()
        )

        # Assert that the total price is correct
        self.assertEqual(total_price, 36)

    def test_calculate_total_price_example_2(self):
        """Test the calculate_total_price with two diffrents films of the saga."""

        # Add movies to the shopping cart
        self.shopping_cart.add_movie("back to the future 1")
        self.shopping_cart.add_movie("back to the future 3")

        # Calculate the total price
        total_price = self.dvd_store.calculate_total_price(
            self.shopping_cart.get_cart()
        )

        # Assert that the total price is correct
        self.assertEqual(total_price, 27)

    def test_calculate_total_price_example_3(self):
        """Test the calculate_total_price with one film of back to the future."""

        # Add movies to the shopping cart
        self.shopping_cart.add_movie("back to the future 1")

        # Calculate the total price
        total_price = self.dvd_store.calculate_total_price(
            self.shopping_cart.get_cart()
        )

        # Assert that the total price is correct
        self.assertEqual(total_price, 15)

    def test_calculate_total_price_example_4(self):
        """Test the calculate_total_price with two identical back tu the future films."""

        # Add movies to the shopping cart
        self.shopping_cart.add_movie("back to the future 1")
        self.shopping_cart.add_movie("back to the future 2")
        self.shopping_cart.add_movie("back to the future 3")
        self.shopping_cart.add_movie("back to the future 2")

        # Calculate the total price
        total_price = self.dvd_store.calculate_total_price(
            self.shopping_cart.get_cart()
        )

        # Assert that the total price is correct
        self.assertEqual(total_price, 48)

    def test_calculate_total_price_example_5(self):
        """Test the calculate_total_price with an other external film."""

        # Add movies to the shopping cart
        self.shopping_cart.add_movie("back to the future 1")
        self.shopping_cart.add_movie("back to the future 2")
        self.shopping_cart.add_movie("back to the future 3")
        self.shopping_cart.add_movie("La chèvre")

        # Calculate the total price
        total_price = self.dvd_store.calculate_total_price(
            self.shopping_cart.get_cart()
        )

        # Assert that the total price is correct
        self.assertEqual(total_price, 56)


if __name__ == "__main__":
    unittest.main()
