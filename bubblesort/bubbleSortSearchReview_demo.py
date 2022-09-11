import csv

records = 0 

lastname = []
firstname = []
age = []

with open("C:/Users/Erick/Desktop/SE126_202240/bubblesort/GOT_bubble_sort.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        lastname.append(rec[0])
        firstname.append(rec[1])
        age.append(int(rec[2]))

for i in range(0,records):
    print("{0:15}\t{1:15}\t{2:5}".format(lastname[i], firstname[i], age[i]))

answer = "y"

while answer == "y":

    print("\tSearch Options")
    print("1. Search for multiples of 1 name [LASTNAME]")
    print("2. Search for unique name [FIRSTNAME]")
    print("3. EXIT")

    choice = input("Enter which you would like to do [1-3]: ")

    while choice != "1" and choice != "2" and choice != "3":
        print("\t\t**ERORR** INVALID ENTRY!")
        choice = input("Enter which you would like to do [1-3]: ")

    #sequential search-----------------------------------------------------------
    if choice == "1":

        print("\n\t\t~Sequential Search~")

        search = input("Enter the LASTNAME of the person/people you are looking for: ")

        found = []
        f = -1

        for i in range(0,records):

            if search == lastname[i]:

                found.append(i) #stores index of found last names to found list
                f = i

        if f >= 0:

            print("\n\t\tYour Sequential Search results for",search,": ")

            for i in range(0, len(found)): #This will run up to the amount of things on the found list
                print("Index: {3}\t{0:15}\t{1:15}\t{2:5}".format(lastname[found[i]], firstname[found[i]], age[found[i]],found[i]))

        else:
            print("\t\tYour Sequential Search results for",search,"could NOT be found. ")
            print("Please check your SpElLiNG and try again =D")

    if choice == "2":
    #Bubble Sort - Required for Binary search! Must happen first!!!
        for i in range(0, records - 1):#outter loop

            print("OUTER LOOP! i = ", i)


            for index in range(0, records - 1):#inner loop

                print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(firstname[index] > firstname[index + 1]):

                    print("\t\t SWAP! ", firstname[index], "<-->", firstname[index + 1])

                    #if above is true, swap places!

                    temp = firstname[index]

                    firstname[index] = firstname[index + 1]

                    firstname[index + 1] = temp

        
                    #swap all other values

                    temp = age[index]

                    age[index] = age[index + 1]

                    age[index + 1] = temp

                    temp = lastname[index]
                    lastname[index] = lastname[index + 1]
                    lastname[index + 1] = temp


    #Binary Search -----------------------------------------------------------
        print("\n\t\t~Sequential Search~")

        search = input("Enter the FIRSTNAME of the person/people you are looking for: ")

        min = 0                     #this is the lowest starting index
        max = records -1            #this is the highest starting index
        guess = int((min + max) / 2) # or : guess = (min + max) // 2 (the // is used to floor) #This is the middle index

        while min < max and search != firstname[guess]: # this is for ascending order lists 

            if search < firstname[guess]:

                max = guess - 1

            else:

                min = guess + 1

            guess = int((min + max) / 2)

        if search == firstname[guess]:

            print("\n\t\tYour Sequential Search results for",search,": ")

            print("Index: {3}\t{0:15}\t{1:15}\t{2:5}".format(lastname[guess], firstname[guess], age[guess], guess))

        else:
            print("\t\tYour Sequential Search results for",search,"could NOT be found. ")
            print("Please check your SpElLiNG and try again =D")

        


    #EXIT----------------------------------------------------------------------------
    if choice =="3":
        print("\nYou have chosen to EXIT")
    else:
        answer = input("\nWould you like to search again? [y/n]: ").lower()

    #answer = input("\nWould you like to search again? [y/n]: ").lower()

        while answer != "n" and answer != "y":
            print("\t\t**ERROR** Invalid Entry!")
            answer = input("\nWould you like to search again? [y/n]: ").lower()


