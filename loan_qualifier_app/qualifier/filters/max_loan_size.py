# -*- coding: utf-8 -*-
"""Max Loan Size Filter.

This script filters the bank list by comparing the user's loan value
against the bank's maximum loan size.

"""

#EH:  Filters the bank list by the maximum allowed loan amount.
def filter_max_loan_size(loan_amount, bank_list):
    """Filters the bank list by the maximum allowed loan amount.

    Args:
        loan_amount (int): The requested loan amount.
        bank_list (list of lists): The available bank loans.

    Returns:
        A list of qualifying bank loans.
    """

#EH:   create a blank loan size approval list.
    loan_size_approval_list = []

#EH:  append the bank loan offer to loan size approval list when bank loan size offer amount is larger or equal to customer's request.
    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list
