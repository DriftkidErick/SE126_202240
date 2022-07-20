#Week 1 Day 2 -se116 Review Demo

print("\n\n\tWelcome to the Room Safety Manager!\n\n")

answer = input("\tWould you like to check some rooms? [y/n]: ").lower()

while answer != "y" and answer != "n":

    print("\t\t**ERROR! INVALID ENTRY!**")   
    answer = input("\tWould you like to check some rooms? [y/n]: ").lower()


while answer == "y":

    roomCapacity = int(input("\tEnter the room's Max Capacity "))

    peopleAttending = int(input("\tEntert the number of meeting attendees for the room: "))

    difference = roomCapacity - peopleAttending

    if difference >= 0: #the meeting can occur (difference is positive, meaning there is room leftover)
        print("\t\tSafely under room capacity!")
        print("You may add up to {0} people to the meeting.".format(difference))

    else:
        print("\t\tOH NO! You are over room capacity!")
        print("Please remove {0} people to the meeting for safety regulations.".format(difference * -1))

    answer = input("\tWould you like to check some rooms? [y/n]: ").lower()
    while answer != "y" and answer != "n":

        print("\t\t**ERROR! INVALID ENTRY!**")   
        answer = input("\tWould you like to check some rooms? [y/n]: ").lower()

print("\n\nThank you for using my program. Goodbye! :]\n\n")