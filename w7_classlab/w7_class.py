#Week 7 Class Lab ~ Python Pals 

#Prompt: Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this: After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

#Varrible Def: 
from os import system, name 

from time import sleep 

def clear():  

     # for windows  
     if name == 'nt':
          _ = system('cls') 

'''def more():

    answer = input("Would you like to add another seat? [y/n]: ").lower()

    if answer == "n".lower():
        print("have a good day")

    elif answer != "y" and answer != "n":
        answer = input("Would you like to add another seat? [y/n]: ").lower()

    
    return (answer)
'''

#Main Code Below-----------------------------------------------------

seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

print("Row")

for i in range(0,7):
    print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])


answer = "y"

while answer =="y":
    answer = int(input("Please enter the row you would like to sit in [1-7]: "))

    r = (answer -1)    

    s = input("Please enter the seat you would like [A - D]: ").upper()

    
    clear()

    if r >= 0 or r <= 7 :    
        if s == "A":
            seatA[r] = "x"

        elif s == "B":
            seatB[r] = "x"
            
        
        elif s == "C":
            seatC[r] = "x"
            

        elif s == "D":
            seatD[r] = "x"

        print("row")
        for i in range(0,7):
            print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])

    answer = input("Would you like to add another seat?: ")

    clear()

    #for i in range(0,7):
        #if r >= 0 or r <= 7 and s == "A": 
        #if seatA[i] == "x":
            #print("Eror")
           # answer = input("Would you like to add another seat?: ")


print("Have a good day =D")
    


