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

def clear_worksheet():
    """
    Clears any data in the pay worksheet generated in
    the last use of the pay calculator
    """
    SHEET.worksheet('pay').batch_clear(["B2:D5"])

def get_dealer_data():
    """
    Some inspiration for this function is taken from get_sales_data()
    function in the Love Sandwich walkthrough project

    Get dealer id from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must match a dealer ID in the dealers worksheet.
    The loop will repeatedly request data, until it is valid.
    """

    print("Please enter Dealer ID")
    print("This must match a Dealer ID in the 'dealer' tab")
    print("Example: 1\n")

    dealer_id = input("Enter Dealer ID here:\n")

    return dealer_id

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


def main():
    """
    Run all program functions.
    """

    clear_worksheet()
    dealer_id = get_dealer_data()
    get_dealer_name(dealer_id)
    get_sales_data()

main()
