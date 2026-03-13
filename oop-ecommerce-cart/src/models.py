from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: float


@dataclass
class CartItem:
    product: Product
    qty: int = 1

    def subtotal(self) -> float:
        return self.product.price * self.qty