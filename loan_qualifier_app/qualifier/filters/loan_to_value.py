# -*- coding: utf-8 -*-
"""Loan to Value Filter.

This script filters the bank list by the applicant's maximum home loan
to home value ratio.

"""

#EH:  Filters the bank list by the maximum loan to value ratio
def filter_loan_to_value(loan_to_value_ratio, bank_list):
    """Filters the bank list by the maximum loan to value ratio.

    Args:
        loan_to_value_ratio (float): The applicant's loan to value ratio.
        bank_list (list of lists): The available bank loans.

    Returns:
        A list of qualifying bank loans.
    """
    #EH:  create a blank loan to value approval list
    loan_to_value_approval_list = []

    #EH:  append loan to value approval list when bank loan to value ratio is larger or equal to customer's
    for bank in bank_list:
        if loan_to_value_ratio <= float(bank[2]):
            loan_to_value_approval_list.append(bank)
    return loan_to_value_approval_list
