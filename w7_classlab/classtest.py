#Class lab W7 Python Pals

#prompt: Write a Python program to assign passengers seats in an airplane. 

#variable definitions:
#row is the row in which the user would like to sit in
#s is the seat they would like to sit in



#function definitions below:
from os import system, name

from time import sleep

def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')
   # for mac 
   else:
    _ = system('clear')

def seatPick():
    #asks the user for the row and seat and returns it
    row = int(input("\n\tPlease select a seat Row [1 - 7]: "))

    while row < 1 or row > 7:
        row = int(input("\n\t**INVALID INPUT** \nPlease select a seat Row [1 - 7]: "))

    s = str(input("\tPlease select the seat you would like [A - D]: ")).upper()

    while s != "A" and s != "B" and s != "C" and s != "D":
        s = str(input("\t**INVALID INPUT** \nPlease select the seat you would like [A - D]: ")).upper()

    return [(row - 1), s]

def more():
    #asks the user if they want to enter another seat
    a = input("\nWould you like to enter another seat? [y/n]: ").lower()

    return a

#Main code below----------------------------------------------------------

#available seat list
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

print("Row")

for i in range(0 , 7): #displays original data
    print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

answer = "y"

while answer == "y":

    flag = "False"

    seat = seatPick()

    clear()

    if seatA[seat[0]] == "x":
            if seat[1] == "A":
                flag = "True"
    
    if seatB[seat[0]] == "x":
            if seat[1] == "B":
                flag = "True"
    
    if seatC[seat[0]] == "x":
            if seat[1] == "C":
                flag = "True"
    
    if seatD[seat[0]] == "x":
            if seat[1] == "D":
                flag = "True"

    for i in range(0,7):

        if flag == "False": 

            if seatA[seat[0]] != "x":
                if seat[1] == "A":
                    seatA[seat[0]] = "x"
            
            if seatB[seat[0]] != "x":
                if seat[1] == "B":
                    seatB[seat[0]] = "x"
            
            if seatC[seat[0]] != "x":
                if seat[1] == "C":
                    seatC[seat[0]] = "x"

            if seatD[seat[0]] != "x":
                if seat[1] == "D":
                    seatD[seat[0]] = "x"

            #prints updated file
            print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

    if flag == "True": # if the seat it take in the file print seat is not available
        print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))
        print("\nThis seat is already taken. Please choose another.")

    answer = more()

    while answer != "y" and answer != "n": #checks for user error
        answer = input("\nWould you like to enter another seat? [y/n]: ").lower()



print("Thank you for using ")

