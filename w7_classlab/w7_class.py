#Week 7 Class Lab ~ Python Pals 

#Prompt: Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this: After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

#Varrible Def:

def selector():
    r = input("\nPlease select which ROW you would like to be seated in [1-7]: ")

    s= input("Please select which Seat you would like to sit in [A-D]: ").upper()

    return (r,s)




    

#Main Code Below-----------------------------------------------------


seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

print("Row")

for i in range(0,7):
    print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])


r = int(input("\nPlease select which ROW you would like to be seated in [1-7]: "))

while r == 1:
    seatA = input("Please select which SEAT you would like to sit in [A-D]: ").upper()
    if seatA[r-1] == "A":
        seatA[r-1].remove("A","X")
        print(seatA,seatB)

    else:
        print("**erorr**")

