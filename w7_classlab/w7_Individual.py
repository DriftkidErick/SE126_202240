#Lab 6A Erick Cordon

#prompt: Write a Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  You must use the binary search method. The program should allow the user to search for as many people as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#Varriables:

#lname = [] empty list for last name
#fname = [] empty lsit for first name
#dob = [] empty list for date of birth 

#Main Code Below----------------------------------------

import csv 

lname = []
fname = []
dob = []

records = 0 #counting var
search_count = 0

with open ("C:/Users/Erick/Desktop/SE126_202240/w7_classlab/lab6A.txt") as csvfile:
    
    file = csv.reader(csvfile) 

    for rec in file:

        records += 1 # adds + 1 to counting var for during each loop

        #appends each list to appropriate colum in csv
        lname.append(rec[0].lower())   
        fname.append(rec[1].lower())
        dob.append(rec[2])

print("\n\n\nFile processing is done. There are {} records".format(records))

print("----------------------------------------------------------")

print("----------------------------------------------------------")

for i in range(0,records):
    print("Index:{} \t{:15}\t{:15}\t{:10}".format(i,lname[i].title(),fname[i].title(),dob[i]))

answer = "y"

while answer == "y":

    search = input("Please enter the LAST NAME you are searching for: ").lower()

    min = 0 

    guess = int((min + max) /2 )

    while min < max and search != lname [guess]:

        if search < lname[guess]:

            max = guess - 1

        else:

            min = guess + 1
        
        guess = int((min + max) / 2)

    if search == lname[guess]:

        print("\n\n\tYour search for", search,": ")

        print("\n\tIndex: {3}\t{0:15}\t{1:15}\t{2:5}".format(lname[guess].title(), fname[guess].title(), dob[guess], guess))


    else:

        print("\t\tYour search for",search,"was not found")
        print("Please check your spelling for any erorrs")


    answer = input("\n\nWould you like to search for another name [y/n]: ").lower()

    while answer != "n" and answer != "y":
        print("\t\t **ERROR** Sorry Invalid Entry")
        answer = input("\nWould you like to search for another name [y/n]: ").lower()


print("Thank you for using our program")
