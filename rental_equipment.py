# -----------------------------------------------------------------------
# Final Project Part 1: Bob's Ski & Snowboard Rentals
# Name: Mila Weiss
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# Class Definition: RentalEquipment
# -----------------------------------------------------------------------
class RentalEquipment:

    # --------------------------------------------------
    # Method Name: __init__
    # Abstract: Initialize a RentalEquipment object.
    # --------------------------------------------------
    def __init__(self, hourly_rate, daily_rate, weekly_rate):

        self.hourly_rate = hourly_rate
        self.daily_rate = daily_rate
        self.weekly_rate = weekly_rate

    # -------------------- Hourly Rate Property --------------------
    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        if hourly_rate <= 0:
            raise Exception("Hourly rate must be greater than 0. The value was: {}".format(hourly_rate))
        else:
            self.__hourly_rate = hourly_rate

    # -------------------- Daily Rate Property --------------------
    @property
    def daily_rate(self):
        return self.__daily_rate

    @daily_rate.setter
    def daily_rate(self, daily_rate):
        if daily_rate <= 0:
            raise Exception("Daily rate must be greater than 0. The value was: {}".format(daily_rate))
        else:
            self.__daily_rate = daily_rate

    # -------------------- Weekly Rate Property --------------------
    @property
    def weekly_rate(self):
        return self.__weekly_rate

    @weekly_rate.setter
    def weekly_rate(self, weekly_rate):
        if weekly_rate <= 0:
            raise Exception("Weekly rate must be greater than 0. The value was: {}".format(weekly_rate))
        else:
            self.__weekly_rate = weekly_rate

    # --------------------------------------------------
    # Method Name: calculate_best_price
    # Abstract: Calculate and return the lowest available
    #           rental price.
    # --------------------------------------------------
    def calculate_best_price(self, rental_period, rental_length):

        if rental_length <= 0:
            raise Exception("Rental length must be greater than 0. The value was: {}".format(rental_length))

        if rental_period == "Hourly":
            hourly_price = rental_length * self.hourly_rate
            daily_price = self.daily_rate

            if hourly_price < daily_price:
                return hourly_price
            else:
                return daily_price

        elif rental_period == "Daily":
            daily_price = rental_length * self.daily_rate
            weekly_price = self.weekly_rate

            if daily_price < weekly_price:
                return daily_price
            else:
                return weekly_price

        elif rental_period == "Weekly":
            return rental_length * self.weekly_rate

        else:
            raise Exception("Rental period must be Hourly, Daily, or Weekly.")