#Erick Cordon Lab 6

#Prompt: Re-write the Week #5 Class Lab but instead of searching for a person’s name, search for their birthday.  If the person is found, reprint their entire record to the console.  The program should allow the user to search for as many birthdays as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#Varriable Definitions:

#Function Definitions:

#Main Code Below----------------------------------------

import csv
from tkinter import Y

lastname = []
firstname = []
dob = []
records = 0
search_count = 0

with open("C:/Users/Erick/Desktop/SE126_202240/w6_classlab/lab5_updated.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        lastname.append(rec[0])
        firstname.append(rec[1])
        dob.append(rec[2])
    
print("-------------------------------------------------------------------------------")
print("INDEX: {0} \t{1:15} \t{2:15} \t{3}".format("","Last Name","First Name","Date Of Birth"))
print("-------------------------------------------------------------------------------")

for i in range(0,records):

    print("INDEX: {0} \t{1:15} \t{2:15} \t{3}".format(i, lastname[i].title(),firstname[i].title(),dob[i]))

answer = "y"

while answer == "y":

    search = input("Please enter the birthdate you are looking for: ")

    found = -1

    for i in range(0,records):

        search_count += 1

        found = -1 #

        if search == dob [i]:

            found = i #This makes this an index

    print("\n\nSearch is being processed")

    if found >= 0: #This is for when index is found

        print("Person found ", search," at index", found)

        print("\t\t\t{0:10} \t {1:10} \t {2:10}".format(lastname[found].title(),firstname[found].title(),dob[found])) #the found in index will only pring what is found

    else: #this is for errors
        print("Your search for ", search, "has NOT BEEN FOUND")
        print("Please check for any errors")

    print("\nTotal Loops Perfromed for search: {}".format(search_count))

    search_count = 0 #this resets the search count after being used in the varriable

    answer = input("Hey, would you like to add another person? [y/n]: ")
    anwer = answer.lower() #This allows the user to type answer with caps lock

    while answer != "y" and answer != "n": # misinput loop
        print("**Error**")
        answer = input("\n\nWould you like to add another person? [y/n]:")
        answer = answer.lower()

print("\n\nThank you for using our program =D")



