# BobsRentalsApplication_Barge
Bob's Rental python application for CPDM 120.

BobsRentalApplication is a Python application created to simulate the experience of running a rental shop for skis and snowboards. It allows new customers to create user profiles, process new rentals, quote their estimated bill and final amount due, and automatically handles inventory updates.

The main application can be found in main_application.py. The provided classes are customer.py, rental.py, rental_equipment.py, rental_shop.py, ski.py, and snowboard.py.

---

# Application Structure:
Upon launching the application, you're presented 4 options:
- New Rental
- Return Rental
- Display Inventory
- End of Day

## New Rental
Upon selecting New Rental, you'll be prompted to answer a few questions:
- Are you a new customer?
  - If yes, you'll be prompted to provide your name to register your customer profile.
  - If no, you'll be prompted to provide your information to find and select your customer profile.
- How many Skis and Snowboards would you like to rent?
- What's the rental basis? Hourly, Daily, or Weekly?
- What is the estimated length of your rental?
- Is there a coupon code you'd like to use? (optional)

After answering these questions, you'll be asked to confirm the information. If the information is correct, it'll be used to provided an estimated bill for the rental, and you'll be asked to confirm the estimate. Upon confirmation, the rental is started and the inventory is updated to reflect it. 

## Return Rental
Upon selecting Return Rental, you'll be prompted to provide your information to find and select your customer profile. After confirming the customer profile, you'll be presented all of the rentals associated with the profile and asked to select one. When one is selected, you'll be presented with the information and asked to confirm it. Then you'll be asked how long the actual rental length was. Using that information, a final total is provided and you're asked to confirm the rental return before the inventory is returned to the shop and the bill total is added to the Daily Revenue.

## Display Inventory
Upon selecting Display Inventory, the current inventory of Skis and Snowboards will be displayed on screen.

## End of Day
Upon selecting End of Day, the total amounts of Skis and Snowboards will be displayed alongside the Daily Revenue, and then the program will end.

---
# Reflection
The assigned classes were used to create and display customer profiles, rentals, and shop properties. They are kept track of using a list, and then iterated through to display information for menus and menu item selection.

I did not find myself with any limitations or problems in the process of using the assigned classes! They were really well thought out and designed, and I found myself with very little friction. It was super intuitive and easy to use. This experience was very eye opening for me, because it helped me understand what kinds of documentation and design go into creating good, applicable classes for others to use. The class provided to me had a certain level of granularity that helped me get everything I needed out of it. It helped me understand how other people may approach the same problems. It also made me reflect on the design of the classes I sent out. It was admittedly a little messy because I assumed I'd be the only one using it, which wasn't the case. I learned that going forward, I should tighten up the quality of the code I create to make it more intuitive for others. I also learned that when I'm creating classes, I should not be concerned with any sort of printing or displaying, as that's a concern for the application development stage. I think I got so wrapped up in the mindset of "getting ahead of the game" that I started concerning myself with parts of the bigger picture (displays, totals, final calculations) and forgot to hone in on the details, the smaller pieces that lead to a good final product.

All that to say, I enjoyed this assignment, and I appreciate all the lessons I've learned from it.

Credit to mila2seta for the very well designed classes.
