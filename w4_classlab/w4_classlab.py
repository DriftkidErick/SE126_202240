#Class lab, Python Pals
#Lab 4 

import csv

ln = []
fn = []
testf = []
tests = []
testt= []

num_avg = []
avg = []

letgr = []


records = 0
classavg = 0

with open("C:/Users/008004507/Desktop/SE126_202240/w4_classlab/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records +=1


        fn.append(rec[0])
        ln.append(rec[1])
        testf.append(int(rec[2]))
        tests.append(int(rec[3]))
        testt.append(int(rec[4]))

    print("--------------------------------Original Data------------------------------------------")

    print("{0} \t{1}\t{2}\t{3}\t{4}".format("Lastname", "Firstname","Test 1", "Test 2", "Test 3"))

    print("----------------------------------------------------------------------------------------")
for i in range(0,records):
    print("{0:13} \t{1:13}\t{2}\t{3}\t{4}".format(ln[i], fn[i], testf[i], tests[i], testt[i]))
print("-------------------------------------------------------------------------------------------\n")


print("\n\n--------------------------------Updated Data with Num Avg--------------------------------------")

print("{0} \t{1}\t{2}\t{3}\t{4}\t{5}".format("Lastname", "Firstname","Test 1", "Test 2", "Test 3",    "Num Average" ))
print("-----------------------------------------------------------------------------------------------")

for i in range(0,records):
    num_avg = (testf[i] + tests[i] + testt[i])/3
    avg.append(num_avg)
    print("{0:13} \t{1:13}\t{2}\t{3}\t{4}\t{5:7.2f}".format(ln[i], fn[i], testf[i], tests[i], testt[i],avg[i]))
print("-------------------------------------------------------------------------------------------\n")


print("\n\n--------------------------------Updated Data With Letter Avg------------------------------------------")

print("{0} \t{1}\t{2}\t{3}\t{4}\t{5}  {6}".format("Lastname", "Firstname","Test 1", "Test 2", "Test 3",    "Num Average", "Let Average"))

print("------------------------------------------------------------------------------------------------------")


for i in range(0,records):

    num_avg = (testf[i] + tests[i] + testt[i])/3
    avg.append(num_avg)


    classavg += num_avg # add one for classave for every num_avg

    if avg[i] >= 90:
        grade = "A"
        letgr.append(grade)

    elif avg[i] >= 80:
        grade = "B"
        letgr.append(grade)
    
    elif avg[i] >= 70:
        grade = "C"
        letgr.append(grade)
    
    elif avg[i] >= 60:
        grade = "D"
        letgr.append(grade)

    elif avg[i] < 60:
        grade = "F"
        letgr.append(grade)


    print("{0:13} \t{1:13}\t{2}\t{3}\t{4}\t{5:7.2f}\t\t{6}".format(ln[i], fn[i], testf[i], tests[i], testt[i], avg[i], letgr[i]))
print("-------------------------------------------------------------------------------------------")

classavg /= records #classavg divided by records

print("\nStudents in class: {}".format(records))
print("The Class Average is: {0} \n".format(classavg))



        

        


