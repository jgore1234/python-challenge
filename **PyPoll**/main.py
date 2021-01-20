import pathlib
import csv

#import election data
election_data_csv = pathlib.Path('Resources/election_data.csv')

with open(election_data_csv) as csvfile:
        csvreader = csv.reader(csvfile)
        csv_header = next(csvfile)

        votes = {}

        for row in csvreader:

            #candidates vote count
            candidate_name = row[2]
     
            if candidate_name in votes:
                votes[candidate_name] += 1
            else:
                votes[candidate_name] = 1

# print(votes)  
vote_counts = (list(votes.values()))

#total number of votes cast
total_count = sum(vote_counts)
# print(total_count)

winner = list(votes.keys())[0]
votes_summary = {}
for candidate in votes.keys():
    if votes[candidate] > votes[winner]:
        winner = candidate
    votes_summary[candidate] = {'votes': votes[candidate], 'vote_pct': round((votes[candidate]/total_count)*100,2),}
    if candidate == winner:
        votes_summary[candidate]["is_winner"] = True
    else:
        votes_summary[candidate]["is_winner"] = False

# election_results = (
#     f"\n\nElection Results\n"
#     f"--------------------\n"
#     f"Total Votes: {total_count}\n"
#     f"--------------------\n"
# )   
# print(election_results, end="")

# for candidate in votes_summary.keys():
#     voter_output = f"{candidate}: {votes_summary[candidate]['vote_pct']}% ({votes_summary[candidate]['votes']})\n"
#     print(voter_output, end="")


# winning_candidate_summary = (
#     f"--------------------\n"
#     f"Winner: {winner}\n"
#     f"--------------------\n"
# )
# print(winning_candidate_summary)


election_results_csv = pathlib.Path('Analysis/election_results.txt')

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

    for candidate in votes_summary.keys():
        voter_output = f"{candidate}: {votes_summary[candidate]['vote_pct']}% ({votes_summary[candidate]['votes']})\n"
        print(voter_output, end="")

        outputfile.write(voter_output)


    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winner}\n"
        f"--------------------\n"
    )
    outputfile.write(winning_candidate_summary)

    print(winning_candidate_summary)




#  election_results_csv = pathlib.Path('Pypoll/Resources/election_results.csv')

## {'Khan': {'votes': 2218231, 'vote_pct':...., 'is_winner': True}, 
##'Correy': {'votes': 704200, 'vote_pct':...., 'is_winner': False}, 
## 'Li': {'votes': 492940, 'vote_pct':...., 'is_winner': False},
##  "O'Tooley": {'votes': 105630, 'vote_pct':...., 'is_winner': False}
# }

##   * The percentage of votes each candidate won

# winner = 'list(votes.keys())[0]'





# for candidate in votes_summary.keys():
#     voter_output = f"{candidate}: {votes_summary[candidate]['vote_pct']}% ({votes_summary[candidate][votes]})\n"
#     print(voter_output, end="")

# winning_candidate_summary = (
#     f"Winner: {winner}\n"
# )
#  print(winning_candidate_summary)

#  election_results_csv = pathlib.Path('Pypoll/Resources/election_results.csv')

#  with open(election_results_csv, 'w') as outputfile:
#     #csvwriter = csv.writer(outputfile)
#     election_results = (
#         f"\n\nElection REsults\n"
#     )

#     print(election_results, end="")

#     outputfile.write(election_results)

#     for candidate in votes_summary.keys():
#             voter_output = f"{candidate}: {votes_summary[candidate]['vote_pct']}% ({votes_summary[candidate]['votes']})\n"
#             print(voter)

# 4:41:21

