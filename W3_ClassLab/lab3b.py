#Lab 3 Individual Erick Cordon

#prompt: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#varribles------------------------------------
#device = [] Laptop or  Desktop
#brand = [] Brand  of machine
#cpu = [] kind of cpu
#ram = []  how much ram
#first_disk = [] 
#num_hdd = []
#second_disk = []
#os = [] operating system
#yr = [] year device was made

#repD = 0  #total desktops getting replaced
#repL = 0  #total laptops getting replaced

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

with open("C:/Users/008004507/Desktop/SE126_202240/W3_ClassLab/lab3a.csv") as csvfile:

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

        #Hard drive data
        if rec[5] == "1":
            second_disk.append("--")
            os.append(rec[6])
            yr.append(rec[7])
            
        
        else:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
            



print("------------------------------------Data File----------------------------------------")

for index in range (0,records):

    #Define machine
    if device[index] == "D":
            device[index] = "Desktop"
        
    elif device[index] == "L":
        device[index] = "Laptop"
    
    #Brand indetifier
    if brand[index] == "DL":
        brand[index] = "Dell"

    elif brand[index] == "HP":
        brand[index] = "HP"

    elif brand[index] == "GW":
        brand[index] = "GateWay"


    print("#{9}:\t{0:8}\t{1}\t {2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], num_hdd[index], second_disk[index], os[index], yr[index], index))

print("-------------------------------------------------------------------------------------")

repD = 0 
repL = 0

for i in range(0,records):

    #if yr[i] == "16" or yr[i] == "15": #test this 
    if yr[i] <="16": #final form
        if device[i] == "Desktop":
            repD += 1
        elif device[i] == "Laptop":
            repL += 1


print("\nThere are {0} desktops needed to be replaced. Total cost will be ${1}".format(repD, repD * 2000)) # cost per desktop is 2k

print("\nThere are {0} laptops needed to be replaced. Total cost will be ${1}".format(repL, repL * 1500)) #cost per laptop is 1.5k






            
