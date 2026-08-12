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

# ------------------------------------- PROVIDED TEST MATERIAL -----------------------------------------



# ------------------------------
# Name: Jordyn Barge
# Assignment Name: Final Project Part 2
# ------------------------------

# ------------------------------
# Imports
# ------------------------------

from ast import Return
from customer import Customer
import customer
from rental import Rental
from rental_equipment import RentalEquipment
from rental_shop import RentalShop
from ski import Ski
from snowboard import Snowboard



# ------------------------------
# Function Area
# ------------------------------

# UTILITY FUNCTIONS

# ------------------------------
# Function Name: Validate Integer
# Function Purpose: Validate an integer for range min > 0 and existence as an integer. A range max can be defined, which will be ignored if left empty or < 0
# ------------------------------
def Validate_Integer(intInput, intRangeMax = 0):
    try:
        intInput = int(intInput)
        if intInput > intRangeMax and intRangeMax > 0:
            print("Input must be less than", intRangeMax + 1)
        elif intInput > 0:
            global blnValidated
            blnValidated = True
        else:
            print("Input must be greater than 0")
    except ValueError:
        intInput = int(0)
        print("Input must be a whole number greater than 0")
    return intInput



# ------------------------------
# Function Name: Validate String Y/N
# Function Purpose: Validate a string to be a Y/N answer
# ------------------------------
def Validate_String_Y_N(strInput):
    try:
        strInput = str(strInput)
        if strInput == "Y" or strInput == "N":
            global blnValidated
            blnValidated = True
        else:
            print("Input must be Y/N (case sensitive)")
    except ValueError:
        strInput = str()
        print("Input must be either letter: Y or N (case sensitive)")
    return strInput



# ------------------------------
# Function Name: Validate String
# Function Purpose: Validate a string
# ------------------------------
def Validate_String(strInput):
    try:
        strInput = str(strInput)
        if strInput == "":
            print("Input must not be empty")
        else:
            global blnValidated
            blnValidated = True
    except ValueError:
        strInput = str()
        print("Input must be a string")
    return strInput



# ------------------------------
# Function Name: Get Valid Integer
# Function Purpose: Yields the program until the user enters a valid integer. A range max can be defined, which will be ignored if left empty or < 0
# ------------------------------
def Get_Valid_Integer(strMessage, intRangeMax = 0):
    intInput = int(0)
    global blnValidated
    while blnValidated is False:
        intInput = input(strMessage)
        intInput = Validate_Integer(intInput, intRangeMax)
    blnValidated = False
    print()
    return intInput



# ------------------------------
# Function Name: Get Valid Integer Optional
# Function Purpose: Yields the program until the user enters a valid integer. A range max can be defined, which will be ignored if left empty or < 0. User can leave blank.
# ------------------------------
def Get_Valid_Integer_Optional(strMessage, intRangeMax = 0):
    intInput = int(0)
    global blnValidated
    while blnValidated is False:
        intInput = input(strMessage)

        if intInput == "":
            blnValidated = True
        else:
            intInput = Validate_Integer(intInput, intRangeMax)
    blnValidated = False
    print()
    return intInput



# ------------------------------
# Function Name: Get Valid String Y/N
# Function Purpose: Yields the program until the user enters a valid string, either Y or N.
# ------------------------------
def Get_Valid_String_Y_N(strMessage):
    strInput = str()
    global blnValidated
    while blnValidated is False:
        strInput = input(strMessage)
        strInput = Validate_String_Y_N(strInput)
    blnValidated = False
    print()
    return strInput



# ------------------------------
# Function Name: Get Valid String
# Function Purpose: Yields the program until the user enters a valid string.
# ------------------------------
def Get_Valid_String(strMessage):
    strInput = str()
    global blnValidated
    while blnValidated is False:
        strInput = input(strMessage)
        strInput = Validate_String(strInput)
    blnValidated = False
    print()
    return strInput



# ------------------------------
# Function Name: Search Customer
# Function Purpose: Searches for a customer based on Name and/or Customer ID
# ------------------------------

def Search_Customer(strName, intID = None):
    if type(intID) != int:
        intID = None

    PotentialCustomers = []

    for objCustomer in Customers:
        if objCustomer.customer_id == intID:
            return objCustomer
        elif str.lower(objCustomer.customer_name) == str.lower(strName):
            PotentialCustomers.append(objCustomer)

    if len(PotentialCustomers) == 0:
        return None
    else:
        return PotentialCustomers



