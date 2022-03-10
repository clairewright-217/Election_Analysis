# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Module3Python/Election_Analysis/Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Module3Python/Election_Analysis/analysis","election_analysis.txt")

# Initialize the total vote counter
total_votes = 0
# Candidate options and candidate votes. WHAT IS THE POINT OF CANDIDATE_OPTIONS, WE NEVER REALLY USE IT
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers = next(file_reader)

    # Print each row after header in the CSV file
    for row in file_reader:
        # Add the total vote count
        total_votes += 1
        # Get the candidate name from each row
        candidate_name = row[2]
        # If the candidate name does not match any existing options, add to candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count in dictionary
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name]  += 1

    # Save the results to our text file.
    with open(file_to_save,"w") as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        #Save the final vote count to the text file.
        txt_file.write(election_results)

        #   WHY IF CHANGE CANDIDATE_NAME VARIABLE IT DOESN'T WORK
        for candidate_name in candidate_votes:
            # Retrieve the vote count and percentage
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes)/float(total_votes)*100

            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

            # Determine the winning vote count, winning percentage, and candidate.
            if (votes>winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

        
        
            #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.") 

        # Print winning candidate's results to the terminal.
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)
    
    #print(winning_candidate_summary)  
      

