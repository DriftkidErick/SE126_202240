#MAKE SURE TO ADD CORRESPODING MOTTOS TO HOUSE

import csv


#blank tags

firstname = []
lastname = []
age = []
nickname = []
house = []

records = 0
with open ("C:/Users/008004507/Desktop/SE126_202240/w4_classlab/lab4A_GOT_NEW.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        firstname.append(rec[0])
        lastname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        house.append(rec[4])

print("--------------------------------Original Data------------------------------------------")

print("{0} \t{1}\t{2}\t{3}\t\t{4}".format("First Name", "Last Name","Age", "Nick Name", "House"))

print("----------------------------------------------------------------------------------------")

for i in range(0,records):
    print("{0:13} \t{1:13}\t{2}\t{3:18}\t{4}".format(firstname[i], lastname[i], age[i], nickname[i], house[i]))


print("\n\n--------------------------------Updated Data---------------------------------------------------------------------")

print("{0} \t{1}\t{2}\t{3}\t\t{4}\t\t\t{5}".format("First Name", "Last Name","Age", "Nick Name", "House", "Motto"))

print("-----------------------------------------------------------------------------------------------------------------")

line = []
stark = 0
bara = 0
tully = 0
watch = 0
lanni = 0
targa = 0

ageave = 0

for i in range(0,records):
    
    houseline = ""

    if house[i] == "House Stark":
        houseline += "Winter is Coming"
        stark += 1
    
    if house[i] == "House Baratheon":
        houseline += "Ours is the Fury"
        bara += 1

    if house[i] == "House Tully":
        houseline += "Family. Duty. Honor"
        tully += 1

    if house[i] == "Night's Watch":
        houseline += "And now my watch begins."
        watch += 1

    if house[i] == "House Lannister": 
        houseline += "Hear me roar!"
        lanni += 1

    if house[i] == "House Targaryen":
        houseline += "Fire & Blood"
        targa += 1
    
    line.append(houseline)
    ageave += age[i]

for i in range(0,records):
    print("{0:13} \t{1:13}\t{2}\t{3:18}\t{4:16}\t{5}".format(firstname[i], lastname[i], age[i], nickname[i], house[i], line[i]))


ageave /=records 

print("\n\nThe total number of people: {}".format(records))
print("\nThe average age is: {:.0f}".format(ageave))

print("\nTotal people per house:") 
print("\tHouse Stark:     {}".format(stark))
print("\tHouse Baratheon: {}".format(bara))	
print("\tHouse Tully:     {}".format(tully))	
print("\tNight's Watch:   {}".format(watch)) 
print("\tHouse Lannister: {}".format(lanni))
print("\tHouse Targaryen: {}".format(targa))
