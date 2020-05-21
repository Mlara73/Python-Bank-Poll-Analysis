# PyBank and PyPoll data parsing with Python

### Overview

###### PyBank and Pypoll were different projects; the first one was to analyze the financial records for a Company X base on the Profit/Losses results dataset provided by the financial department. The second project objective was to automate the votes counting process for a small rural town, based on the Voter ID, County and Candidates. The source dataset for both projects were provided as "CSV" files.

### Objectives

##### PyBank:

###### 1. To calculate the total number of months for the financial records.
###### 2. To totalize the net amount of "Profit/Losses" over the entire period.
###### 3. To calculate the average of changes in "Profit/Losses" over the entire period.
###### 4. To calculate the greatest in profits and the greates decrease in losses over the entire period, defining also the corresponding date and amount.

##### PyPoll:

###### 1. To calculate the total number of votes cast.
###### 2. To generate a list of candidates who received votes.
###### 3. To calculate the total number of votes each candidate won.
###### 4. To calculate the percentage of votes each candidate won.
###### 5. To show the winner candidate based on popular vote.

### Anslysis and Results

###### As a result, the program generates the following analysis as an "output.txt" file (stored on the "Analysis" folder) and at GitBash/Terminal screen:

##### PyBank:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
![PyBank](Images\PyBank_Git_Bash.PNG)

##### PyPoll:
```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```
![PyPoll](Images\PyPoll_Git_Bash.PNG)	

###### For additional information, please see the source code for both programs within PyBank and PyPoll folders
