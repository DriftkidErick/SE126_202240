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

#Main Code Below--------------------------

seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

print("Row")

for i in range(0,7):
    print("{}  {} {}\t{} {}".format(i + 1, seatA[i],seatB[i],seatC[i],seatD[i]))

answer = "y"

while answer =="y":
    answer = int(input("Please enter the row you would like to sit in [1-7]: "))

    r = (answer -1)    

    s = input("Please enter the seat you would like [A - D]: ").upper()

    if r >= 0 or r <= 7 :    
        if s == "A":
            seatA[r] = "x"
            

        elif s == "B":
            seatB[r] = "x"
            
        
        elif s == "C":
            seatC[r] = "x"
            

        elif s == "D":
            seatD[r] = "x"

        for i in range(0,7):
            print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])

    more() #The function that asks the user if they want to add another seat


print("out of loop")