import csv

fname = []
lname = []
dob = []

with open ("C:/Users/008004507/Desktop/SE126_202240/w6_classlab/lab5_updated.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        fname.append(rec[0])
        lname.append(rec[1])
        dob.append(rec[2])

month = []
day = []
year = []

todays_month = 9
today_day = 12
today_year = 2022

for i in range(0, len(dob)):
    
    dob_list = dob[i].split("/")

    month.append(int(dob_list[0]))
    day.append(int(dob_list[1]))
    year.append(int(dob_list[2]))

for i in range(0, len(dob)):

    print("{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:5}\t{5:5}".format(lname[i],fname[i],dob[i],month[i],day[i],year[i]))

for i in range(0, len(dob)):

    if month[i] < todays_month:
    #birthday has occured

        age = today_year - year[i] + 1

        if day[i] < today_day:
            age = age

        else:
            age - 1

