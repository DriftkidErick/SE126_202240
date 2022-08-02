# Class Lab 3, The Python Pals

#Prompt: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective lists, and then process the lists to determine the 5 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 5 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 5 totals.

#----------------------------Main Code Below----------------------------------

noReg = 0 
notOLD = 0 
yesVot = 0
noVot = 0
totalrecs = 0

import csv

with open("/Users/erickcordon/Desktop/SE126_202240/SE126_202240/W3_ClassLab/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        totalrecs += 1

        idnum = rec[0]
        age = int(rec[1])
        reg = rec[2]
        vot = rec[3]

        if age <= 17:
            notOLD += 1
        
        elif reg == "N" and age >= 18:
            noReg += 1
        
        if vot == "Y" and reg == "Y":
            yesVot += 1
        
        if reg == "Y" and vot == "N":
            noVot += 1


#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.


print("\n\tNumber of individuals not eligible to register: {}".format(notOLD))

print("\n\tNumber of individuals who are old enough to vote but have not registered: {}".format(noReg))

print("\n\tNumber of individuals who are eligible to vote but did not vote: {}".format(noVot))

print("\n\tNumber of individuals who did vote: {}".format(yesVot))

print("\nTotal number of records processed: {}".format(totalrecs))


        