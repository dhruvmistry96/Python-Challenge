import os
import csv
#import pandas
#from pandas import DataFrame

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    
    csv_header = next(csvreader)
    
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    Tooley_Votes = 0
    totalcount = 0
    max_votecount = 0
    
    def percentage (part, whole):
        return 100 * float(part)/float(whole)
    
    for row in csvreader:
        voterid = row[0]
        country = row[1]
        candidate = row[2]
        # Find Total Vote Count
        totalcount = totalcount + 1

        # Find votecount by candidates
        if candidate =="Khan":
           Khan_votes = Khan_votes + 1
        if candidate =="Correy":
           Correy_votes = Correy_votes + 1
        if candidate =="Li":
           Li_votes = Li_votes + 1
        if candidate =="O'Tooley":
           Tooley_Votes = Tooley_Votes + 1
           
        candidatevote = {"Khan": Khan_votes,"Correy": Correy_votes,"Li" :Li_votes, "O'Tooley": Tooley_Votes}
     # Find winner 
        for candidate, value in candidatevote.items():
          if value > max_votecount:
            max_votecount = value
            winner = candidate
                
    
print(f'Election Results'+'\n')
print(f'-------------------------------'+'\n')
print(f'Total Votes:'+str(totalcount)+'\n')
print(f'-------------------------------'+'\n')

print(f'Khan: {percentage(Khan_votes,totalcount):.3f}%  ({Khan_votes})')
print(f'Correy: {percentage(Correy_votes,totalcount):.3f}%  ({Correy_votes})')
print(f'Li: {percentage(Li_votes,totalcount):.3f}%  ({Li_votes})')
print(f'O\'Tooley: {percentage(Tooley_Votes,totalcount):.3f}%  ({Tooley_Votes})')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')