# ------------------------------
# Function Name: Get Customer
# Function Purpose: Prompts customer to provide information to get their account
# ------------------------------

def Get_Customer():
    blnValidated = False
    objCustomer = None

    while blnValidated == False:
        strName = Get_Valid_String("Enter your name: ")
        intID = Get_Valid_Integer_Optional("Enter your customer ID (optional, leave blank to skip): ")

        objCustomer = Search_Customer(strName, intID)

        if objCustomer == None:
            strOption = Get_Valid_String_Y_N("No customer was found. Try again? (Enter Y/N): ")

            if strOption == "N":
                blnValidated = True

        elif type(objCustomer) == Customer:
            print("Customer found:", objCustomer.customer_name, objCustomer.customer_id)
        elif type(objCustomer) == list:
            print("Multiple customers with name found.")

            strList = ""
            intItemNumber = 1

            for objPotentialCustomer in objCustomer:
                strList = strList & intItemNumber & ".: " & objPotentialCustomer.customer_name & " " & objPotentialCustomer.customer_id & "\n"
                intItemNumber += 1
            



# APPLICATION FUNCTIONS

# ------------------------------
# Function Name: Start Of Day
# Function Purpose: Prompt user to set the starting inventory numbers, returns the instantiated RentalShop
# ------------------------------

def Start_Of_Day():
    print("---START OF DAY---")
    intSkis = Get_Valid_Integer("Enter ski inventory amount: ")
    intSnowboards = Get_Valid_Integer("Enter snowboard inventory amount: ")
    return RentalShop(intSkis, intSnowboards)



# ------------------------------
# Function Name: Main Menu
# Function Purpose: Prompt user to select a submenu
# ------------------------------

def Main_Menu():
    print("---MAIN MENU---")
    intChoice = Get_Valid_Integer("1. NEW RENTAL\n2. RETURN RENTAL\n3. SHOW INVENTORY\n4. END OF DAY\nSelect an option (1-4): ", 4)

    if intChoice == 1:
        New_Rental_Menu()
    elif intChoice == 2:
        Return_Rental_Menu()
    elif intChoice == 3:
        Show_Inventory() 
    else: 
        End_Of_Day()



# ------------------------------
# Function Name: New Rental Menu
# Function Purpose: Collect rental info to generate a new rental
# ------------------------------

def New_Rental_Menu():
    print("---NEW RENTAL MENU---")
    intChoice = Get_Valid_Integer("1. NEW CUSTOMER\n2. RETURNING CUSTOMER\nSelect an option (1-2): ", 2)
    
    objCustomer = None

    if intChoice == 1:
        objCustomer = New_Customer_Menu()

    Start_Rental_Menu(objCustomer)



# ------------------------------
# Function Name: New Customer Menu
# Function Purpose: Prompt customer to provide their name and create a new profile
# ------------------------------

def New_Customer_Menu():
    global Customers
    
    print("---NEW CUSTOMER MENU---")
    strName = Get_Valid_String("Enter your name: ")
    intID = len(Customers) + 1
    print(strName & ", your CustomerID is", intID)

    objCustomer = Customer(intID, strName)
    Customers.append(objCustomer)

    return objCustomer



# ------------------------------
# Function Name: Start Rental Menu
# Function Purpose: Prompt customer to provide information to generate a new rental
# ------------------------------

def Start_Rental_Menu(objCustomer = None):
    print("---START RENTAL---")



# ------------------------------
# Function Name: Return Rental Menu
# Function Purpose: Prompt customer to provide rental information to process a return
# ------------------------------

def Return_Rental_Menu():
    pass



# ------------------------------
# Function Name: Show Inventory
# Function Purpose: Display the current inventory levels
# ------------------------------

def Show_Inventory():
    pass 



# ------------------------------
# Function Name: End Of Day
# Function Purpose: Display daily totals and end program
# ------------------------------

def End_Of_Day():
    pass


# ------------------------------
# Main Area
# ------------------------------

blnValidated = bool(False)
Customers = []

def main():
    # ----- DAY START
    # Create objects
    Skis = Ski()
    Snowbards = Snowboard()

    # Prompt start of day inventory
    SnowShop = Start_Of_Day()

    # ----- MAIN MENU
    Main_Menu()

main()