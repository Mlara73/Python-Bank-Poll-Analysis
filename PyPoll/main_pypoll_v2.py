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

#Modules import

import os
import csv

#csvpath store

csvpath = os.path.join("Resources","election_data.csv")

# Lists and Dictionaries

candidate_list = []
candit_list = []
candidate_dic = dict()

#Open and read csvfile

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

#Read the header

    csv_header = next(csvreader)

#Candidates list from csvfile

    for row in csvreader:
        candidate_list.append(row[2])
    
# Candidates and votes
# A Loop through candidate_list, checking if the candidate exists in candidate_dic

    for candidate in candidate_list:
        if candidate in candidate_dic:
            candidate_dic[candidate] += 1
        else:
            candidate_dic[candidate] = 1

# Lists to store candidates names (list_candidates), total votes per candidates (candidates_votes), and votes percentage per candidat(list_percentage)
        
    list_candidates = [candidate for candidate in candidate_dic.keys()]
    candidates_votes = list(candidate_dic.values())
    list_percentage = [round(float((votes/len(candidate_list)*100)),3) for votes in candidate_dic.values()]
    
# Determining the max number within candidates_votes lists
    winner_votes = max(candidates_votes)
#Determining the index for the max votes number
    winner_index = (candidates_votes.index(winner_votes))
# Matching the winener index within list_candidates
    winner_name = list_candidates[winner_index]

# Printing to git bash

    print("Election Results")
    print("-------------------------------------")
    print(f"Total Votes: {len(candidate_list)}")
    print("--------------------------------------")
# Loop to print indexes from list_percentage, list_candidates, candidates_votes
    for item in range(len(list_candidates)):
        list_percentage[item] = format(list_percentage[item],'.3f')
        print(f"{list_candidates[item]} : {list_percentage[item]}% ({candidates_votes[item]})")
    print("--------------------------------------")
    print(f"Winner: {winner_name}")
    print("--------------------------------------")
    
# Writting results to text
# Save the output file path
output_file = os.path.join("Analysis","output.txt")

# Open the output text file in "Writting Mode"
with open(output_file, "w") as datafile:

# Text file print

    print("Election Results",file = datafile, end="\n")
    print("-------------------------------------", file = datafile, end="\n")
    print(f"Total Votes: {len(candidate_list)}", file = datafile, end="\n")
    print("--------------------------------------",file = datafile, end="\n")

# Loop to print indexes from list_percentage, list_candidates, candidates_votes

    for items in range(len(list_candidates)):
        list_percentage[item] = format(float(list_percentage[items]),'.3f')
        print(f"{list_candidates[items]} : {list_percentage[item]}% ({candidates_votes[item]})", file = datafile, end="\n")
    print("--------------------------------------", file = datafile, end="\n")
    print(f"Winner: {winner_name}", file = datafile, end="\n")
    print("--------------------------------------", file = datafile, end="\n")   

Testing
# # Set of candidates
#     cand_set = set(candidate_list)
#     for candidate in cand_set:
#         candit_list.append(cand_set)
#     print(candit_list)

   
 
