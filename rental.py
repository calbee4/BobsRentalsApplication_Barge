# -----------------------------------------------------------------------
# Final Project Part 1: Bob's Ski & Snowboard Rentals
# Name:                 Mila Weiss
# -----------------------------------------------------------------------


from ski import Ski
from snowboard import Snowboard


# -----------------------------------------------------------------------
# Class Definition: Rental
# -----------------------------------------------------------------------
class Rental:

    family_discount_rate = 0.25
    coupon_discount_rate = 0.10

    # --------------------------------------------------
    # Method Name: __init__
    # Abstract: Initialize a Rental object.
    # --------------------------------------------------
    def __init__(self, customer, ski_quantity, snowboard_quantity,
                 rental_period, coupon_code=""):

        self.customer = customer
        self.ski_quantity = ski_quantity
        self.snowboard_quantity = snowboard_quantity
        self.rental_period = rental_period
        self.coupon_code = coupon_code

        if self.get_total_items() == 0:
            raise Exception("A rental must include at least one item.")

    # -------------------- Customer Property --------------------
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if customer is None:
            raise Exception("Customer cannot be blank.")
        else:
            self.__customer = customer

    # -------------------- Ski Quantity Property --------------------
    @property
    def ski_quantity(self):
        return self.__ski_quantity

    @ski_quantity.setter
    def ski_quantity(self, ski_quantity):
        if type(ski_quantity) != int:
            raise Exception(
                "Ski quantity must be an integer. The value was: {}".format(
                    ski_quantity
                )
            )
        elif ski_quantity < 0:
            raise Exception(
                "Ski quantity cannot be negative. The value was: {}".format(
                    ski_quantity
                )
            )
        else:
            self.__ski_quantity = ski_quantity

    # -------------------- Snowboard Quantity Property --------------------
    @property
    def snowboard_quantity(self):
        return self.__snowboard_quantity

    @snowboard_quantity.setter
    def snowboard_quantity(self, snowboard_quantity):
        if type(snowboard_quantity) != int:
            raise Exception(
                "Snowboard quantity must be an integer. The value was: {}".format(
                    snowboard_quantity
                )
            )
        elif snowboard_quantity < 0:
            raise Exception(
                "Snowboard quantity cannot be negative. The value was: {}".format(
                    snowboard_quantity
                )
            )
        else:
            self.__snowboard_quantity = snowboard_quantity

    # -------------------- Rental Period Property --------------------
    @property
    def rental_period(self):
        return self.__rental_period

    @rental_period.setter
    def rental_period(self, rental_period):
        if rental_period != "Hourly" and \
                rental_period != "Daily" and \
                rental_period != "Weekly":

            raise Exception(
                "Rental period must be Hourly, Daily, or Weekly. "
                "The value was: {}".format(rental_period)
            )
        else:
            self.__rental_period = rental_period

    # -------------------- Coupon Code Property --------------------
    @property
    def coupon_code(self):
        return self.__coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        if type(coupon_code) != str:
            raise Exception(
                "Coupon code must be a string. The value was: {}".format(
                    coupon_code
                )
            )
        else:
            self.__coupon_code = coupon_code

    # --------------------------------------------------
    # Method Name: get_total_items
    # Abstract: Return the total number of rented items.
    # --------------------------------------------------
    def get_total_items(self):
        return self.ski_quantity + self.snowboard_quantity

    # --------------------------------------------------
    # Method Name: calculate_subtotal
    # Abstract: Calculate the rental cost before discounts.
    # --------------------------------------------------
    def calculate_subtotal(self, rental_length):

        ski = Ski()
        snowboard = Snowboard()

        ski_total = (
            ski.calculate_best_price(
                self.rental_period,
                rental_length
            ) * self.ski_quantity
        )

        snowboard_total = (
            snowboard.calculate_best_price(
                self.rental_period,
                rental_length
            ) * self.snowboard_quantity
        )

        return ski_total + snowboard_total

    # --------------------------------------------------
    # Method Name: apply_family_discount
    # Abstract: Apply a 25% discount to rentals containing
    #           three through five total items.
    # --------------------------------------------------
    def apply_family_discount(self, rental_cost):

        total_items = self.get_total_items()

        if total_items >= 3 and total_items <= 5:
            discount = rental_cost * Rental.family_discount_rate
            return rental_cost - discount
        else:
            return rental_cost

    # --------------------------------------------------
    # Method Name: apply_coupon_discount
    # Abstract: Apply a 10% discount when the coupon code
    #           ends with BBP.
    # --------------------------------------------------
    def apply_coupon_discount(self, rental_cost):                           # Creates a method to check and apply the coupon discount

        coupon_length = len(self.coupon_code)                               # Finds how many characters are in the coupon code

        if coupon_length >= 3:                                              # Checks that the coupon has at least 3 characters

            third_last_character = self.coupon_code[coupon_length - 3]      # Gets the third character from the end
            second_last_character = self.coupon_code[coupon_length - 2]     # Gets the second character from the end
            last_character = self.coupon_code[coupon_length - 1]            # Gets the last character

            if (third_last_character == "B" and                             # Checks whether the third-last character is B
                second_last_character == "B" and                            # Checks whether the second-last character is B
                last_character == "P"):                                     # Checks whether the last character is P

                discount = rental_cost * Rental.coupon_discount_rate        # Calculates 10% of the rental cost
                return rental_cost - discount                               # Returns the price after the discount

            else:                                                           # Runs when the coupon does not end with BBP
                return rental_cost                                          # Returns the original cost

        else:                                                               # Runs when the coupon has fewer than 3 characters
            return rental_cost                                              # Returns the original cost
    # --------------------------------------------------
    # Method Name: calculate_total
    # Abstract: Calculate the rental total and apply the
    #           family discount before the coupon discount.
    # --------------------------------------------------
    def calculate_total(self, rental_length):

        rental_cost = self.calculate_subtotal(rental_length)

        rental_cost = self.apply_family_discount(rental_cost)
        rental_cost = self.apply_coupon_discount(rental_cost)

        return rental_cost

    # --------------------------------------------------
    # Method Name: calculate_estimate
    # Abstract: Calculate the estimated rental cost.
    # --------------------------------------------------
    def calculate_estimate(self, estimated_length):
        return self.calculate_total(estimated_length)

    # --------------------------------------------------
    # Method Name: calculate_final_bill
    # Abstract: Calculate the final bill using the actual
    #           rental length.
    # --------------------------------------------------
    def calculate_final_bill(self, actual_length):
        return self.calculate_total(actual_length)
