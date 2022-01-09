# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""

#EH:  import python packages, sys, fire, questionary, csv, pathlib packages
import sys
import fire
import questionary
from pathlib import Path


import csv

#EH:  Below calls function from different modules under qualifier folders.
from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

#EH: import csv_save function from fileio file
from qualifier.utils.fileio import save_csv

#EH:  Load a list of bank loan offer into python list
def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """
#EH:  Request user input of bank loan file path
    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)

#EH:  Exist function when the filepath cannot be found    
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

#EH:  Load the file into python list
    return load_csv(csvpath)

#EH:  request and store customer financial information
def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

#EH:  request user input of credit score, debt, income, loan_amount, home_value
    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

#EH:  store user input as numbers for calculation
    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

#EH:  Call variable values
    return credit_score, debt, income, loan_amount, home_value

#EH:  Find which loans the user qualifies for.
def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    #EH: display a statement of number of qualifying loans
    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered

#EH:  state number of qualifying loans and give user choice to export the list of qualifying loan as csv file.
def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    
    #EH:  Find any qualifying loans or not
    if len(qualifying_loans)>0:

        #EH:  ask and get customer feedback on saving qualifying loan as csv file
        cust_file_save = questionary.confirm("Would you like to save qualified loan list as csv?").ask()

        
        if cust_file_save == False:
            #EH:  If customer doesn't want to export the information, exist out of the function.
            sys.exit(f"No file is saved to your computer.  Have a good day!")
        
        else:
            #EH:  when customer wants to save the file, the function will request/store a csv filename
            filename = questionary.text("Enter a filename to save qualified loan list (.csv):").ask()

            #EH:  validate filename as csv filename or not. invalid filename will trigger function exit.
            if filename[-4:]!=".csv":
                sys.exit(f"Oops! The filename is not valid.  Please re-try.")

            
            #EH:  if filename is csv filename, export qualifying loan to user's computer as csv file
            return save_csv(filename,qualifying_loans)



#EH:  Run all functions from import bank loan list, get customer information, find qualifying loans, and save qualifying loans.
def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)
    


if __name__ == "__main__":
    fire.Fire(run)
