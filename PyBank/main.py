# Modules
import os
import csv

# Lists to store data
Dates = []
PNL = []
totalmonths = 0
totalPNL = 0

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first
    csv_header = next(csvreader)

    # start iteration to add to list for date, PNL, and total months
    for row in csvreader:
        Dates.append(row[0])
        PNL.append(row[1])
        totalmonths += 1

    # convert PNL from string to float
    PNL = [float (p) for p in PNL]
    # Create separate PNL list, remove first value. Will be used to 
    # subtract from PNL to find month over month change
    PNL2 = [x for p, x in enumerate(PNL) if p > 0]
    # create list to capture month over month change
    chg = [i - j for i, j in zip(PNL2, PNL)]
    # zip files to allow printing of max/ min change values w/ dates
    pybank = zip(Dates, PNL, chg)
    pybank1 = zip(Dates, chg)
    pybank2 = zip(Dates, chg)
    # assign values
    avgchgPNL = sum(chg)/len(PNL2)
    totalPNL = sum(PNL)
    GIncrease = max(chg)
    GDecrease = min(chg)
    DIncrease = [c for c,d in pybank1 if d == GIncrease]
    DDecrease = [a for a,b in pybank2 if b == GDecrease]
    #DDecrease = [d for d,c in pybank if c == GDecrease]
    
    print(
        f'''
        Financial Analysis
        ---------------------
        Total Months: {totalmonths} 
        Total: ${totalPNL} 
        Average Change: ${avgchgPNL} 
        Greatest Increase in Profits: {DIncrease[0]} (${GIncrease})
        Greatest Decrease in Profits: {DDecrease[0]} (${GDecrease})
         ''')

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Date", "Profit and Lose", "Month over Month Change"])

    writer.writerows(pybank)
