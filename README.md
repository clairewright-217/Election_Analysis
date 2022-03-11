# Election_Analysis

## Project Overview
A Colorado Board of Elections employee needs help to complete an election audit of the recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who receieved votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Get a unique list of counties where voting occurred. 
7. Caculate the total number of votes from each county. 
8. Calculate the percentage of votes from each county.
9. Determine which county had the largest voting turnout.


## Resources
Data Source: election_results.csv
Software: Python 3.9.7, Visual Studio Code, 1.64.2 (Universal)

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11.606 votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
- The counties were:
    - Jefferson
    - Denver
    - Arapahoe
- The county results were:
    - Jefferson county had 10.5% of the vote and 38,855 votes.
    - Denver county had 82.8% of the vote and 306,055 votes.
    - Arapahoe county had 6.7% of the vote and 24,801 votes.
- The county with the highest turnout was Denver.

## Overview of Election Audit
The challenge for this Python lesson was to obtain the voter turnout and percentage of votes of each county in the election, and then determine the county with the highest voter turnout. This built on the same coding techniques that were needed to calculate similar voting metrics for the election candidates (total votes and percentage of votes per candidate, and the winning candidate), as presented in Module 3.  The deliverables of this analysis were to print the results both on the command line and in a separate text file. 

The data file provided for this analysis was a [csv file](Resources/election_results.csv) with three columns: Ballot ID, County, and Candidate. The analysis was done in a python file (`.py`), and then it prints to both the terminal and a seperate text file (`.txt`) when the python file is run. 


## Election Audit Results

The first step in analyzing the election results in Python was to import the `csv` and `os` modules, which were important python dependencies needed for our analysis. The `os` module was used to open the csv file without needing to know the direct path, making it a more robust way to share this code with others to run the same analysis. The `os` module was also used to provide the indirect path to the [text file](analysis/election_analysis.txt) where the analysis summary was written, and to write to this file.


How many votes were cast in this congressional election?
### Calculating Total Votes Cast

The first analysis done was to determine how many votes were cast in the congressional election. Based on a quick, manual evaluation of the data in the Election Results csv file, it had a header row for Ballot ID, County, and Candidate, and then thousands of lines of data with this information. Therefore, each row below the header repesented one vote in the election. 

First, a variable was created outside a `for` loop to store the total votes. Then, the csv file was opened using a `with` statement, and the `csv` module was used with the `.reader` function to read through each row. The `next` function in Python was used to skip the header row and exclude it from our count. Finally, the `+=` operator was used to add each row the count of the variable tracking the total votes. 

```
total_votes = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        total_votes = total_votes + 1
```

While looping through each row in the csv file, two blocks of conditional statements were used after the `for` loop to create a unique `list` of candidate names and counties. The `list` of counties and `list` of candidates then served as `keys` within the two distinct dictionaries that stored the votes per county and votes per candidate. Another `+=` operator was used to tally each vote per county to the corresponding `key` within the `county_votes` dictionary. Here is a code sample for creating a dictionary of votes per county based reading through each row of the csv file within a `for` loop.

```
county_list = []
county_votes = {}

# other code not shown here

 for row in reader:
 
 # other code not shown here
 
     county_name = row[1]
     
     if county_name not in county_list:
                
                county_list.append(county_name)
                county_votes[county_name] = 0
            
            county_votes[county_name] += 1
```

### Calculating the number and the percentage of total votes for each county in the precinct.

Now that a dictionary was created that stored each unique county as a `key` and the total number of votes per county as the `value` after the first `for` loop completed, it was possible to show the total and percentage of total votes by county.

Another `for` loop was used to iterate through the dictionary of votes per county. New variables were created to store the total number of votes per each county, and then use basic math to calculate the percentage of votes by dividing this number into the total votes previously calculated. 

```
for county_name in county_votes:
       
        cvotes = county_votes.get(county_name)
        
        cvotes_percentage = float(cvotes) / float(total_votes)*100
```

A conditional was used in this `for` loop to find the vote count and the name of the county with the highest turnout. 

```
 if cvotes > winning_county_count:
    winning_county_count = cvotes
    winning_county = county_name
```
            

The values of all of the `winning_county` variable from the conditional above was printed to the terminal and on the [Election Analysis text file](analyis/election_analysis.txt) in a formatted style using an f-string. 

```
 winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary) 
```

The output to the terminal and text file shows that Denver had the largest turnout: 

**Largest County Turnout: Denver**

### The number and percentage of votes each candidate received

Using similar methods, the performance of each candidate who participated in the congressional election was evalauted. We can see from the analysis output that 369,711 ballots were cast, and that Raymon Anthony Doane recieved just 3.1% of the vote, while Diana DeGette received a full 73.8% of the vote. Charles Casper Stockham finished in the middle with 23.0% of the vote. 

> Total Votes: 369,711
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

This shows that Diana DeGette won the election:

**Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%**

