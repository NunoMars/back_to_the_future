# Description: A simple program that calculates the price of a shopping cart of movies.
class DVDStore:
    """The DVD store that calculates the price of a shopping cart."""

    def __init__(self):
        self.bttf_prices = {
            "back to the future 1": 15,
            "back to the future 2": 15,
            "back to the future 3": 15,
        }
        self.other_movie_price = 20

    def calculate_total_price(self, cart):
        """Calculate the total price of the shopping cart."""
        count_how_many_btff_films = {
            movie: cart.count(movie) for movie in self.bttf_prices.keys()
        }  #  Compte le nombre de films Back to the Future dans le panier par film

        total_price = sum(
            self.bttf_prices[movie] * count_how_many_btff_films[movie]
            for movie in self.bttf_prices.keys()
        )  #  Calcule le prix total des films Back to the Future

        unique_bttf_count = sum(
            1 for movie, count in count_how_many_btff_films.items() if count > 0
        )  #  Compte le nombre de films Back to the Future uniques dans le panier
        if unique_bttf_count == 2:
            total_price *= 0.9  #  Applique une réduction de 10% si deux films Back to the Future sont présents
        elif unique_bttf_count == 3:
            total_price *= 0.8  # Applique une réduction de 20% si trois films Back to the Future sont présents

        total_price += (
            len(cart) - sum(count_how_many_btff_films.values())
        ) * self.other_movie_price  #  Ajoute le prix des autres films au prix total

        return int(total_price)


class ShoppingCart:
    """A simple shopping cart that stores movies."""

    def __init__(self):
        self.cart = []

    def add_movie(self, movie):
        """Add a movie to the cart."""
        self.cart.append(movie)

    def get_cart(self):
        """Return the cart."""
        return self.cart


def main():
    """Main function to run the program."""
    ### Instancie les classes DVDStore et ShoppingCart ###
    dvd_store = DVDStore()
    shopping_cart = ShoppingCart()

    print("Enter movies in your cart (one per line), then leave blank to finish:")
    while True:
        movie = (
            input().lower()
        )  #  Demande à l'utilisateur d'entrer un film et le convertit en minuscules

        if movie == "":  #  Si l'utilisateur entre une chaîne vide, arrête la boucle
            break
        shopping_cart.add_movie(movie)  #  Ajoute le film au panier

    total_price = dvd_store.calculate_total_price(
        shopping_cart.get_cart()
    )  #  Calcule le prix total du panier
    print("Total price:", total_price)


if __name__ == "__main__":
    main()
