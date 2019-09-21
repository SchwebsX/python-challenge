import os
import csv

#find the budget data csv file
budget_data = os.path.join('..', "Resources", "budget_data.csv")

#read the budget data csvfile
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#set row counter to zero
    monthcounter = 0
    totalprofit = 0
    changes = []
    monthandchg = {}
    lastrowprofit = 0
    change = 0

#searching rows with a for loop
    for row in csvreader:        
           month = row[0]
           profit = row[1]
           #calc profit change
           change = int(profit) - int(lastrowprofit)
           #putting profit change in a list
           changes.append(change)
           #incrementing monthcounter
           monthcounter = monthcounter + 1
           #adding up profit
           totalprofit = int(totalprofit) + int(row[1])  
           #appending month and profit to dict
           monthandchg[int(change)] = str(month)
           lastrowprofit = row[1]   
    
    chgsum = sum(changes)
    mxval = max(changes)
    mxmonth = (monthandchg.get(mxval))
    minval = min(changes)
    minmonth = (monthandchg.get(minval))
    
    #print(monthandchg)
     
    print("Total Months:" + str(monthcounter))
    print("Total Profit:" + str(totalprofit))
    print("Average Profit Chg:"+ str(chgsum / monthcounter))
    print("Greatest increase in profits:" + str(mxmonth) +" " + str(mxval))
    print("Greatest decrease in profits:" + str(minmonth) +" " + str(minval))
     

      

