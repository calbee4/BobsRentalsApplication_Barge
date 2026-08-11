# -----------------------------------------------------------------------
# Final Project Part 1: Bob's Ski & Snowboard Rentals
# Name:                 Mila Weiss
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# Class Definition: RentalShop
# -----------------------------------------------------------------------
class RentalShop:

    # --------------------------------------------------
    # Method Name: __init__
    # Abstract: Initialize a RentalShop object with the
    #           starting ski and snowboard inventory.
    # --------------------------------------------------
    def __init__(self, starting_ski_inventory,
                 starting_snowboard_inventory):

        self.starting_ski_inventory = starting_ski_inventory
        self.starting_snowboard_inventory = starting_snowboard_inventory

        self.__available_ski_inventory = starting_ski_inventory
        self.__available_snowboard_inventory = starting_snowboard_inventory

        self.__daily_skis_rented = 0
        self.__daily_snowboards_rented = 0
        self.__daily_revenue = 0

    # -------------------- Starting Ski Inventory Property --------------------
    @property
    def starting_ski_inventory(self):
        return self.__starting_ski_inventory

    @starting_ski_inventory.setter
    def starting_ski_inventory(self, starting_ski_inventory):

        if type(starting_ski_inventory) != int:
            raise Exception(
                "Starting ski inventory must be an integer. "
                "The value was: {}".format(starting_ski_inventory)
            )

        elif starting_ski_inventory < 0:
            raise Exception(
                "Starting ski inventory cannot be negative. "
                "The value was: {}".format(starting_ski_inventory)
            )

        else:
            self.__starting_ski_inventory = starting_ski_inventory

    # -------------------- Starting Snowboard Inventory Property --------------------
    @property
    def starting_snowboard_inventory(self):
        return self.__starting_snowboard_inventory

    @starting_snowboard_inventory.setter
    def starting_snowboard_inventory(self, starting_snowboard_inventory):

        if type(starting_snowboard_inventory) != int:
            raise Exception(
                "Starting snowboard inventory must be an integer. "
                "The value was: {}".format(starting_snowboard_inventory)
            )

        elif starting_snowboard_inventory < 0:
            raise Exception(
                "Starting snowboard inventory cannot be negative. "
                "The value was: {}".format(starting_snowboard_inventory)
            )

        else:
            self.__starting_snowboard_inventory = starting_snowboard_inventory

    # -------------------- Available Ski Inventory Property --------------------
    @property
    def available_ski_inventory(self):
        return self.__available_ski_inventory

    # -------------------- Available Snowboard Inventory Property --------------------
    @property
    def available_snowboard_inventory(self):
        return self.__available_snowboard_inventory

    # -------------------- Daily Skis Rented Property --------------------
    @property
    def daily_skis_rented(self):
        return self.__daily_skis_rented

    # -------------------- Daily Snowboards Rented Property --------------------
    @property
    def daily_snowboards_rented(self):
        return self.__daily_snowboards_rented

    # -------------------- Daily Revenue Property --------------------
    @property
    def daily_revenue(self):
        return self.__daily_revenue

    # --------------------------------------------------
    # Method Name: check_availability
    # Abstract: Check whether the requested equipment
    #           quantities are currently available.
    # --------------------------------------------------
    def check_availability(self, ski_quantity,
                           snowboard_quantity):

        if type(ski_quantity) != int:
            raise Exception(
                "Ski quantity must be an integer. "
                "The value was: {}".format(ski_quantity)
            )

        elif type(snowboard_quantity) != int:
            raise Exception(
                "Snowboard quantity must be an integer. "
                "The value was: {}".format(snowboard_quantity)
            )

        elif ski_quantity < 0:
            raise Exception(
                "Ski quantity cannot be negative. "
                "The value was: {}".format(ski_quantity)
            )

        elif snowboard_quantity < 0:
            raise Exception(
                "Snowboard quantity cannot be negative. "
                "The value was: {}".format(snowboard_quantity)
            )

        elif ski_quantity > self.available_ski_inventory:
            return False

        elif snowboard_quantity > self.available_snowboard_inventory:
            return False

        else:
            return True

    # --------------------------------------------------
    # Method Name: rent_equipment
    # Abstract: Reduce available inventory and update
    #           the daily equipment totals.
    # --------------------------------------------------
    def rent_equipment(self, ski_quantity,
                       snowboard_quantity):

        if self.check_availability(
                ski_quantity,
                snowboard_quantity) == False:

            raise Exception(
                "The requested equipment is not available."
            )

        else:
            self.__available_ski_inventory -= ski_quantity
            self.__available_snowboard_inventory -= snowboard_quantity

            self.__daily_skis_rented += ski_quantity
            self.__daily_snowboards_rented += snowboard_quantity

    # --------------------------------------------------
    # Method Name: return_equipment
    # Abstract: Restore returned equipment to the
    #           available inventory.
    # --------------------------------------------------
    def return_equipment(self, ski_quantity,
                         snowboard_quantity):

        if type(ski_quantity) != int:
            raise Exception(
                "Ski quantity must be an integer. "
                "The value was: {}".format(ski_quantity)
            )

        elif type(snowboard_quantity) != int:
            raise Exception(
                "Snowboard quantity must be an integer. "
                "The value was: {}".format(snowboard_quantity)
            )

        elif ski_quantity < 0:
            raise Exception(
                "Ski quantity cannot be negative. "
                "The value was: {}".format(ski_quantity)
            )

        elif snowboard_quantity < 0:
            raise Exception(
                "Snowboard quantity cannot be negative. "
                "The value was: {}".format(snowboard_quantity)
            )

        elif (self.available_ski_inventory + ski_quantity >
              self.starting_ski_inventory):

            raise Exception(
                "Returned skis cannot exceed the starting inventory."
            )

        elif (self.available_snowboard_inventory + snowboard_quantity >
              self.starting_snowboard_inventory):

            raise Exception(
                "Returned snowboards cannot exceed the starting inventory."
            )

        else:
            self.__available_ski_inventory += ski_quantity
            self.__available_snowboard_inventory += snowboard_quantity

    # --------------------------------------------------
    # Method Name: add_daily_revenue
    # Abstract: Add a completed rental payment to the
    #           daily rental revenue.
    # --------------------------------------------------
    def add_daily_revenue(self, rental_revenue):

        if (type(rental_revenue) != int and
            type(rental_revenue) != float):

            raise Exception(
                "Rental revenue must be a number. "
                "The value was: {}".format(rental_revenue)
            )

        elif rental_revenue < 0:
            raise Exception(
                "Rental revenue cannot be negative. "
                "The value was: {}".format(rental_revenue)
            )

        else:
            self.__daily_revenue += rental_revenue
