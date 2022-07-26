#Lab 2A

#Prompt: The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event.  Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

import csv

total_records = 0 # counts total records

total_rooms = 0 # total rooms

print("{0}\t{1}\t{2}\t{3}".format("Room", "Max", "Min", "Over"))

with open("w2_Lab\lab2a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        total_records += 1

    print(rec)

    max = 0
    min = 0
    over = 0

    if over > min:
        print()

    total_rooms += over