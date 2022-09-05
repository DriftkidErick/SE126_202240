from os import system, name
from time import sleep

def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')
   # for mac 
   else:
    _ = system('clear')

#Functions:
def rowPick():
    #asks the user for the row and seat and returns it
    r = int(input("\n\tPlease enter the row of the seat you want to pick: "))

    while r < 1 and r > 7:
        r = int(input("\n\t**INVALID INPUT** \nPlease enter the row of the seat you want to pick: "))


    return [(r - 1)]

def seatPick():

    s = input("\tPlease enter the seat letter you would like to pick: ").upper()

    while s != 'A' and s != 'B' and s != 'C' and s != 'D':
        s = input("\t**INVALID INPUT** \nPlease enter the seat letter you would like to pick: ").upper()
    
    return [s]

def repeat():
    #asks the user if they want to enter another seat
    a = input("\nWould you like to enter another seat? [y/n]: ")

    if a != "y" and a != "n":
        print("\n\t\t**INVALID INPUT** PLEASE TRY AGAIN.")
        a = input("\nWould you like to enter another seat that you would like? [y/n]: ")
    
    return a

#MAIN CODE------------------------------------------------------------------------------------------------------------------------

answer = "y"

#lists
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

print("ROW")
for i in range(0, (len(seatA))):
    #displays original seating chart
    print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

while answer == "y":

    seatTaken = "False"
    row = rowPick()
    seat = seatPick()

    if seatA[row[0]] == 'X':
            if row[1] == 1:
                if seat[1] == 'A':
                    seatTaken = "True"

    for i in range(0, (len(seatA))):
            
        if seatTaken == "False":
            #checks the input from user against this if/else tree
            if seatA[row[0]] != 'X':
                if row[0] == 1:

                 if seat[1] == 'A':
                        seatA[seat[0]] = 'X'

        

            #prints updated seating chart
            print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))
        
    if seatTaken == "True":
        print("\nThis seat is already taken. Please choose another.")
    
    
    
    answer = repeat()

print("Thank you for using our program =D")