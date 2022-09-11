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

def bubble(index):


    if(fname[index] > fname[index + 1]):

        #if above is true, swap places!

        temp = fname[index]

        fname[index] = fname[index + 1]

        fname[index + 1] = temp


        #swap all other values

        temp = age[index]

        age[index] = age[index + 1]

        age[index + 1] = temp

        temp = lname[index]
        lname[index] = lname[index + 1]
        lname[index + 1] = temp


def again():

    answer = input("Would you like to go again? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        print("\nSorry wrong input")

        answer = input("Would you like to go again? [y/n]: ").lower()

    return answer

def goodbye():

    print("\nThank you for using our program")
    print("\nThe Lannisters send their regards.")

#Main Code Below ------------------------------------------------------------------------------------------

id = []
lname= []
fname = []
age = []
allegiance = []

records = 0

with open("C:/Users/Erick/Desktop/SE126_202240/w8_labs/GOT_bubble_sort_7.txt") as csvfile:

    csv_reader = csv.reader(csvfile)

    for rec in csv_reader:

        records += 1

        id.append(rec[0].lower())
        lname.append(rec[1].lower())
        fname.append(rec[2].lower())
        age.append(rec[3])
        allegiance.append(rec[4].lower())

print("------------------------------------------------------------------------------------------------------------------")

print("Index: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}\t{5:15}".format("Num","ID Code","Last Name","First Name","Age","Allegiance"))

print("------------------------------------------------------------------------------------------------------------------")

for i in range(0,records):
    print("Index: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}\t{5:15}".format(i,id[i],lname[i],fname[i],age[i],allegiance[i]))


answer = "y"

while answer == "y":

    print("\n\n")

    choice = menu()

    if choice == "1":
        for i in range(0 , records -1):

            for index in range(0, records - 1):

                sort = bubble(index)

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

            print("Index: {0}\t{1:15}\t{2:15}\t{3:8}\t{4:18}".format(i[i],lname[i],fname[i],age[i],allegiance[i])) #this is the print error location

        else:
            print("\n\tSorry your search for",search,"could NOT be found")

            print("Please check your spelling")

    

    answer = again()

done = goodbye()


#add a bubble search fuynction




