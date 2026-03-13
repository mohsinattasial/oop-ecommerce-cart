from src.cart import ShoppingCart
from src.models import Product
from src.strategies import NoDiscount, PercentageDiscount

strategy = NoDiscount()
cart = ShoppingCart(strategy)

products = {
    "P1": Product("P1", "Laptop", 1000),
    "P2": Product("P2", "Mouse", 50),
    "P3": Product("P3", "Keyboard", 80),
}

while True:

    print("\n1 Add Product")
    print("2 Remove Product")
    print("3 Show Subtotal")
    print("4 Apply Discount")
    print("5 Checkout Total")
    print("6 Exit")

    choice = input("Choose: ")

    if choice == "1":

        sku = input("SKU (P1,P2,P3): ")
        qty = int(input("Quantity: "))

        cart.add(products[sku], qty)

        print("Added to cart")

    elif choice == "2":

        sku = input("SKU: ")
        cart.remove(sku)

        print("Removed")

    elif choice == "3":

        print("Subtotal:", cart.subtotal())

    elif choice == "4":

        percent = float(input("Discount %: "))
        cart.strategy = PercentageDiscount(percent)

        print("Discount applied")

    elif choice == "5":

        print("Total:", cart.total())

    elif choice == "6":
        break