# -*- coding: utf-8 -*-
"""Debt to Income Filter.

This script filters the bank list by the applicant's
maximum debt-to-income ratio.

"""

#EH:  Filters the bank list by the maximum debt-to-income ratio allowed by the bank.
def filter_debt_to_income(monthly_debt_ratio, bank_list):
    """Filters the bank list by the maximum debt-to-income ratio allowed by the bank.

    Args:
        monthly_debt_ratio (float): The applicant's monthly debt ratio.
        bank_list (list of lists): The available bank loans.

    Returns:
        A list of qualifying bank loans.
    """
   
    #EH:  create a blank debit to income approval list.
    debit_to_income_approval_list = []

    #EH:  append debit to income approval list with bank with debt to income larger or equal than customer's  
    for bank in bank_list:
        if monthly_debt_ratio <= float(bank[3]):
            debit_to_income_approval_list.append(bank)
    return debit_to_income_approval_list
