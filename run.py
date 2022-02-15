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

def clear_work_sheet():
    """
    Clears any data in the pay worksheet generated in
    the last use of the pay calculator
    """
    SHEET.worksheet('pay').batch_clear(["B2:D5"])

clear_work_sheet()
