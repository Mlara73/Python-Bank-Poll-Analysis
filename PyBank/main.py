# Import Modules csv, os.
# Store Path as csvpath.
# Open and read the file
# read the header
# Create a list for months [0] and profit/losses [1].
# Count months elements using len function.
# The average of the changes in "Profit/Losses" over the entire period (avergae_change)
# The net total amount of "Profit/Losses" over the entire period (average_total)
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

#Lists

months_count = []
profit_losses = []
average_change = []

#Path Storing

csvpath = os.path.join("Resources","budget_data.csv")

# Open and read file

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    

#Header

    csv_header = next(csvreader)

# Months and Profit/Losses Lists

    total_volume = 0
    for row in csvreader:
        months_count.append(row[0])
        profit_losses.append(row[1])
        
# Total Volume Calculation

        total_volume += int(row[1])
    
# Months counting

    total_months = len(months_count)
    

# Average Change

    for row in range(len(profit_losses)):
        if row+1 < len(profit_losses):
            cur = int(profit_losses[row])
            nxt = int(profit_losses[row+1])
            average_change.append(nxt - cur)

# Average Total

    average_total = 0
    for row in range(len(average_change)):
        average_total += average_change[row]
    average_total = (average_total/len(average_change))
    
# Maximum and Minimum Decrease

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

# save the output file path
output_file = os.path.join("Analysis","output.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    print(f"Financial Analysis",file = datafile, end="\n")
    print("----------------------------",file = datafile, end="\n")
    print(f"Total Months: {total_months}",file = datafile,end="\n")
    print(f"Total: ${total_volume}", file= datafile, end="\n")
    print(f"Average Change: ${round(average_total,2)}",file= datafile, end="\n")
    print(f"Greatest Increase in Profits: {month_max} (${max_avg})",file= datafile, end="\n")
    print(f"Greatest Increase in Profits: {month_min} (${min_avg})",file= datafile)
    