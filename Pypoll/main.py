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
        #looping through candidateandvote dict to add up votes
    #for row in csvreader:   
        #if (row[2]) in candidateandvote:
            #candidateandvote[names] += 1

    print("Election Results")
    print("------------------------------------")
    print("Total Votes:" + str(votercounter))
    print("------------------------------------")
    for k, v in candidateandvote.items():
        print(str(k)+ ":" + " " + str(v))

    print("------------------------------------")
    print("Winner:")
  