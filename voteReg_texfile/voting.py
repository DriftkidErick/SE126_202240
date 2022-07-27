import csv

records = 0

too_young = 0 # age < 18
not_reg = 0 #age >=18, reg != "Y"
no_vote = 0 #age >= 18, reg == "Y", voted != "Y"
yes_vote = 0 #age >= 18, reg == "Y", voted == "Y"

print("{0:10}| \t {1:10}| \t {2}| \t {3}".format("ID #", "AGE", "REG", "Voted"))
with open("C:/Users/008004507/Desktop/SE126_202240/voteReg_texfile/voting.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        #print(rec)

        id = rec[0]
        age = int(rec[1]) #int before rec turns rec str to int
        reg = rec[2]
        voted = rec[3]

        if age < 18:

            too_young += 1
        
        elif reg == "N":
            not_reg +=1

        elif voted != "Y":

            no_vote +=1

        else: 

            yes_vote +=1
    
        print("{0:10}| \t {1:10}| \t {2} \t {3}".format(id, age, reg, voted))



print("-------------------------\n\n")

print("     Too young: ", too_young)
print("Not Registered: ", not_reg)
print("  Did not vote: ", no_vote)
print("         Voted: ", yes_vote)
print(" Total Records:", records)
