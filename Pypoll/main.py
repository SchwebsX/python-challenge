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
    candidatesvotes = 0

#runs through each line of the file    
    for row in csvreader:
        #adds one to vote counter
        #candidatelist.append(row[2])
        votercounter = votercounter + 1
        #add name to candidate list if it is a new name
        if (row[2]) not in candidateandvote:
            candidatelist.append(row[2])
            
            candidateandvote[row[2]] = +int(0)
        for names in candidateandvote:
            if (names in candidateandvote):
                candidateandvote[names] += 1
            #else:
                #candidateandvote[names] = 0
    
    
    #trying to count elements in a dictionary
    

        #else:
            #addup[names] = 1
    
    #for key, value in addup.items():
       # print("%d : %d"%(str(key, value))

    print("Election Results")
    print("------------------------------------")
    print("Total Votes:" + str(votercounter))
    print("------------------------------------")
    for k, v in candidateandvote.items():
        print(str(k)+ ":" + " " + str(v))

    print("------------------------------------")
    print("Winner:")
    #print(candidate)
    #print(candidateandvote)