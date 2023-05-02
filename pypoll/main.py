import csv
import os
# Create a dictionary 
candidate_votes = {}

# Create a counter variable 
total_votes = 0

csvpath ="C:/Users/dgnil/Desktop/Homework/03-Python/python-challenge/PyPoll/Resources/election_data.csv"
# Open the CSV file and read its contents
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip the header row

    for row in reader:
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
        total_votes += 1

print("Election Results")

        # Print the total number of votes 
print(f"Total votes: {total_votes}")

print("----------------------------")

# Print the results
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {votes} vote{'s' if votes != 1 else ''} ({percentage:.1f}%)")

# find the winner
winner = max(candidate_votes, key=candidate_votes.get)


print("----------------------------")

# Print the winner
print(f"\nWinner: {winner}")

print("----------------------------")

 # Export the results to a text file
with open("output.txt", "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")