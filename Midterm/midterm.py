import csv
import random

#Kanye album sales
#num avg
#rating
#sort list from most sales to least
#sort list from best reviewed to least reviewed

def menu():

    print("1. Print Original Files")
    print("2. Print Gross Album sales")
    print("3. Print Rating for ablums from METACRITIC")
    print("4. Recommend a Random Song")
    print("5. Exit")

    choice = int(input("Please Select One of the following: "))

    while choice < 0 or choice > 5:
        print("*Error!*")
        choice = int(input("Please enter your selection: "))

    return choice

def picker(value):

    for i in range(0,1): 
        song = rec[0]
        value = random.choices(song)
        print("\nToday we recommend you listen to this album: {}\n".format(value))



album = []
rating = []
sales = []
year = []
cost = []
value = 0
num_avg = []

records = 0

with open ("/Users/erickcordon/Desktop/SE126_202240/Midterm/KanyeSales.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        album.append(rec[0])
        year.append(rec[1])
        sales.append(int(rec[2]))
        rating.append(int(rec[3]))
        cost.append(int(rec[4]))

for i in range(0,records):

    avgsls = sales[i]*cost[i]

    num_avg.append(avgsls)


pick = menu()

star = []

while pick != 5: 

    if pick == 1:
        print ("------------------------------Kanye West Album Sales OG DATA--------------------------------\n")

        print("Album                                   Date                     Sales \n")

        for i in range(0,records):
            print("{0:32}\t{1:18}\t{2:8}\t".format(album[i],year[i],sales[i]))

        print("---------------------------------------------------------\n")

    
    if pick == 2:

        print("-------------------------------------------------------------------------------------------------------------")
        print("Album                                   Date                     Sales \t\t\tGross Sales")
        print("-------------------------------------------------------------------------------------------------------------")

        for i in range(0,records):
            print("{0:32}\t{1:18}\t{2:8}\t\t{3:0.2f}".format(album[i],year[i],sales[i],num_avg[i]))
        print("-------------------------------------------------------------------------------------------------------------")



    if pick == 3:

        print("-------------------------------------------------------------------------------------------------------------")
        print("Album                                   Date                     Sales \t\tScore\t\tStar")
        print("-------------------------------------------------------------------------------------------------------------")

        for i in range(0,records):

            star_add = ""

            if rating[i] >= 78:
                star_add = "*"
            
            star.append(star_add)

            print("{0:32}\t{1:18}\t{2:8}\t {3}\t\t{4:5}".format(album[i],year[i],sales[i],rating[i],star[i]))

    if pick == 4:

        song = picker(value)
            

    pick = menu()

print("Thank you for using our software =D")




