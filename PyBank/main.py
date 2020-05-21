# Import csv, os modules
# Store csvpath.
# Open, read the csvfile.
# Read the csv_header.
# Create months_count and profit_losses list looping through the csvfile.
# Calculate total_months with len funcion.
# Calculate total_volume over profit_losses list.
# Create a list to store the average_change, looping through the profit_losses list, calculating the change between each period.
# Calculate the average_total for the entire period.
# Calculate the max_avg in profits using the max function with the average_change list. Calculate index_max to match the month_max.
# Calculate the min_avg in profits using the min function with the average_change list. Calculate index_min for to match the month_mix.
# Print the results to git bash and text file as "output.txt"

#Importing modules

import os
import csv

#Lists

months_count = []
profit_losses = []
average_change = []

#Storing csvpath

csvpath = os.path.join("Resources","budget_data.csv")

# Opening and reading csvfile

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    

#Reading the csv_header

    csv_header = next(csvreader)

# Creating lists for months count and profit_losses

    total_volume = 0
    for row in csvreader:
        months_count.append(row[0])
        profit_losses.append(row[1])
        
# Calculating the total volume

        total_volume += int(row[1])
    
# Counting months with "len" function

    total_months = len(months_count)
    

# Calculating the average change between each period

    for row in range(len(profit_losses)):
        if row+1 < len(profit_losses):
            cur = int(profit_losses[row])
            nxt = int(profit_losses[row+1])
            average_change.append(nxt - cur)

# Calculating the average total for the entire period

    average_total = 0
    for row in range(len(average_change)):
        average_total += average_change[row]
    average_total = (average_total/len(average_change))
    
# Calculating max average, min average and corresponding indexes to search the respectively month

    max_avg = max(average_change)
    index_max = average_change.index(max_avg)
    month_max = months_count[index_max+1]
    min_avg = min(average_change)
    index_min = average_change.index(min_avg)
    month_min = months_count[index_min+1]
    
# Git Bash Results

print(f"Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_volume}")
print(f"Average Change: ${round(average_total,2)}")
print(f"Greatest Increase in Profits: {month_max} (${max_avg})")
print(f"Greatest Increase in Profits: {month_min} (${min_avg})")

# Writting results to text
# Saving the output_file path

output_file = os.path.join("Analysis","output.txt")

# Opening the output_file and printing results:

with open(output_file, "w") as datafile:
    print(f"Financial Analysis",file = datafile, end="\n")
    print("----------------------------",file = datafile, end="\n")
    print(f"Total Months: {total_months}",file = datafile,end="\n")
    print(f"Total: ${total_volume}", file= datafile, end="\n")
    print(f"Average Change: ${round(average_total,2)}",file= datafile, end="\n")
    print(f"Greatest Increase in Profits: {month_max} (${max_avg})",file= datafile, end="\n")
    print(f"Greatest Increase in Profits: {month_min} (${min_avg})",file= datafile)
    