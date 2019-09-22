import os
import csv

#find the election data csv file
election_data = os.path.join("..", "Resources","election_data.csv")

#read the election data csvfile
with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#sets variables to zero and initializes lists
    votercounter = 0
    candidatelist = []
    candidateandvote = {}
    max_votes = 0

#runs through each line of the file    
    for row in csvreader:
        #adds one to vote counter
        votercounter = votercounter + 1
        #add name to candidate list if it is a new name
        if (row[2]) not in candidateandvote:
            #making a list of the candidates
            candidatelist.append(row[2])
            #making the candidate and vote count dictionary
            candidateandvote[row[2]] = +int(0)
        else:
            candidateandvote[row[2]] +=1
    
    max_votes = max(candidateandvote, key=lambda x: candidateandvote.get(x))

    print("Election Results")
    print("------------------------------------")
    print("Total Votes:" + str(votercounter))
    print("------------------------------------")
    for k, v in candidateandvote.items():
        print(str(k)+ ":" + " " + str(round((int(v) / int(votercounter)*100),3)) + "%  " + (str(v)))

    print("------------------------------------")
    print("Winner:" + str(max_votes))
