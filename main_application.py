# ------------------------------------- PROVIDED TEST MATERIAL ------------------------------------------

# # -----------------------------------------------------------------------
# # Final Project Part 1: Bob's Ski & Snowboard Rentals
# # Name:                 Mila Weiss
# # -----------------------------------------------------------------------


# from customer import Customer
# from ski import Ski
# from snowboard import Snowboard
# from rental import Rental
# from rental_shop import RentalShop


# # -----------------------------------------------------------------------
# # Main Program
# # Abstract: Create objects and test the classes and methods.
# # -----------------------------------------------------------------------
# def main():

#     # -------------------------------------------------------------------
#     # Create Objects
#     # -------------------------------------------------------------------
#     customer = Customer(101, "Mila Weiss")

#     ski = Ski()
#     snowboard = Snowboard()

#     rental = Rental(customer, 2, 1, "Daily", "SAVE10BBP")

#     rental_shop = RentalShop(10, 8)


#     # -------------------------------------------------------------------
#     # Test Customer
#     # -------------------------------------------------------------------
#     print("CUSTOMER TEST")
#     print("Customer ID: {}".format(customer.customer_id))
#     print("Customer Name: {}".format(customer.customer_name))


#     # -------------------------------------------------------------------
#     # Test Equipment and Best Price
#     # -------------------------------------------------------------------
#     print("\nEQUIPMENT TEST")
#     print("Ski Hourly Rate: ${:.2f}".format(ski.hourly_rate))
#     print("Snowboard Hourly Rate: ${:.2f}".format(
#         snowboard.hourly_rate
#     ))

#     print("Ski Best Price for 4 Hours: ${:.2f}".format(
#         ski.calculate_best_price("Hourly", 4)
#     ))

#     print("Snowboard Best Price for 4 Hours: ${:.2f}".format(
#         snowboard.calculate_best_price("Hourly", 4)
#     ))


#     # -------------------------------------------------------------------
#     # Test Rental Calculations
#     # -------------------------------------------------------------------
#     print("\nRENTAL TEST")

#     print("Total Items: {}".format(rental.get_total_items()))

#     print("One-Day Subtotal: ${:.2f}".format(
#         rental.calculate_subtotal(1)
#     ))

#     print("One-Day Estimate: ${:.2f}".format(
#         rental.calculate_estimate(1)
#     ))

#     final_bill = rental.calculate_final_bill(2)

#     print("Two-Day Final Bill: ${:.2f}".format(final_bill))


#     # -------------------------------------------------------------------
#     # Test Inventory
#     # -------------------------------------------------------------------
#     print("\nINVENTORY TEST")

#     print("Equipment Available: {}".format(
#         rental_shop.check_availability(2, 1)
#     ))

#     print("Too Many Skis Available: {}".format(
#         rental_shop.check_availability(20, 1)
#     ))

#     rental_shop.rent_equipment(2, 1)

#     print("Available Skis After Rental: {}".format(
#         rental_shop.available_ski_inventory
#     ))

#     print("Available Snowboards After Rental: {}".format(
#         rental_shop.available_snowboard_inventory
#     ))

#     rental_shop.return_equipment(2, 1)

#     print("Available Skis After Return: {}".format(
#         rental_shop.available_ski_inventory
#     ))

#     print("Available Snowboards After Return: {}".format(
#         rental_shop.available_snowboard_inventory
#     ))


#     # -------------------------------------------------------------------
#     # Test Daily Totals
#     # -------------------------------------------------------------------
#     print("\nDAILY TOTALS TEST")

#     rental_shop.add_daily_revenue(final_bill)

#     print("Daily Skis Rented: {}".format(
#         rental_shop.daily_skis_rented
#     ))

#     print("Daily Snowboards Rented: {}".format(
#         rental_shop.daily_snowboards_rented
#     ))

#     print("Daily Revenue: ${:.2f}".format(
#         rental_shop.daily_revenue
#     ))


# # -----------------------------------------------------------------------
# # Run Main Program
# # -----------------------------------------------------------------------
# main()

# ------------------------------------- PROVIDED TEST MATERIAL ------------------------------------------