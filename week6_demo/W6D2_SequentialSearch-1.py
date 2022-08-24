#WEEK 6 DAY 2: Sequential Search

#Sequential Search: Sequential search means to search through an entire list (array), starting at the first record and looking through every one until the last, when looking for something. 

 

#For Loops --> allow us to process every record in an list (for index in range(0, records) --> this applies to every record in the list)

#If Statements --> allow us to "search": compare a value in the list we are looking through against the value(s) we are looking for. 

#we are utilizing binary.txt for this demo
#       FIELD0     #FIELD1     FIELD2      FIELD3
#       ID nums    Names       Age         Color  

#VARIABLE DICTIONARY
#




#BASE PROGRAM CODE-----------------------------------------------------------------

import csv

#initialize starting vars (counters) & lists

records = 0

id = []
name = []
age = []
color = []

with open("C:/Users/008004507/Desktop/SE126_202240/week6_demo/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        id.append(rec[0])
        name.append(rec[1])
        age.append(int(rec[2]))
        color.append(rec[3])

#--disconnected from file ------- must utilize lists for rest of program


for i in range(0, records):

    print("{0} \t {1:10} \t {2}yo \t {3}".format(id[i], name[i], age[i], color[i]))




answer = "y"

while answer == "y":


    #SEQUENTIAL SEARCH!

    #first step: ask user for their search item

    search = input("Enter a name you are looking for: ")
    #search is cAsE sEnSiTiVe! 


    #flag system 
    flag = "red"        #red means name is not found, green means name is found
    location = -1       #location is -1 because index values are always positive 
                        #*can also use a decimal value instead of negative

    loop_count = 0

    #second step: run the searching loop; 2 parts --> for loop + if statement INSIDE
    for i in range(0, records):

        #update the loop count
        loop_count += 1
        #searching for a NAME --> look through the name[i]
        if search == name[i]:

            #print("Found the Name!")
            flag = "green"
            location = i        #store the index of the name (location/position 
                                #of  where it is in the list) because all other data for that name is found at the same position in other lists

    print("Search completed after {} search loops".format(loop_count))

    #easier editing of code
    x = location

    #step three: determine if the name has been found or not; print results to user
    if flag == "green": #found the name!

        print("Your search for {} has been found!".format(search))

        #if name has been found, print all data corresponding to the name (original record associated with that name)
        print("{0} \t {1:10} \t {2}yo \t {3}".format(id[x], name[x], age[x], color[x]))

    else: #flag is still red, not been found 

        print("Your search for {} has *NOT* been found!".format(search))
        print("Check your spelling &capitaliation and try again.")


    answer = input("Would you like to search again? [y/n]: ")
    answer = answer.lower()

    while answer != "y" and answer != "n":

        print("**ERROR!**")
        answer = input("Would you like to search again? [y/n]: ")
        answer = answer.lower()




