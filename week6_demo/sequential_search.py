#Week 6 Day 2 Demo

#BASE Program ---------------------------------------------------------------------------

import csv

id = []
name = []
age = []
color = []

records = 0 

with open ("C:/Users/008004507/Desktop/SE126_202240/week6_demo/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records +=1

        id.append(rec[0])
        name.append(rec[1].lower())
        age.append(rec[2])
        color.append(rec[3].lower())

print("Finished processing file. There are {} records".format(records))

for i in range(0,records):

    print("Index: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i].title(), age[i], color[i].title()))

print("\n\n\n")


answer = "y"

while answer == "y":

    search_count = 0

    #request search parameter
    search = input("Enter the full lastname of the records you are looking for: ").lower()
    found = -1 #found is -1 because this is NOT a valid index

    #this is the sequential searching loop
    for i in range(0,records):

        search_count +=1 #count how many iterations of loop search perfroms

        #'Search' through list items for requested info
        if search == name[i]:
            
            #every time above condition is true, we will display to the user all of the info
            #print("Index: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i], age[i], color[i]))

            found = i

        #else:
            #print("Your search for '", search,"' was NOT FOUND")
    
    print("\n\nSEQUENTIAL SEARCH COMPLETE")

    if found >= 0:
        print("Your search for '", search,"' was FOUND on Index {}".format(found))
        print("Index: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(found, id[found], name[found].title(), age[found], color[found]))

    else:
        print("Your search for '", search,"' was NOT FOUND")

    print("Search Loop Iterations Performed: {}".format(search_count))

    answer = input("\nEnter 'y' to search again: [y/n] ").lower()

    while answer !="y" and answer != "n":
        print("ERROR")
        answer = input("\nEnter 'y' to search again: [y/n] ").lower()

print("\n\n\t\tThanks for using my program! Bye =D!")



