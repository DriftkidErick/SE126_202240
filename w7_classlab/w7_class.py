#Week 7 Class Lab ~ Python Pals 

#Prompt: Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this: After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

#Varrible Def:

#Main Code Below-----------------------------------------------------

# https://stackoverflow.com/questions/24106733/replace-an-item-in-a-list-based-on-user-input (Check this out)
# https://stackoverflow.com/questions/49633640/how-to-replace-string-character-pattern-using-python-in-csv-file#:~:text=After%20opening%20the%20file%20with,the%20string%20characters%20you%20desire.

import csv

row_a = []
row_b = []
row_c = []
row_d = []

records = 0
search_count = 0 

with open("C:/Users/Erick/Desktop/SE126_202240/w7_classlab/Seat.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        row_a.append(rec[0])
        row_b.append(rec[1])
        row_c.append(rec[2])
        row_d.append(rec[3])

print("Row")

for i in range(0,records):

    print("{0} \t{1} {2} \t{3} {4}".format(i + 1, row_a[i], row_b[i], row_c[i], row_d[i]))

print("Close") #Delete this used just for closing

answer = "y"

while answer == "y": #trying to build a search/input

    choice = input=("Please select the row you would like: ")
    search = input=("Please Enter the seat you would like: ")

    for i in range(0,records):
        