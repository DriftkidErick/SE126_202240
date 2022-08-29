import csv

id = []
name = []
age = []
color = []

records = 0 

with open("C:/Users/008004507/Desktop/SE126_202240/binarysearch/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        id.append(rec[0])
        name.append(rec[1].lower())
        age.append(rec[2])
        color.append(rec[3].lower())

print("Finished processing file. There are {} records".format(records))



#Binary Search Algorithm:

search = input("Get search from user! Enter LAST name: ").lower()

min = 0

max = records - 1       #can also use len(listName) for 'records' value

guess = int((min + max) / 2)

#this is for INCREASING order

search_count = 0

while (min < max and search != name[guess]):

    search_count += 1

    if search < name[guess]:

        max = guess - 1

    else:

        min = guess + 1

    guess = int((min + max) / 2)

if search == name[guess]:

    #found them! use 'guess' for index of found search item
    print("Your search for {} was Found at Index: {} ".format(search, guess))

else:

    #boooo not found
    print("Your search for {} was not FOUND".format(search))

print("BINARY SEARCH LOOPS: {}".format(search_count))