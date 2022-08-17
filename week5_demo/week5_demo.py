import csv

def menu():

    print("1. Show Numeric Avg")
    print("2. Show Letter Avg")
    print("3. Print Original File")
    print("4.       EXIT      ")

    choice = int(input("Please enter your selection: "))

    while choice < 0 or choice > 4:
        print("*Error!*")
        choice = int(input("Please enter your selection: "))

    return choice


firstname = []
lastname = []
test1 = []
test2 = []
test3 = []
teacher = []

records = 0

with open ("C:/Users/008004507/Desktop/SE126_202240/week5_demo/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        firstname.append(rec[0])
        lastname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
        teacher.append("KT")
'''
for i in range(0,records):
    print("{0:15}\t{1:15}\t{2:3}t\{3:3}\t{4:3}\t{5:3}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], teacher[i]))
'''
num_avg = []

for i in range(0,records):

    grade_sum = test1[i] + test2[i] + test3[i]
    grade_avg = grade_sum / 3
    num_avg.append(grade_avg)

letter_avg = []

for i  in range (0,records):

    if num_avg[i] >= 90:
        letter = "A"

    else:
        letter = "Not an A"

    letter_avg.append(letter)

menu_choice = menu()

while menu_choice != 4:

    if menu_choice == 1:
        print("\n\tNumeric AVG")

        for i in range(0,records):
            
            print("{0:15}\t{1:15}\t{2:3}".format(firstname[i], lastname[i], num_avg[i]))

    if menu_choice == 2:
        print("\n\tLetter AVG")
        for i in range(0,records):
            print("{0:15}\t{1:15}\t{2:3}".format(firstname[i], lastname[i], letter_avg[i]))

    if menu_choice == 3:
        print("Original Data File")
        for i in range(0,records):
            print("{0:15}\t{1:15}\t{2:3}t\{3:3}\t{4:3}\t{5:3}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], teacher[i]))

    menu_choice = menu()

print("\nThank you")