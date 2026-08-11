# -----------------------------------------------------------------------
# Final Project Part 1: Bob's Ski & Snowboard Rentals
# Name:                 Mila Weiss
# -----------------------------------------------------------------------


from rental_equipment import RentalEquipment


# -----------------------------------------------------------------------
# Class Definition: Snowboard
# -----------------------------------------------------------------------
class Snowboard(RentalEquipment):

    # --------------------------------------------------
    # Method Name: __init__
    # Abstract: Initialize a Snowboard object with the
    #           hourly, daily, and weekly rental rates.
    # --------------------------------------------------
    def __init__(self):

        super().__init__(10, 40, 160)
