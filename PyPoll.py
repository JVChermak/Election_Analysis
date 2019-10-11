# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# Add our dependencies
import csv
import os
# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to a direct or indirect path to a file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize list for Candidate Options.
candidate_options = []
# Create empty dictionary for candidates and votes.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and perform analysis
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row in the CSV file.
    headers = next(file_reader)
    # Print each row in the csv file
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name from each row.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# Print the candidate list.
print(candidate_options)        
# Print the candidate vote dictionary.
print(candidate_votes)
# Print the total votes.
print(total_votes)

# Determine the percentage of cotes for each candidate by looping through counts.
for candidate in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100
    # Print the candidate name, vote count, and percentage of votes.
    print(f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')

    # Determine winning vote count and candidate.
    # Determine if the voters are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage
        winning_counts = votes
        winning_percentage = vote_percentage
        # Set the winning candidate equal to the candidate's name.
        winning_candidate = candidate
winning_candidate_summary = (
    f"-------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_counts:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------------\n")
print(winning_candidate_summary)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")