#Lab 7 Erick Cordon

#Prompt: Write a program that gives the user a menu of options to search through the file.

#varriable Def():

#Function Def():
import csv

def menu():

    print("SEARCH MENU")
    print("1. Search by FIRST NAME")
    print("2. Search by ID CODE")
    print("3. Search by LAST NAME")
    print("4. Search by ALLEGIANCE")
    print("5. Exit")

    pick = input("Hello, Please make a selection from the following below [1-5]: ")

    while pick != "1" and pick != "2" and pick != "3" and pick !="4" and pick != "5":
        print("\nSorry...An invalid input was made. Please try again")

        pick = input("Hello, Please make a selection friom the following below [1-5]: ")

    return pick

def bubble():
    
    for i in range(0, records - 1):#outter loop

        for index in range(0, records - 1):#inner loop

            if(fname[index] > fname[index + 1]):

                #if above is true, swap places!

                temp = fname[index]

                fname[index] = fname[index + 1]

                fname[index + 1] = temp


                #swap all other values

                temp = age[index]

                age[index] = age[index + 1]

                age[index + 1] = temp

                temp = idP[index]
                idP[index] = idP[index + 1]
                idP[index + 1] = temp

def idbubble():

    for i in range(0, records - 1):#outter loop

        for index in range(0, records - 1):#inner loop

            if(idP[index] > idP[index + 1]):

                #if above is true, swap places!

                temp = fname[index]

                fname[index] = fname[index + 1]

                fname[index + 1] = temp


                #swap all other values

                temp = age[index]

                age[index] = age[index + 1]

                age[index + 1] = temp

                temp = idP[index]
                idP[index] = idP[index + 1]
                idP[index + 1] = temp

def again():

    answer = input("Would you like to add another search? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        print("\nSorry wrong input")

        answer = input("Would you like to add another search? [y/n]: ").lower()

    return answer

def goodbye():

    print("\nThank you for using our program")
    print("\nThe Lannisters send their regards.")

#Main Code Below ------------------------------------------------------------------------------------------

idP = []
lname= []
fname = []
age = []
allegiance = []

records = 0

with open("C:/Users/Erick/Desktop/SE126_202240/w8_labs/GOT_bubble_sort_7.txt") as csvfile:

    csv_reader = csv.reader(csvfile)

    for rec in csv_reader:

        records += 1

        idP.append(rec[0].lower())
        lname.append(rec[1].lower())
        fname.append(rec[2].lower())
        age.append(rec[3])
        allegiance.append(rec[4].lower())

print("------------------------------------------------------------------------------------------------------------------")

print("Index: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}\t{5:15}".format("Num","ID Code","Last Name","First Name","Age","Allegiance"))

print("------------------------------------------------------------------------------------------------------------------")

for i in range(0,records):
    print("Index: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}\t{5:15}".format(i,idP[i].title(),lname[i].title(),fname[i].title(),age[i],allegiance[i].title()))


answer = "y"

while answer == "y":

    print("\n\n")

    choice = menu()

    if choice == "1":

        print("\nYou've selected search FIRST NAME")
        
        sort = bubble()

        search = input("Please enter the FIRST NAME of the person you are looking for: ").lower()

        min = 0 #this is the lowest starting index
        max = records -1 #this is the highest starting index
        guess = int((min + max) // 2) #this is the middle point of the index

        while min < max and search != fname[guess]: 

            if search < fname[guess]:

                max = guess -1

            else:
                min = guess + 1

            guess = int((min + max) / 2)

        if search == fname[guess]:

            print("\n\t\tYour search results for", search,": ")

            print("\t\t\tIndex: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:8}{5:18}".format(guess,idP[guess].title(),lname[guess].title(),fname[guess].title(),age[guess],allegiance[guess].title())) 
        else:
            print("\n\tSorry your search for",search,"could NOT be found")

            print("Please check your spelling")

    if choice == "2":

        print("\nYou are now searching based on ID Code")

        sort = idbubble()

        search = input("\nPlease Enter the ID CODE of the person/people you searhing for: ")

        min = 0
        max = records - 1
        guess = int((min + max) / 2)

        while min < max and search != idP[guess]:

            if search < idP[guess]:

                max = guess - 1
            
            else:

                min = guess + 1 
            
            guess = int((min + max) / 2)

        if search == idP[guess]:

            print("\n\t\tYour search results for", search, ": ")

            print("\t\t\tIndex: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:8}{5:18}".format(guess,idP[guess].title(),lname[guess].title(),fname[guess].title(),age[guess],allegiance[guess].title())) 
        
        else:

            print("\n\t\tYour search for", search," could NOT be found")
            print("\tPlease check for spelling errors")

    if choice == "3":

        print("Search based off of LAST NAME")

        search = input("Please enter the LAST NAME of the person/people you are searching for: ")

        found = []
        f = - 1





    

    answer = again()

done = goodbye()





