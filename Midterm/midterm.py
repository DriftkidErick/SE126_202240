import csv 

#Kanye album sales
#num avg
#rating
#sort list from most sales to least
#sort list from best reviewed to least reviewed

def menu():

    print("1. Print Original Files")
    print("2. Print Gross Album sales")
    print("3. Print Rating for ablums from METACRITIC")
    print("4. Sort from most sales to least sales")
    print("5. Exit")

    choice = int(input("Please Select One of the following: "))

    while choice < 0 or choice > 5:
        print("*Error!*")
        choice = int(input("Please enter your selection: "))

    return choice

album = []
rating = []
sales = []
year = []
cost = []
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

for i in range(0,records):

    avgsls = sales[i]/cost[i]

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
        for i in range(0,records):
            print("{0:32}\t{1:18}\t{2:8}\t\t{3:0.2f}".format(album[i],year[i],sales[i],num_avg[i]))

        print("The number of average total ablum sales is {}".format(avgsls))

    if pick == 3:
        for i in range(0,records):

            star_add = ""

            if rating[i] > 79:
                star_add = "*****"

            elif rating[i] > 75:
                star_add = "****"
            
            if rating[i] > 70:
                star_add = "***"
            
            if rating[i] < 70:
                star_add = "**"

            if rating[i] <= 60:
                star_add = "*"

            star.append(star_add)

            print("{0:32}\t{1:18}\t{2:8}\t{3}\t{4:5}".format(album[i],year[i],sales[i],rating[i],star[i]))

    pick = menu()

print("Thank you for using our software =D")




