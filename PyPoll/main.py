# Modules
import os
import csv

# Lists to store data
VoterID = []
County = []
Candidate = []
totalVotes = 0

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first
    csv_header = next(csvreader)

    # start iteration to add to list for date, PNL, and total months
    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        totalVotes += 1
    Candidate.sort()
    Votes = dict((c,Candidate.count(c),) for c in set(Candidate))
    winner = max(Votes, key=Votes.get)
    #Pair_candidate_VoterID = dict(zip(Candidate,VoterID))

print(
f'''
Election Results
--------------------------
Total Votes: {totalVotes} 
--------------------------'''
        )
pctv=[]
for i in Votes:
    
    pct=f'{(round((Votes[i]/totalVotes),2)*100)}%'
    pctv.append(pct)
    print(i, pct,Votes[i])
print(
f'''
--------------------------
Winner: {winner}
--------------------------'''
)
results = zip(Votes,pctv)
# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Candidate", "Percentage of Vote"])

    writer.writerows(results)
    