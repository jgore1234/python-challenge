# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#import pathlib module
import pathlib
import os
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

# The total number of months included in the dataset
    # The total number of months is equal to the number of rows
    # excluding the header row
    # every time we call next, we increment a counter
    # count = 0
    # count = count + 1

    count = 0
    total_pnl = 0
    row = next(csvreader)
    # first_row = next(csvreader)
    change = []
    prior_pnl = 0
    months = []
  
    # The stopping condition is that there is no data in the last row
    while row is not None:
        # Count the row
        count = count + 1
        months.append(row[0])
        # Get pnl for this month
        pnl = row[1]

        # Convert pnl from string to integer
        pnl = int(pnl)

        # Every row is one month
        # Count the pnl for this month
        total_pnl = total_pnl + pnl
        pnl_change = pnl - prior_pnl
        change.append(pnl_change)
        prior_pnl = pnl

        # Get the next row
        try:
            row = next(csvreader)
        except:
            break
    #    * The average of the changes in "Profit/Losses" over the entire period 
    avg_change = sum(change) / (count-1)

    #   * The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(change)
    greatest_increase_index = change.index(greatest_increase)
    greatest_increase_months = months[greatest_increase_index]
    

    #   * The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(change)
    greatest_decrease_index = change.index(greatest_decrease)
    greatest_decrease_months = months[greatest_decrease_index]
    
    print('Financial Analysis')
    print(count)
    print(total_pnl)
    # print(change)
    print(avg_change)
    print(greatest_decrease_months)
    print(greatest_decrease)
    print(greatest_increase_months)
    print(greatest_increase)

          
Fin_Analysis_csv = pathlib.Path('**PyBank**/Analysis/Fin_Analysis.txt')

with open(Fin_Analysis_csv,'w') as outputfile:
 

    Fin_Analysis = (
    f"\n\nFin_Analysis\n"
    f"--------------------\n"
    f"Total Votes: {total_count}\n"
    f"--------------------\n"
    )   
    print(election_results, end="")

    # outputfile.write(election_results)

    # for candidate in votes_summary.keys():
    #     voter_output = f"{candidate}: {votes_summary[candidate]['vote_pct']}% ({votes_summary[candidate]['votes']})\n"
    #     print(voter_output, end="")

    #     outputfile.write(voter_output)


    # winning_candidate_summary = (
    #     f"--------------------\n"
    #     f"Winner: {winner}\n"
    #     f"--------------------\n"
    # )
    # outputfile.write(wining_candidate_summary)

    # print(winning_candidate_summary)