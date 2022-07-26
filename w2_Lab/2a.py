#Lab 2A

#Prompt: The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event.  Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

import csv

total_records = 0 # counts total records

total_rooms = 0 # total rooms

print("{0:10}\t{1:4}\t{2:4}\t{3:4}".format("Room", "Max", "Min", "Over"))

with open("w2_Lab\lab2a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        total_records += 1

    #print(rec)

    room = rec[0]
    max = int(rec[1])
    min = int(rec[2])
    over = min - max

    

    #total_rooms += over

    print("{0:10}\t{1:4}\t{2:4}\t{3:4}".format(room, max, min, over))
print(total_records)
print(total_rooms)