# Election_Analysis

## Project Overview
A Colorado Board of ELections employee needs help to complete an election audit of the recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who receieved votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.


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

## Challenge Overview
The challenge required applying several skills using Python and VS Code to complete, including:
1. Importing and reading csv files in a python file on VS Code, and using dependencies and modeules to do so.

To import and use the data within the csv file, first we had to use the `import os` command to load the `os` module. Then we had to locate the path to the csv file for the `os` module to help us open it:

> `file_to_load = os.path.join("Resources", "election_results.csv")` 

Later on, I used the `with` plus `as` commands to open the csv file as a new variable called `election_data`, and then I used the `reader` command from the `csv` module to read the csv file:

> with open(file_to_load) as election_data:
    >file_reader = csv.reader(election_data)

2. Creating new txt files and writing to them directly from a python file

The following line created a `txt` file in the specified directory based on the local path I provided:

> file_to_save = os.path.join("analysis", "election_analysis.txt")

I had to create a new folder, "analysis", on my computer for the path to this location to work. In parallel to opening a csv file to read it, I used the `with` plus `as` commands to be able to write in the newly created `txt` file where I stored my election analysis:

> with open(file_to_save, "w") as txt_file:

4. Using for loops and conditionals to read through the csv file and perform analysis on the data

I used the `next` function to skip the first row of data in the csv file, which was the header row of the columns of data. I only wanted to analyze the data that fell below the headers. Also, I used the `+=` syntax to count through all of the rows in the for loop to total them up, which represented the total number of votes. Finally I used an `if` statement to build up a list of unique candidate names so I could loop through the candidate list later on in the code and tally their votes individually. 

```
 with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    
    for row in file_reader:
    
       total_votes += 1
       candidate_name = row[2]
       
       if candidate_name not in candidate_options:
       
           candidate_options.append(candidate_name)
           
           # And begin tracking that candidate's voter count.
           
           candidate_votes[candidate_name] = 0
           
       candidate_votes[candidate_name] += 
```

5. Using f-strings to print out data summaries with a mix of strings and variables. Variables are written inside squiggly brackets, `{}`.

f-strings enable variables to be included within strings and for the variables to be printed out as strings. For example, in the following code, an f-string is used: 

```
txt_file.write(election_results)
  for candidate_name in candidate_votes:
     # Retrieve vote count and percentage.
     votes = candidate_votes[candidate_name]
     vote_percentage = float(votes) / float(total_votes) * 100
     candidate_results = (
         f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
```            

An example output that would be written in the specified `txt` file from the code above would looke like:

>Charles Casper Stockham: 23.0% (85,213)


## Challenge Summary

The challenge required a number of relevant Python skills to be used in order to complete the election analysis. I liked having to think through the logic of how variables were assigned and calculated within a `for` loop. One major challenge I had was around the spacing of code blocks; my code was broken for a while because of improper indentation of a particular function. Debugging indentation issues in Python can be tricky. 

