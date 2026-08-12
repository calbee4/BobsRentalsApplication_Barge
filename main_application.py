# ------------------------------
# Name: Jordyn Barge
# Assignment Name: Final Project Part 2
# ------------------------------

# ------------------------------
# Imports
# ------------------------------

from customer import Customer
from rental import Rental
from rental_equipment import RentalEquipment
from rental_shop import RentalShop
from ski import Ski
from snowboard import Snowboard
from datetime import datetime, timedelta



# ------------------------------
# Function Area
# ------------------------------

# UTILITY FUNCTIONS

# ------------------------------
# Function Name: Validate Integer
# Function Purpose: Validate an integer, within an optional inclusive range.
# ------------------------------
def Validate_Integer(intInput, intRangeMax = None, intRangeMin = None):
    if intRangeMin != None and intRangeMax != None:
        if intRangeMax < intRangeMin:
            intRangeMax = intRangeMin

    try:
        intInput = int(intInput)
        if intRangeMax != None and intInput > intRangeMax:
            print("Maximum input must be less than", intRangeMax + 1)
        elif intRangeMin != None and intInput < intRangeMin:
            print("Minimum input must be", intRangeMin, "or greater")
        else:
            global blnValidated
            blnValidated = True
    except ValueError:
        intInput = int(0)
        strOutput = "Input must be a whole number"

        if intRangeMin != None:
            strOutput += ", minimum " + str(intRangeMin)

        if intRangeMax != None:
            strOutput += ", maximum " + str(intRangeMax)

        print(strOutput)
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
# Function Name: Validate String Rental Basis
# Function Purpose: Validate a string to be "Hourly", "Daily", or "Weekly"
# ------------------------------
def Validate_String_Rental_Basis(strInput):
    try:
        strInput = str(strInput)
        if strInput == "Hourly" or strInput == "Daily" or strInput == "Weekly":
            global blnValidated
            blnValidated = True
        else:
            print("Input must be Hourly, Daily, or Weekly (case sensitive)")
    except ValueError:
        strInput = str()
        print("Input must be Hourly, Daily, or Weekly (case sensitive)")
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
# Function Purpose: Yields the program until the user enters a valid integer. An optional inclusive range can be set.
# ------------------------------
def Get_Valid_Integer(strMessage, intRangeMax = None, intRangeMin = None):
    intInput = int(0)
    global blnValidated
    while blnValidated is False:
        intInput = input(strMessage)
        intInput = Validate_Integer(intInput, intRangeMax, intRangeMin)
    blnValidated = False
    print()
    return intInput



# ------------------------------
# Function Name: Get Valid Integer Optional
# Function Purpose: Yields the program until the user enters a valid integer. An optional inclusive range can be set. User can leave blank.
# ------------------------------
def Get_Valid_Integer_Optional(strMessage, intRangeMax = None, intRangeMin = None):
    intInput = int(0)
    global blnValidated
    while blnValidated is False:
        intInput = input(strMessage)

        if intInput == "":
            blnValidated = True
        else:
            intInput = Validate_Integer(intInput, intRangeMax, intRangeMin)
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
# Function Name: Get Valid Rental Basis
# Function Purpose: Yields the program until the user enters a valid rental basis (string).
# ------------------------------
def Get_Valid_Rental_Basis(strMessage):
    strInput = str()
    global blnValidated
    while blnValidated is False:
        strInput = input(strMessage)
        strInput = Validate_String_Rental_Basis(strInput)
    blnValidated = False
    print()
    return strInput



