# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
from pathlib import Path
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


#EH: Save a list of qualified loan as csv
def save_csv(filename, data):

    #create header on output file
    header =['Lender','Max Loan Amount','Max LTV','Max DTI','Min Credit Score','Interest Rate']

    #create filename
    
    csvpath = Path(filename)
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter =csv.writer(csvfile,delimiter=",")
        csvwriter.writerow(header)
        for qualified_loan in data:
            #write qualified list into csv output
            csvwriter.writerow(qualified_loan[0:])