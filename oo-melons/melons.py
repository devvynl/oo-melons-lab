from random import randint 
from datetime import datetime

"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == "christmas":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        if self.qty < 10 and self.order_type == "international":
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True
    
    def get_base_price(self):

        surge_price = randint(5,9)
        time_obj = datetime.now()
        num_day = time_obj.isoweekday()
        hour = time_obj.hour
        if num_day in range(1,6) and hour in range(8,12):
            return surge_price + 4

        return surge_price

class GovernmentMelonOrder(AbstractMelonOrder):
    """Each order will need to pass a security inspection."""
    def __init__(self, species, qty):

        self.order_type = "government"
        self.tax = 0
        self.passed_inspection = False
        super().__init__(species, qty)

    def mark_inspection(self):
        self.passed_inspection = True 

        

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08
        super().__init__(species, qty)

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        self.order_type = "international"
        self.tax = 0.17
        super().__init__(species, qty)

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