# ------------------------------
# Function Name: Get Valid String Optional
# Function Purpose: Yields the program until the user enters a valid string. User can leave blank.
# ------------------------------
def Get_Valid_String_Optional(strMessage):
    strInput = str()
    global blnValidated
    while blnValidated is False:
        strInput = input(strMessage)

        if strInput == "":
            blnValidated = True
        else:
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
        intID = Get_Valid_Integer_Optional("Enter your customer ID (optional, leave blank to skip): ", intRangeMin = 0)

        objCustomer = Search_Customer(strName, intID)

        if objCustomer == None:
            strOption = Get_Valid_String_Y_N("No customer was found. Try again? (Enter Y/N): ")

            if strOption == "N":
                blnValidated = True

        elif type(objCustomer) == Customer:
            print("Customer found: {} (ID: {})".format(objCustomer.customer_name, objCustomer.customer_id))
            strOption = Get_Valid_String_Y_N("Is this the correct customer? (Enter Y/N): ")

            if strOption == "Y":
                blnValidated = True
            else:
                print("Canceling, please try again.\n")
        elif type(objCustomer) == list:
            print("Customers found via name. Select your profile.")

            strList = ""
            intItemNumber = 1

            for objPotentialCustomer in objCustomer:
                strList = strList + "{}. {} (ID: {})\n".format(intItemNumber, objPotentialCustomer.customer_name, objPotentialCustomer.customer_id)
                intItemNumber += 1

            intItemNumber = Get_Valid_Integer(strList + "(Enter 1-{}): ".format(len(objCustomer)), intRangeMin = 1, intRangeMax = len(objCustomer))
            objCustomer = objCustomer[intItemNumber - 1]

            print("Customer selected: {} (ID: {})".format(objCustomer.customer_name, objCustomer.customer_id))
            strOption = Get_Valid_String_Y_N("Is this the correct customer? (Enter Y/N): ")

            if strOption == "Y":
                blnValidated = True
            else:
                print("Canceling, please try again.\n")

    return objCustomer



# ------------------------------
# Function Name: Get Customer Rentals
# Function Purpose: Returns a list of all rentals made by a customer and prompts the user to select one
# ------------------------------

def Get_Customer_Rentals(objCustomer):
    if type(objCustomer) != Customer:
        print("Customer was not properly provided! Please try again.")
        return

    global Rentals

    lstRentals = []

    for objRental in Rentals:
        if objRental.customer == objCustomer:
            lstRentals.append(objRental)

    if len(lstRentals) == 0:
        print("No rentals found!")
        return None
    else:
        print("Customer rentals found. Select the rental.")

        strList = ""
        intItemNumber = 1

        for objPotentialRental in lstRentals:
            strList = strList + "{}. {} Skis, {} Snowboards, Rental Basis: {}, Coupon: {}\n".format(intItemNumber, objPotentialRental.ski_quantity, objPotentialRental.snowboard_quantity, objPotentialRental.rental_period, objPotentialRental.coupon_code)
            intItemNumber += 1

        intItemNumber = Get_Valid_Integer(strList + "(Enter 1-{}): ".format(len(lstRentals)), intRangeMin = 1, intRangeMax = len(lstRentals))
        objRental = lstRentals[intItemNumber - 1]

        print("Rental {} selected.".format(intItemNumber))
        return objRental



# ------------------------------
# Function Name: Display Quote
# Function Purpose: Displays a quote with the given rental items, basis, and length
# ------------------------------

def Display_Quote(intSkis, intSnowboards, strRentalBasis, intRentalLength, objRental):
    fltSubtotal = objRental.calculate_subtotal(intRentalLength)
    fltTotal = objRental.calculate_subtotal(intRentalLength)

    if objRental.ski_quantity > 0:
        print("{} Skis on a x{} {} basis: ${:.2f}".format(intSkis, intRentalLength, strRentalBasis, Skis.calculate_best_price(strRentalBasis, intRentalLength) * intSkis))
                    
    if objRental.snowboard_quantity > 0:
        print("{} Snowboards on a x{} {} basis: ${:.2f}".format(intSnowboards, intRentalLength, strRentalBasis, Snowboards.calculate_best_price(strRentalBasis, intRentalLength) * intSnowboards))
                    
    print("Subtotal: ${:.2f}".format(fltSubtotal))

    fltTotal = objRental.apply_family_discount(fltTotal)

    if fltTotal < fltSubtotal:
        print("Family discount: -${:.2f}".format(fltSubtotal - fltTotal))
        fltSubtotal = fltTotal
                
    fltTotal = objRental.apply_coupon_discount(fltTotal)
                    
    if fltTotal < fltSubtotal:
        print("Coupon code: -${:.2f}".format(fltSubtotal - fltTotal))
                    
    print("Total: ${:.2f}".format(fltTotal))

