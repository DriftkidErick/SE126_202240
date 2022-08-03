#Lab 3 Individual Erick Cordon

#prompt: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#----------Main Code Below-----------------

import csv

records = 0

device = []
brand = []
cpu = []
ram = []
first_disk = []
num_hdd = []
second_disk = []
os = []
yr = []

with open() as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        #add data from file to lists - .append()
        device.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_hdd.append(rec[5])

        if rec[5] == "1":
            second_disk.append("--")
            
