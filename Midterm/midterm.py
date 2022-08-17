import csv 

#Kanye album sales
#num avg
#rating
#sort list from most sales to least
#sort list from best reviewed to least reviewed

def menu():

    print("1. Print Original Files")
    print("2. Print average number of sales")
    print("3. Print Rating for ablums based on sales")
    print("4. Sort from most sales to least sales")
    print("5. Exit")

    choice = int(input("Please Select One of the following: "))

    while choice < 0 or choice > 4:
        print("*Error!*")
        choice = int(input("Please enter your selection: "))

    return choice

album = []
genre = []
rating = []
sales = []
year = []
num_avg = []

records = 0

with open ("Create a csv file") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        album.append(rec[])
        year.append(rec[])
        sales.append(int(rec[]))
        rating.append(int(rec[]))

