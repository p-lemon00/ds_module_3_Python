# Read in csv

import csv

# Find
# The total number of votes cast
# A complete list of candidates who received votes


csvpath = "Resources/election_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)

    
    vote_tot = 0
    candi_dict = {}

    
    for row in csvreader:

        vote_tot = vote_tot + 1
        
        county = row[1]
        candidate = row[2]

        if candidate in candi_dict:
            candi_dict[candidate] = int(candi_dict[candidate]) + 1
        
        else:
            candi_dict[candidate] = 1

    
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote
    # Print results then write to a text file
    
    txt = open("analysis/analysis_pypoll.txt", "w")


    print(f"Election Results \n------------------------- \nTotal Votes: {vote_tot} \n-------------------------")
    txt.write(f"Election Results \n------------------------- \nTotal Votes: {vote_tot} \n-------------------------\n")
    
    vote_win = 0

    for x in candi_dict:
            
        vote_count = candi_dict[x]
        perc = (vote_count / vote_tot) * 100
        print(f"{x} : {perc}% ({vote_count})")
        txt.write(f"{x} : {perc}% ({vote_count})\n")

        if candi_dict[x] > vote_win:

            winner = x
            vote_win = candi_dict[x]

    print(f"------------------------- \nWinner: {winner} \n-------------------------")
    txt.write(f"------------------------- \nWinner: {winner} \n-------------------------")

        
