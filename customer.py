# -----------------------------------------------------------------------
# Final Project Part 1: Bob's Ski & Snowboard Rentals
# Name:                 Mila Weiss
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# Class Definition: Customer
# -----------------------------------------------------------------------
class Customer:

    # --------------------------------------------------
    # Method Name: __init__
    # Abstract: Initialize a Customer object.
    # --------------------------------------------------
    def __init__(self, customer_id, customer_name):

        self.customer_id = customer_id
        self.customer_name = customer_name

    # -------------------- Customer ID Property --------------------
    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        if customer_id <= 0:
            raise Exception("Customer ID must be greater than 0. The value was: {}".format(customer_id))
        else:
            self.__customer_id = customer_id

    # -------------------- Customer Name Property --------------------
    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        if customer_name == "":
            raise Exception("Customer name cannot be blank. The value was: {}".format(customer_name))
        else:
            self.__customer_name = customer_name
