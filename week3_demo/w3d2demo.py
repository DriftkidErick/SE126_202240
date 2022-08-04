import csv 


records = 0

device = []#we have created an empty list
brand = []
cpu = []
ram = []
first_disk = []
num_hdd = []
second_disk = []
os = []
yr = []



with open("/Users/erickcordon/Desktop/SE126_202240/SE126_202240/W3_ClassLab/lab3a.csv") as csvfile:

    #access the file's data
    file = csv.reader(csvfile)

    #process the file's data
    for rec in file:

        records += 1

        #add data from file to lists - .append()

        #remeber to tab this in 
        device.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_hdd.append(rec[5])

        if rec[5] == "1":
            second_disk.append("-none-")
            os.append(rec[6])
            yr.append(rec[7])

        else:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])




    #closed file-----------------------------------------

#process the list to print data to the screen 
print("\n\tORIGINAL FILE DATA-----------------------------------------------")

for index in range(0,records):

    print("INDEX#{9}:\t{0:8}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], num_hdd[index], second_disk[index], os[index], yr[index], index))

print("\t-------------------------------------------------------------------")
print("\n\n\tTotal Records: ", records)

#process to print desktop/laptop + brand name
print("\n\tUpdated File Data-------------------------")

for index in range(0,records):

    if device[index] == "D":
        #change to desktop
        device[index] = "Desktop"
    
    elif device[index] == "L":
        #change to laptop
        device[index] = "Laptop"

    #change brands
    
    print("INDEX#{9}:\t{0:8}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], num_hdd[index], second_disk[index], os[index], yr[index], index))

print("\t-------------------------------------------------")

#prepare counting variables
ram8 = 0
ram16 = 0
#processs the list to determine the number of 8 rams and 16 rams

for i in range(0,records):

    if ram[i] == "08":
        ram8 += 1
    
    elif ram[i] == "16":
        ram16 += 1

    else:
        print("*ERROR encounterd at index{}".fomat(i))

print("\n\tTHERE ARE {0} 8GB RAM DEVICES / {1} 16GB RAM DEVICES".format(ram8,ram16))
