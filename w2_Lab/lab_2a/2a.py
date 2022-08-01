#Lab 2A Class Lav

#Prompt: The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event.  Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

import csv

total_records = 0 # counts total records

total_rooms = 0 # total rooms

print("{0:19}\t{1:5}\t{2:4} {3:4}".format("Room", "Max", "Min", "Over"))

with open("C:/Users/008004507/Desktop/SE126_202240/w2_Lab/lab_2a/lab2a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        total_records += 1


        room = rec[0]
        max = int(rec[1])
        min = int(rec[2])
        over = (max - min) *-1
        
        if over >= 0:
        

            total_rooms += 1

            print("{0:18}\t{1:3}\t{2:3} {3:3}".format(room, max, min, over))
    
print("\nTotal records processed are {}".format(total_records))
print("\nTotal rooms over the limit are {}".format(total_rooms))