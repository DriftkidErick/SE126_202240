import csv

#create empty lists
lastname = []
firstname = []
test1 = []
test2 = []
test3 = []

records = 0

#hand populated lists
#teacher = ["KT"]
#for i in range(0,len(teacher)):
    #print(teacher[i])

with open("C:/Users/008004507/Desktop/SE126_202240/week4_demo/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        print("Row#: {}, {}".format(records + 1, rec)) #can be used to see what row/line has an error
        records += 1

        lastname.append(rec[1])
        firstname.append(rec[0])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

print("Records in file: {}".format(records))

print("--------------------------------------------------------------------")
print("{:10}\t{:10}\t{}\t{}\t{}".format("FIRST", "LASTNAME", "T1", "T2", "T3"))
print("--------------------------------------------------------------------")

for i in range(0,records):

    print("{:10}\t{:10}\t{}\t{}\t{}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i]))

className = []
stars = []
for i in range(0,records):

    className.append("C++")

    star_add = ""

    if test1[i] >= 85:
        star_add += "*"

    if test2[i] >= 85:
        star_add += "*"
    
    if test3[i] >= 85:
        star_add += "*"

    stars.append(star_add)

print("--------------------------------------------------------------------")
print("{:10}\t{:10}\t{}\t{}\t{}".format("FIRST", "LASTNAME", "T1", "T2", "T3"))
print("--------------------------------------------------------------------")

for i in range(0,records):

    print("Class:{} \t{:10}\t{:10}\t{}\t{}\t{}\t{}".format(className[i], firstname[i], lastname[i], test1[i], test2[i], test3[i], stars[i]))

