import csv
import random

#Kanye album sales
#num avg
#rating
#sort list from most sales to least
#sort list from best reviewed to least reviewed

def menu():

    print("1. Print Original Files")
    print("2. Print Gross Album sales")
    print("3. Print Rating for ablums from METACRITIC")
    print("4. Recommend a Random Song")
    print("5. Exit")

    choice = int(input("Please Select One of the following: "))

    while choice < 0 or choice > 5:
        print("*Error!*")
        choice = int(input("Please enter your selection: "))

    return choice

def mood():

    print("1. The College Dropout ")
    print("2. Late Registration")
    print("3. Graduation")
    print("4. 808s & Heartbreak")
    print("5. My Beautiful Dark Twisted Fantasy")
    print("6. Yeezus")
    print("7. The Life Of Pablo")
    print("8. Ye")
    print("9. Jesus Is King")
    print("10. Donda")
    
    choice2 = int(input("Please Select One of the following: "))

    while choice2 < 0 or choice2 > 10:
        print("*Error!*")
        choice2 = int(input("Please enter your selection: "))

    return choice2



album = []
rating = []
sales = []
year = []
cost = []
num_avg = []

records = 0

with open ("C:/Users/Erick/Desktop/SE126_202240/Midterm/KanyeSales.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        album.append(rec[0])
        year.append(rec[1])
        sales.append(int(rec[2]))
        rating.append(int(rec[3]))
        cost.append(int(rec[4]))

for i in range(0,records):

    avgsls = sales[i]*cost[i]

    num_avg.append(avgsls)


pick = menu()

star = []

while pick != 5: 

    if pick == 1:
        print ("------------------------------Kanye West Album Sales OG DATA--------------------------------\n")

        print("Album                                   Date                     Sales \n")

        for i in range(0,records):
            print("{0:32}\t{1:18}\t{2:8}\t".format(album[i],year[i],sales[i]))

        print ("---------------------------------------------------------------------------------------------")

    
    if pick == 2:

        print("-------------------------------------------------------------------------------------------------------------")
        print("Album                                   Date                     Sales \t\tGross Sales")
        print("-------------------------------------------------------------------------------------------------------------")

        for i in range(0,records):
            print("{0:32}\t{1:18}\t{2:8}\t{3:0.2f}".format(album[i],year[i],sales[i],num_avg[i]))
        print("-------------------------------------------------------------------------------------------------------------")



    if pick == 3:

        print("-------------------------------------------------------------------------------------------------------------")
        print("Album                                   Date                     Sales \t\tScore   Star")
        print("-------------------------------------------------------------------------------------------------------------")

        for i in range(0,records):

            star_add = ""

            if rating[i] >= 78:
                star_add = "*"
            
            star.append(star_add)

            print("{0:32}\t{1:18}\t{2:8}\t {3}\t{4:5}".format(album[i],year[i],sales[i],rating[i],star[i]))

    if pick == 4:

        gen = mood()

        while gen != 11:

            if gen == 1:

                tcd = ["Intro","We Dont Care", "Graduation Day","All Falls Down","I'll Fly Away","Spaceship","Jesus Walks","Never Let Me Down","Get Em High","Workout Plan","The New Workout Plan","Slow Jamz","Breathe In Breathe Out","School Spirit Skit","School Spirit Skit 2","Lil Jimmy SKit","Two Words","Through The Wire","Family Business"]

                song = random.choice(tcd)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break
                
            if gen == 2:

                lr = ["Wake Up Mr.West","Heard 'Em Say","Touch The Sky","Gold Digger","Drive Slow","My Way Homme","Crack Music","Roses","Bring Me Down","Addiction","Diamonds From Sierra Leone","We Major","Hey Mama","Celebration","Gone","Diamonds from Sierra Leone [remix]","Late"]

                song = random.choice(lr)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 3:

                g = ["Good Morning","Champion","Stronger","I Wonder","Good Life","Can't Tell Me Nothing","Barry Bonds","Drunk and Hot","Flashing Lights","Everything","The GLory","Homecoming","Big Brother"]

                song = random.choice(g)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 4:

                hrtbrk = ["Say You Will","Welcome To Heartbreak","Heartless","Amazing","Love Lockdown","Paranoid","RoboCop","Street Lights","Bad News","See You In My Nightmares","Coldest Winter","Pinocchio Story"]

                song = random.choice(hrtbrk)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 5:

                mbdtf = ["Dark Fantasy","Gorgeous","Power","All Of The Lights (Interlude)","All of the Lights","Monster","So Appalled","Devil In A New Dress","Runaway","Hell Of A Life","Blame Game","Lost In The World","Who Will Survive In America"]

                song = random.choice(mbdtf)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 6:

                zus = ["On Sight","Skinhead","I am A God","New","Hold My Liquor","I'm In it","Blood On The Leaves","Guilt Trip","Send It Up","Bound 2"]

                song = random.choice(zus)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 7:

                tlp = ["Ultralight Beam","Father Stretch My Hands","Pt.2","Famous","Feedback","Low Lights","Highlights","Freestyle 4","I Love Kanye","Waves","FML","Real Friends","Wolves","Franks track","30 Hours","No More Parties In LA","Facts","Fade","Saint Pablo"]

                song = random.choice(tlp)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 8:

                ye = ["I Thought About you","Yikes","All Mines","Wouldn't Leave","No Mistakes","Ghost Town","Violent Crimes"]

                song = random.choice(ye)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 9:

                jik = ["Every Hour","Selah","Follow God","Closed On Sunday","On God","Everything We Need","Water","God Is","Hands On","Use This Gospel","Jesus is Lord"]

                song = random.choice(jik)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 10:

                don = ["Donda Chant","Hurricane","Moon","Life Of The Party","Off The Grid","Jail","Praise God","Come To Life","Believe What I Say","No Child Left Behind","Up From The Ashes","Remote Control Pt.2","God Breathed","Lord I Need You","24","Junya","Never Abandon Your Family","Donda","Keep My Spirit Alive","Jesus Is Lord Pt.2","Heaven And Hell","Remote Control","Tell The Vision","Jonah","Pure Souls","Ok Ok","New Again","Junya Pt. 2","Jail Pt.2","Keepy My Spirit Alive Pt.2"]

                song = random.choice(don)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break









            










    pick = menu()

print("Thank you for using our software =D")




