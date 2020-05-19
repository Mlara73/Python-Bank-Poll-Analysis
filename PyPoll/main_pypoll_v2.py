# import os and csv modules.
# strore csvpath.
# open the csvfile and read it with csvreader variable.
# read the csv_header
# create a candidate_list that stores all candidates. Use a loop that go through all rows[2].
# calculate the total votes on (len(candidate_list)) to store the total votes cast.
# create a loop to store a dictionary with key as candidate name and valua as total votes.
# convert the above dictionary into separate list (values, keys)
# calculate the max number of votes to define the winner
# print to terminal
# print to text

#modules import

import os
import csv

#csvpath store

csvpath = os.path.join("Resources","election_data.csv")

# Lists and Dictionaries

candidate_list = []
candit_list = []
candidate_dic = dict()

#open and read the csvfile

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

#Header

    csv_header = next(csvreader)

#Candidates lists: this will output the total votes

    for row in csvreader:
        candidate_list.append(row[2])
    
# Candidates and votes

# A Loop through candidate_list, checking if the candidate exists in the dictionary

    for candidate in candidate_list:
        if candidate in candidate_dic:
            candidate_dic[candidate] += 1
        else:
            candidate_dic[candidate] = 1

# List creation per percentage, candidate names, and votes per candidate.
        
    list_percentage = [round(float((votes/len(candidate_list)*100)),3) for votes in candidate_dic.values()]
    list_candidates = [candidate for candidate in candidate_dic.keys()]
    candidates_votes = list(candidate_dic.values())

#From the above lists
    winner_votes = max(candidates_votes)
    winner_index = (candidates_votes.index(winner_votes))
    winner_name = list_candidates[winner_index]

# Print to terminal

    print("Election Results")
    print("-------------------------------------")
    print(f"Total Votes: {len(candidate_list)}")
    print("--------------------------------------")
    for item in range(len(list_candidates)):
        list_percentage[item] = format(list_percentage[item],'.3f')
        print(f"{list_candidates[item]} : {list_percentage[item]}% ({candidates_votes[item]})")
    print("--------------------------------------")
    print(f"Winner: {winner_name}")
    print("--------------------------------------")
    
# Writting results to text

# save the output file path
output_file = os.path.join("Analysis","output.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:

# Text Print

    print("Election Results",file = datafile, end="\n")
    print("-------------------------------------", file = datafile, end="\n")
    print(f"Total Votes: {len(candidate_list)}", file = datafile, end="\n")
    print("--------------------------------------",file = datafile, end="\n")

# Loo through list range to find each index name

    for items in range(len(list_candidates)):
        list_percentage[item] = format(float(list_percentage[items]),'.3f')
        print(f"{list_candidates[items]} : {list_percentage[item]}% ({candidates_votes[item]})", file = datafile, end="\n")
    print("--------------------------------------", file = datafile, end="\n")
    print(f"Winner: {winner_name}", file = datafile, end="\n")
    print("--------------------------------------", file = datafile, end="\n")   

# # Set of candidates
#     cand_set = set(candidate_list)
#     for candidate in cand_set:
#         candit_list.append(cand_set)
#     print(candit_list)
