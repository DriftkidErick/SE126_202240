#lab 2b Erick Cordon

#Prompt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output. The last line should print the number of computers in the file.

#main code below----

import csv

record = 0
print("\nDATA FROM FILE------------------------")

print("{0:8} {1:8} {2}   {3:3}  {4:6}     {5:9} {6:6} {7:2} {8:4}".format("Type", "BRAND", "CPU", "RAM", "DISC 1", "NUM DISCS", "DISC 2", "OS", "YEAR"))
print("----------------------------------------------------------------------")

with open("w2_Lab/lab_2B/lab2b.csv") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file: #one record at a time
        #entire code block applies to ONE record ... at a time
        record +=1

        type_ = rec[0]
        manu = rec[1]
        cpu = rec[2]
        ram = rec[3]
        first_disk = rec[4]
        num_disk = rec[5]

        #fields below change per record
        second_disc = ""
        os = ""
        year = ""

        if type_ == "D":
            type_ = "Desktop"
        
        elif type_ == "L":
            type_ = "Laptop"

        else: 
            #error check
            point = record - 1
            type_ = "ERROR @ record" + str(point)

        if manu == "DL":
            manu = "Dell"

        elif manu == "HP":
            manu = "Hewlett Packard"

        elif manu == "GW":
            manu = "Gateway"

        if num_disk == "1":
            #means no second disc
            os = rec[6]
            year= rec[7]
            second_disc = "---"
        
        elif num_disk == "2":
            second_disc = rec[4]
            
            


        


        print("{0:8} {1:8} {2}   {3:3}  {4:6}     {5:9} {6:6} {7:2} {8:4}".format(type_, manu, cpu, ram, first_disk, num_disk, second_disc, os, year))
print("----------------------------------------------------")

print("\n\nRecords: {0}".format(record))