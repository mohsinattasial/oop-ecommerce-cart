from abc import ABC, abstractmethod


class PricingStrategy(ABC):

    @abstractmethod
    def calculate(self, subtotal: float) -> float:
        pass


class NoDiscount(PricingStrategy):

    def calculate(self, subtotal: float) -> float:
        return subtotal


class PercentageDiscount(PricingStrategy):

    def __init__(self, percent: float):

        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100")

        self.percent = percent

    def calculate(self, subtotal: float) -> float:

        discount = subtotal * (self.percent / 100)
        return subtotal - discount