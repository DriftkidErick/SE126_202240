def seatPick():
    #asks the user for the row and seat and returns it
    r = int(input("\n\tPlease select a seat Row [1 - 7]: "))
    while r < 1 or r > 7:
        r = int(input("\n\t**INVALID INPUT** \nPlease select a seat Row [1 - 7]: "))

    s = str(input("\tPlease select the seat you would like [A - D]: ")).upper()
    while s != "A" and s != "B" and s != "C" and s != "D":
        s = str(input("\t**INVALID INPUT** \nPlease select the seat you would like [A - D]: ")).upper()

    return [(r - 1), s]


def repeat():
    #asks the user if they want to enter another seat
    a = input("\nWould you like to enter another seat? [y/n]: ").lower()

    if a != "y" and a != "n":
        print("\n\t\t**INVALID INPUT** PLEASE TRY AGAIN.")
        a = input("\nWould you like to enter another seat that you would like? [y/n]: ").lower()

    return a

#---------------MAIN CODE---------------
import os

#lists
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

print("ROW")
for i in range(0, (len(seatA))):
    #displays original seating chart
    print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

answer = "y"
while answer == "y":
    seatTaken = "False"
    seat = seatPick()
    os.system('cls')

    if seatA[seat[0]] == 'X':
            if seat[1] == 'A':
                seatTaken = "True"
    if seatB[seat[0]] == 'X':
            if seat[1] == 'B':
                seatTaken = "True"
    if seatC[seat[0]] == 'X':
            if seat[1] == 'C':
                seatTaken = "True"
    if seatD[seat[0]] == 'X':
            if seat[1] == 'D':
                seatTaken = "True"

    for i in range(0, (len(seatA))):

        if seatTaken == "False":
            #checks the input from user against this if/else tree
            if seatA[seat[0]] != 'X':
                if seat[1] == 'A':
                    seatA[seat[0]] = 'X'
            if seatB[seat[0]] != 'X':
                if seat[1] == 'B':
                    seatB[seat[0]] = 'X'
            if seatC[seat[0]] != 'X':
                if seat[1] == 'C':
                    seatC[seat[0]] = 'X'
            if seatD[seat[0]] != 'X':
                if seat[1] == 'D':
                    seatD[seat[0]] = 'X'

            #prints updated seating chart
            print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

    if seatTaken == "True":
        print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))
        print("\nThis seat is already taken. Please choose another.")

    answer = repeat()

print("\n\n\t\t\tGoodbyeeeeee!")