# APPLICATION FUNCTIONS

# ------------------------------
# Function Name: Start Of Day
# Function Purpose: Prompt user to set the starting inventory numbers, returns the instantiated RentalShop
# ------------------------------

def Start_Of_Day():
    print("---START OF DAY---")
    intSkis = Get_Valid_Integer("Enter ski inventory amount: ", intRangeMin = 0)
    intSnowboards = Get_Valid_Integer("Enter snowboard inventory amount: ", intRangeMin = 0)
    
    return RentalShop(intSkis, intSnowboards)



# ------------------------------
# Function Name: Main Menu
# Function Purpose: Prompt user to select a submenu
# ------------------------------

def Main_Menu():
    print("---MAIN MENU---")
    intChoice = Get_Valid_Integer("1. NEW RENTAL\n2. RETURN RENTAL\n3. SHOW INVENTORY\n4. END OF DAY\nSelect an option (1-4): ", intRangeMin = 1, intRangeMax = 4)

    if intChoice == 1:
        New_Rental_Menu()
    elif intChoice == 2:
        Return_Rental_Menu()
    elif intChoice == 3:
        Show_Inventory()
        print()
        Main_Menu()
    else: 
        End_Of_Day()



# ------------------------------
# Function Name: New Rental Menu
# Function Purpose: Collect rental info to generate a new rental
# ------------------------------

def New_Rental_Menu():
    print("---NEW RENTAL MENU---")
    strChoice = Get_Valid_String_Y_N("Are you a new customer? (Answer Y/N): ")
    
    objCustomer = None

    if strChoice == "Y":
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
    print(strName + ", your CustomerID is", intID)
    print()

    objCustomer = Customer(intID, strName)
    Customers.append(objCustomer)

    return objCustomer



# ------------------------------
# Function Name: Start Rental Menu
# Function Purpose: Prompt customer to provide information to generate a new rental
# ------------------------------

def Start_Rental_Menu(objCustomer = None):
    global SnowShop
    global Rentals
    global Skis
    global Snowboards

    print("---START RENTAL---")
    blnCancel = False

    intSkis = 0
    intSnowboards = 0
    strRentalBasis = ""
    intRentalLength = 0
    strCoupon = ""

    if type(objCustomer) != Customer:
        objCustomer = None

    if objCustomer == None:
        print("Select your user profile.")
        objCustomer = Get_Customer()
        
        if objCustomer == None:
            blnCancel = True

    if SnowShop.available_ski_inventory + SnowShop.available_snowboard_inventory == 0:
        print("There is currently no equipment to rent! Come back later!\n")
        blnCancel = True

    if not blnCancel:
        Show_Inventory()

        if SnowShop.available_ski_inventory > 0:
            intSkis = Get_Valid_Integer("How many Skis would you like to rent? (Enter a whole number): ", intRangeMin = 0, intRangeMax = SnowShop.available_ski_inventory)
        
        if SnowShop.available_snowboard_inventory > 0: 
            intSnowboards = Get_Valid_Integer("How many Snowboards would you like to rent? (Enter a whole number): ", intRangeMin = 0, intRangeMax = SnowShop.available_snowboard_inventory)

        if intSkis == 0 and intSnowboards == 0:
            print("No inventory is being rented -- rental canceled.\n")
            blnCancel = True

        if not blnCancel:
            intRentalChoice = Get_Valid_Integer("Would you like to rent on an Hourly, Daily, or Weekly basis?\n1. HOURLY\n2. DAILY\n3. WEEKLY\n(Enter a number 1-3): ", 3, 1)

            if intRentalChoice == 1:
                strRentalBasis = "Hourly"
            elif intRentalChoice == 2:
                strRentalBasis = "Daily"
            else:
                strRentalBasis = "Weekly"

            intRentalLength = Get_Valid_Integer("What's the estimated length of the rental? (Enter a whole number): ", intRangeMin = 1)

            strCoupon = Get_Valid_String_Optional("Enter a discount code (optional, leave blank if none): ")

            objRental = Rental(objCustomer, intSkis, intSnowboards, strRentalBasis, strCoupon)

            print("CONFIRM RENTAL: \nCustomer: {} (ID: {}) \nSkis: {} \nSnowboards: {} \nRental Basis: {} \nRental Length: {} \nCoupon Code: {}".format(objCustomer.customer_name, objCustomer.customer_id, intSkis, intSnowboards, strRentalBasis, intRentalLength, strCoupon))
            strConfirm = Get_Valid_String_Y_N("Is this correct? (Enter Y/N): ")

            if strConfirm == "Y":
                print("COST ESTIMATE:")
                
                Display_Quote(intSkis, intSnowboards, strRentalBasis, intRentalLength, objRental)
                
                strConfirm = Get_Valid_String_Y_N("Confirm rental (Enter Y/N): ")

            if strConfirm == "Y":
                print("Rental Started.\n")
                Rentals.append(objRental)

                SnowShop.rent_equipment(intSkis, intSnowboards)
            else:
                print("Rental canceled. Returning to main menu.\n")

    Main_Menu()



