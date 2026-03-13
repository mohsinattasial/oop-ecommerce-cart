from typing import Dict
from .models import Product, CartItem
from .strategies import PricingStrategy


class ShoppingCart:

    def __init__(self, strategy: PricingStrategy):

        self._items: Dict[str, CartItem] = {}
        self.strategy = strategy

    def add(self, product: Product, qty: int = 1) -> None:

        if qty < 1:
            raise ValueError("Quantity must be >= 1")

        if product.sku in self._items:
            self._items[product.sku].qty += qty
        else:
            self._items[product.sku] = CartItem(product, qty)

    def remove(self, sku: str) -> None:

        if sku not in self._items:
            raise KeyError("Product not in cart")

        del self._items[sku]

    def subtotal(self) -> float:

        total = 0

        for item in self._items.values():
            total += item.subtotal()

        return total

    def total(self) -> float:

        subtotal = self.subtotal()
        return self.strategy.calculate(subtotal)