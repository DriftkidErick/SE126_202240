#Python Pals Week 6 Class Lab

#Prompt: Write a Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  You must use the sequential search.  The program should allow the user to search for as many people as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

# Varriable Def:

#lastname = [] last name of student
#firstname = [] first name of student
#dob = [] date of birth 
#record = 0 counting var
#search_count = 0 count total searches
#found = -1 starts a negative one because this is not a valid index

#main code below:

import csv

lastname = []
firstname = []
dob = []

record = 0
search_count = 0


with open("C:/Users/008004507/Desktop/SE126_202240/w6_classlab/lab5_updated.txt") as csvfile:

    file =csv.reader(csvfile)

    for rec in file:
        record += 1

        lastname.append(rec[0].lower())
        firstname.append(rec[1].lower())
        dob.append(rec[2])

print("-------------------------------------------------------------------------------")
print("INDEX: {0} \t{1:15} \t{2:15} \t{3}".format("","Last Name","First Name","Date Of Birth"))
print("-------------------------------------------------------------------------------")


for i in range(0,record): #original data

    print("INDEX: {0} \t{1:15} \t{2:15} \t{3}".format(i, lastname[i].title(),firstname[i].title(),dob[i])) #.title() used to uppercase on display

print("\n\n") #Everything Works Up to Here

answer = "y"#Everything Below Is in Testing Stage

while answer == "y":

    search = input("Enter the lastname of the people you would like to find:  ").lower()

    found = -1 

    for i in range(0,record):

        search_count += 1

        if search == lastname[i]:

            found = i

    print("\n\nSearch Processed")

    if found >= 0: 

        print("Person found ", search, " at INDEX: ", found)

        print("\t\t\t{0:10} \t {1:10} \t {2:10}".format(lastname[found].title(),firstname[found].title(),dob[found]))#.title() uses to upper case in final display

    else:
        print("Your search for ", search, " has NOT BEEN FOUND.")
        print("Please check for errors")

    print("\nLoops preformed for search: {}".format(search_count)) #search counted through loop


    search_count = 0 #this is placed here to reset after a search
    answer = input("\n\nWould you like to add another person? [y/n]:")
    answer = answer.lower()

    while answer != "y" and answer != "n":
        print("**Error**")
        answer = input("\n\nWould you like to add another person? [y/n]:")
        answer = answer.lower()


print("\n\nThank you for using our program =D!!!!\n")


