#Week 7 Class Lab ~ Python Pals 

#Prompt: Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this: After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

#Varrible Def: 
from os import system, name 

from time import sleep 

def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')
   # for mac 
   else:
    _ = system('clear')

def more():

    answer = input("Would you like to add another seat? [y/n]: ").lower()

    if answer == "n".lower():
        print("have a good day")

    elif answer != "y" and answer != "n":
        answer = input("Would you like to add another seat? [y/n]: ").lower()

    
    return (answer)

def rowPick():

    r = int(input("\n\tPlease enter the row of the seat you want to pick: "))

    while r < 1 and r > 7:
        r = int(input("\n\t**INVALID INPUT** \nPlease enter the row of the seat you want to pick: "))
    
    return ([r - 1])

def seatPick():
    s = input("\tPlease enter the seat letter you would like to pick: ").upper()

    while s != 'A' and s != 'B' and s != 'C' and s != 'D':
        s = input("\t**INVALID INPUT** \nPlease enter the seat letter you would like to pick: ").upper()

    return (s)

#Main Code Below-----------------------------------------------------

seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

print("Row")

for i in range(0,7):
    print("{}  {} {}\t{} {}".format(i + 1, seatA[i],seatB[i],seatC[i],seatD[i]))

answer = "y"

while answer =="y":
    
    row = rowPick()

    seat = seatPick()

    flag = "taken"

    while row[0] > 0 and row[0] < 7:  

        if seat[1] == "A":

            seatA[row[0],seat[1]] = "x"
            
            if seatA[i] == "x":
                flag = "taken" 

    for i in range(0,7):
        print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])

    answer = more() #The function that asks the user if they want to add another seat


print("out of loop")
print("Have a good day =D")
    


