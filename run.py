import gspread
from google.oauth2.service_account import Credentials

"""
Imports at the top, SCOPE and CREDS taken from source code of
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


def get_dealer_data():
    """
    Some inspiration for this function is taken from get_sales_data()
    function in the Love Sandwich walkthrough project

    Get dealer id from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must match a dealer ID in the dealers worksheet.
    The loop will repeatedly request data, until it is valid.
    """
    while True:

        print("Please enter Dealer ID\n")
        print("This must match a Dealer ID in the 'dealer' tab")
        print("Example: 1\n")

        dealer_id = input("Enter Dealer ID here:\n")

        if dealer_data_validation(dealer_id):
            print("Data is valid!")
            break

    return dealer_id

def dealer_data_validation(value):
    """
    Checks an integer has been entered and checks and
    if the dealer ID exists in the Google Sheet.
    """
    try:
        int(value)
        if value not in SHEET.worksheet('dealer').col_values(1):
            raise ValueError(
                f"{value} not in dealer worksheet. Please enter valid dealer"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def get_dealer_name(dealer_id):
    """
    Gets dealer name stored in dealer worksheet.
    """
    stored_dealer_id_col = SHEET.worksheet('dealer').col_values(1)
    stored_dealer_name_col = SHEET.worksheet('dealer').col_values(2)
    stored_dealer_combine_list = zip(stored_dealer_id_col, stored_dealer_name_col)
    stored_dealer = dict(stored_dealer_combine_list)

    dealer_name = stored_dealer.get(dealer_id)
    print(f"You are entering sales data for {dealer_name} with Dealer ID {dealer_id}\n")
    
    return dealer_name

def get_sales_data():
    """
    Some inspiration for this function is taken from get_sales_data()
    function in the Love Sandwich walkthrough project

    Get sales data for dealer from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must match a dealer ID in the dealers worksheet.
    The loop will repeatedly request data, until it is valid.
    """

    print("This must be entered as whole number or to two decimal places")
    print("Example: 100 or 10.50\n")

    sales_data = input("Enter sales data for here:\n")

    return sales_data

def calculate_dealer_pay(sales_data):
    """
    Calculates how much to pay the dealer and prints to terminal.
    """
    if float(sales_data):
        dealer_pay = round(float(sales_data) - ((float(sales_data) * 5) / 100), 2)
    elif int(sales_data):
        dealer_pay = int(sales_data) - ((int(sales_data) * 5) / 100)
        
    print(dealer_pay)

    return dealer_pay

def calculate_house_pay(sales_data):
    """
    Calculates how much to pay the house and prints to terminal.
    """
    if float(sales_data):
        house_pay = round(((float(sales_data) * 5) / 100), 2)
    elif int(sales_data):
        house_pay = ((int(sales_data) * 5) / 100)

    

    return house_pay

def update_pay_worksheet(dealer_id, dealer_name, dealer_pay, house_pay):
    """
    Adds calculations for dealer and house to pay worksheet for storage
    """
    row_data = [dealer_id, dealer_name, dealer_pay, house_pay]
    worksheet_to_update = SHEET.worksheet('pay')
    worksheet_to_update.append_row(row_data)
    print(row_data)


def main():
    """
    Run all program functions.
    """
    dealer_id = get_dealer_data()
    dealer_name = get_dealer_name(dealer_id)
    sales_data = get_sales_data()
    dealer_pay = calculate_dealer_pay(sales_data)
    house_pay = calculate_house_pay(sales_data)
    update_pay_worksheet(dealer_id, dealer_name, dealer_pay, house_pay)

main()