# ------------------------------
# Function Name: Return Rental Menu
# Function Purpose: Prompt customer to provide rental information to process a return
# ------------------------------

def Return_Rental_Menu():
    global SnowShop
    global Rentals

    print("---RENTAL RETURN---")
    blnCancel = False

    print("Select your user profile.")
    objCustomer = Get_Customer()
        
    if objCustomer == None:
        blnCancel = True

    if not blnCancel:
        objRental = Get_Customer_Rentals(objCustomer)

        if objRental == None:
            print("Returning to the main menu.\n")
            blnCancel = True
        else:
            intRentalTime = Get_Valid_Integer("Enter the actual rental length: ", intRangeMin = 1)

            print("CONFIRM RENTAL: \nCustomer Name: {} (ID: {}) \nSkis Rented: {} \nSnowboards Rented: {} \nRental Period: {} \nRental Time: {}".format(objCustomer.customer_name, objCustomer.customer_id, objRental.ski_quantity, objRental.snowboard_quantity, objRental.rental_period, intRentalTime))
            strChoice = Get_Valid_String_Y_N("Is this correct? (Enter Y/N): ")

            if strChoice == "N":
                print("Canceling rental return. Returning to main menu.\n")
                blnCancel = True

            if not blnCancel:
                print("CHECKOUT:")

                Display_Quote(objRental.ski_quantity, objRental.snowboard_quantity, objRental.rental_period, intRentalTime, objRental)
                
                strChoice = Get_Valid_String_Y_N("Confirm total due amount (Enter Y/N): ")

                if strChoice == "N":
                    print("Canceling checkout. Returning to main menu.\n")
                    blnCancel = True

                if not blnCancel:
                    SnowShop.return_equipment(objRental.ski_quantity, objRental.snowboard_quantity)
                    SnowShop.add_daily_revenue(objRental.calculate_final_bill(intRentalTime))

                    print("Successfully returned {} skis and {} snowboards. Thank you for renting with Bobs Rentals!\n".format(objRental.ski_quantity, objRental.snowboard_quantity))

                    Rentals.remove(objRental)

    Main_Menu()



# ------------------------------
# Function Name: Show Inventory
# Function Purpose: Display the current inventory levels
# ------------------------------

def Show_Inventory():
    global SnowShop

    print("Current inventory levels: \nSkis: {} \nSnowboards: {}".format(SnowShop.available_ski_inventory, SnowShop.available_snowboard_inventory))



# ------------------------------
# Function Name: End Of Day
# Function Purpose: Display daily totals and end program
# ------------------------------

def End_Of_Day():
    global SnowShop

    print("\n---END OF DAY---")
    print("Skis Rented Today: {} \nSnowboards Rented Today: {} \nDaily Revenue: ${:.2f}".format(SnowShop.daily_skis_rented, SnowShop.daily_snowboards_rented, SnowShop.daily_revenue))
    print("Good work today! :)")


# ------------------------------
# Main Area
# ------------------------------

blnValidated = bool(False)
Customers = []
Rentals = []
SnowShop = None
Skis = Ski()
Snowboards = Snowboard()

def main():
    global SnowShop

    # ----- DAY START
    # Create objects
    SnowShop = Start_Of_Day()

    # ----- MAIN MENU
    Main_Menu()

main()