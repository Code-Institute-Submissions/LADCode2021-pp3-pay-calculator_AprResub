import gspread
from google.oauth2.service_account import Credentials

from datetime import date

import pandas as pd


"""
Imports at the top and SCOPE and CREDS taken from source code of
love_sandwiches walkthrough project.
"""

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dealer_details')


def get_user_choice():
    """
    Starts programme by taking users choice via input
    """
    print("\nWelcome to Pay Calculator\n")

    print("Would you like to:\n \nA. View previous sales data for a dealer?\n \nB. Enter new sales data for a dealer?\n")
    
    while True:
        user_choice = input("\nEnter 'a' or 'b'\n")
        if user_choice_validation(user_choice):
            print("Valid choice.\n")
            break

    print("\nPlease select a dealer ID from the list below (dealer ID is the number to the left of the name):\n")

    all_dealers = SHEET.worksheet('dealer').get_all_values()[1:]

    for dealer in all_dealers:
        print(*dealer)

    print("\nThis must match a Dealer ID in the list above")
    print("Example: 1\n")

    return user_choice


def user_choice_validation(value):
    """
    Some minor detail such as ValueError as e taken from Code
    Institute love sandwiches walkthrough project.
    Check an integer has been entered and check if the dealer 
    ID exists in the Google Sheet.
    """
    try:
        if value != 'a' and value != 'b':
            raise ValueError(
                f"{value} not in dealer worksheet. Please enter valid dealer"
            )
    except ValueError as e:
        print(f"{value} is not a valid data input, please try again.\n")
        return False

    return True


def get_dealer_id():
    """
    Some inspiration for this function is taken from get_sales_data()
    function in the Love Sandwich walkthrough project
    Get dealer id from the user.
    Get dealer id and names from Google Sheet and display to user.
    Run a while loop to collect a valid intger of data from the user
    via the terminal, which must match a dealer ID in the list provided.
    The loop will repeatedly request data, until it is valid.
    """

    while True:
        #input validated by dealer_data_validation()
        dealer_id = input("Enter Dealer ID here to start:\n")
        if dealer_data_validation(dealer_id):
            print("Valid dealer ID.\n")
            break

    return dealer_id
    
def dealer_data_validation(value):
    
    """
    Some minor detail such as ValueError as e taken from Code
    Institute love sandwiches walkthrough project.
    Check an integer has been entered and check if the dealer 
    ID exists in the Google Sheet.
    """
    try:
        int(value)
        if value not in SHEET.worksheet('dealer').col_values(1):
            raise ValueError(
                f"{value} not in dealer worksheet. Please enter valid dealer"
            )
    except ValueError as e:
        print(f"{value} is not a valid data input, please try again.\n")
        return False

    return True


def get_previous_sales_data(dealer_id):
    """
    Gets previous dealer data based on user inputted ID
    """
    dealer_id = int(dealer_id)
    dataframe = pd.DataFrame(SHEET.worksheet('pay').get_all_records())
    pd.set_option('display.max_columns', None)
    dealer_pay_data = dataframe.loc[dataframe['Dealer_ID'] == dealer_id]
    print(f"\n{dealer_pay_data.to_string(index=False)}")


def get_dealer_name(dealer_id):
    """
    Get dealer name stored in dealer worksheet and print to terminal.
    """
    stored_dealer_id_col = SHEET.worksheet('dealer').col_values(1)
    stored_dealer_name_col = SHEET.worksheet('dealer').col_values(2)
    stored_dealer_list = zip(stored_dealer_id_col, stored_dealer_name_col)
    stored_dealer = dict(stored_dealer_list)

    dealer_name = stored_dealer.get(dealer_id)
    print(
        f"You are entering sales data for {dealer_name}"
        + f" with Dealer ID {dealer_id}\n"
        )   
    return dealer_name


def get_sales_data():
    """
    Some inspiration for this function is taken from get_sales_data()
    function in the Love Sandwich walkthrough project
    Get sales data for dealer from the user.
    Run a while loop to collect a valid integer 
    or float of data from the user via the terminal, 
    which must match a dealer ID in the dealers worksheet.
    The loop will repeatedly request data, until it is valid.
    """
    while True:

        print("This must be entered as whole number or to two decimal places")
        print("Example: 100 or 10.50\n")

        #input validated by sales_data_validation()
        sales_data = input("Enter sales data here:\n")

        if sales_data_validation(sales_data):
            print("Valid sales data.\n")
            break

    return sales_data


def sales_data_validation(value):
    """
    Some very minor detail such as ValueError as e taken from Code
    Institute love sandwiches walkthrough project.
    Check if an integer or float has been entered for sales data.
    """
    try:
        if not float(value) and not int(value):
            raise ValueError(
                f"{value} is invalid. Please enter whole number or decimal"
            )
    except ValueError as e:
        print(f"{value} is invalid, please check your input and try again.\n")
        return False
    
    return True


def calculate_dealer_pay(sales_data, dealer_name):
    """
    Calculate how much to pay the dealer based on inputted sales data.
    """
    print("Calculating dealer pay...\n")

    dealer_pay = 0
    
    if float(sales_data):
        dealer_pay = round(
            float(sales_data) - ((float(sales_data) * 5) / 100), 2
                )
    elif int(sales_data):
        dealer_pay = int(sales_data) - ((int(sales_data) * 5) / 100)
    
    print(f"You need to pay {dealer_name} £{dealer_pay}\n")

    return dealer_pay


def calculate_house_pay(sales_data):
    """
    Calculate how much to pay the house based on sales data.
    """
    print("Calculating house pay...\n")

    house_pay = 0

    if float(sales_data):
        house_pay = round(((float(sales_data) * 5) / 100), 2)
    elif int(sales_data):
        house_pay = ((int(sales_data) * 5) / 100)
    
    print(f"You need to pay the house £{house_pay}\n")

    return house_pay
    

def date_generator():
    """
    Generated today's today to be used when storing sales data
    """
    today = date.today()
    date_entered = today.strftime("%d/%m/%Y")

    return date_entered


def update_pay_worksheet(dealer_id, dealer_name, dealer_pay, house_pay, date_entered):
    """
    Add calculations for dealer and house to pay worksheet for storage.
    """
    row_data = [dealer_id, dealer_name, dealer_pay, house_pay, date_entered]
    print(f"Updating pay worksheet with {row_data}...\n")
    worksheet_to_update = SHEET.worksheet('pay')
    worksheet_to_update.append_row(row_data)
    print(f"{row_data} successfully added to pay worksheet")


def main():
    """
    Run all program functions.
    """
    user_choice = get_user_choice()
    dealer_id = get_dealer_id()
    if user_choice == 'b':
        dealer_name = get_dealer_name(dealer_id)
        sales_data = get_sales_data()
        dealer_pay = calculate_dealer_pay(sales_data, dealer_name)
        house_pay = calculate_house_pay(sales_data)
        date_entered = date_generator()
        update_pay_worksheet(dealer_id, dealer_name, dealer_pay, house_pay, date_entered)
        exit()
    elif user_choice == 'a':
        get_previous_sales_data(dealer_id)


main()
