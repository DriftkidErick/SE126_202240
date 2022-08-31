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


row = int(input("Please enter the row you would like to sit in [1-7]: "))

r = (row -1)

while r  >=0 or r <= 7 :

    s = input("Please enter the seat you would like [A - D]: ").upper()
    if r == 0:    
        if s == "A":
            seatA[0] = "x"
            print(seatA)

        elif s == "B":
            seatB[0] = "x"
            print(seatA)
        
        elif s == "C":
            seatC[0] = "x"
            print(seatA)

        elif s == "D":
            seatD[0] = "x"

        for i in range(0,7):
            print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])
        
    if r == 1:    
        if s == "A":
            seatA[1] = "x"
            print(seatA)

        elif s == "B":
            seatB[1] = "x"
            print(seatA)
        
        elif s == "C":
            seatC[1] = "x"
            print(seatA)

        elif s == "D":
            seatD[1] = "x"

        for i in range(0,7):
            print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])
    
    if r == 2:    
        if s == "A":
            seatA[2] = "x"
            print(seatA)

        elif s == "B":
            seatB[2] = "x"
            print(seatA)
        
        elif s == "C":
            seatC[2] = "x"
            print(seatA)

        elif s == "D":
            seatD[2] = "x"

        for i in range(0,7):
            print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])

    if r == 3:    
        if s == "A":
            seatA[3] = "x"
            print(seatA)

        elif s == "B":
            seatB[3] = "x"
            print(seatA)
        
        elif s == "C":
            seatC[3] = "x"
            print(seatA)

        elif s == "D":
            seatD[3] = "x"

        for i in range(0,7):
            print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])

    if r == 4:    
        if s == "A":
            seatA[4] = "x"
            print(seatA)

        elif s == "B":
            seatB[4] = "x"
            print(seatA)
        
        elif s == "C":
            seatC[4] = "x"
            print(seatA)

        elif s == "D":
            seatD[4] = "x"

        for i in range(0,7):
            print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])

    if r == 5:    
        if s == "A":
            seatA[5] = "x"
            print(seatA)

        elif s == "B":
            seatB[5] = "x"
            print(seatA)
        
        elif s == "C":
            seatC[5] = "x"
            print(seatA)

        elif s == "D":
            seatD[5] = "x"

        for i in range(0,7):
            print(i + 1, seatA[i],seatB[i],seatC[i],seatD[i])
    


