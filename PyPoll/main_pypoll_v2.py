# Import os and csv modules.
# Store csvpath.
# Open the csvfile and read it with csvreader variable.
# Read the header as csv_header.
# Create a candidate_list that stores all candidates names. Use a loop that go through all csv rows, storing index[2] on the new list.
# Calculate the total votes using the len function on candidate_list.
# Create a loop and conditional to store a candidate_dic with key as candidate name and value as total votes.
# Convert candidate_dic into two separate list: one for key pairs(list_candidates), another for values (candidates_votes).
# Using list_candidates, calculate list_percentage that hold the percentage of votes for each candidate.
# Calculate the maximum value of list_candidates and the index number to find the winner.
# Print to Git Bash
# Print to "Output.txt" file.

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
        
    list_candidates = [candidate for candidate in candidate_dic.keys()]
    candidates_votes = list(candidate_dic.values())
    list_percentage = [round(float((votes/len(candidate_list)*100)),3) for votes in candidate_dic.values()]
    
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

# open the output text file in "Writting Mode"
with open(output_file, "w") as datafile:

# Text Print

    print("Election Results",file = datafile, end="\n")
    print("-------------------------------------", file = datafile, end="\n")
    print(f"Total Votes: {len(candidate_list)}", file = datafile, end="\n")
    print("--------------------------------------",file = datafile, end="\n")

    # Loop through list range to find each index name

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

   
 
