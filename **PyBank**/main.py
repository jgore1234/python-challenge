#import pathlib module
import pathlib

#create filepath for resource raw data
csvpath = pathlib.Path("Resources/budget_data.csv")

#import CSV reading module
import csv


with open(csvpath, mode='r') as csvfile:
    #set CSV reader delimeter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    #read header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

