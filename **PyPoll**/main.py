#import pathlib module
import pathlib
import csv

#create filepath for resource raw data
csvpath = pathlib.Path('Resources/election_data.csv')

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile)
        csv_header = next(csvfile)
        
        votes = {}

        for row in csvreader:

            #candidates vote count
            name = row[2]
     
            if name in votes:
                votes[name] += 1
            else:
                votes[name] = 1

# print(votes)  
numberof_votes = (list(votes.values()))

#total number of votes cast
total_count = sum(numberof_votes)
# print(total_count)

winner = list(votes.keys())[0]
voting_summary = {}
for candidate in votes.keys():
    if votes[candidate] > votes[winner]:
        winner = candidate
    voting_summary[candidate] = {'votes': votes[candidate], 'vote_pct': round((votes[candidate]/total_count)*100,2),}
    if candidate == winner:
        voting_summary[candidate]["is_winner"] = True
    else:
        voting_summary[candidate]["is_winner"] = False



election_results_csv = pathlib.Path('Analysis/election_results.txt')
#write formated results to txt file in analysis folder
with open(election_results_csv,'w') as outputfile:
    # csvwriter = csv.writer(outputfile)

    election_results = (
    f"\n\nElection Results\n"   
    f"--------------------\n"
    f"Total Votes: {total_count}\n"
    f"--------------------\n"
    )   
    print(election_results, end="")

    outputfile.write(election_results)

    for candidate in voting_summary.keys():
        voter_output = f"{candidate}: {voting_summary[candidate]['vote_pct']}% ({voting_summary[candidate]['votes']})\n"
        print(voter_output, end="")

        outputfile.write(voter_output)


    election_winner = (
        f"--------------------\n"
        f"Winner: {winner}\n"
        f"--------------------\n"
    )
    outputfile.write(election_winner)

    print(election_winner)

