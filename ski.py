# -----------------------------------------------------------------------
# Final Project Part 1: Bob's Ski & Snowboard Rentals
# Name:                 Mila Weiss
# -----------------------------------------------------------------------


from rental_equipment import RentalEquipment


# -----------------------------------------------------------------------
# Class Definition: Ski
# -----------------------------------------------------------------------
class Ski(RentalEquipment):

    # --------------------------------------------------
    # Method Name: __init__
    # Abstract: Initialize a Ski object with the ski
    #           hourly, daily, and weekly rental rates.
    # --------------------------------------------------
    def __init__(self):

        super().__init__(15, 50, 200)
