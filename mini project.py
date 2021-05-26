import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\n Chooose A, B or C to continue")
required1 = ("\nChoose A or B to continue")
required2 = ("\nChoose B or C to continue")
end2 = ("\nThe story ends here. Thank you for playing ^-^ ")
end = ("\nX--------------------You survive this day and proceed towards the next!!!--------------------X\n")
i = 65
f = 25

#Day 1(discover)
def intro():
    print("\nIt is 11 am of a Sunday morning. You wake up as per your routine. "
    "You head out of your bedroom towards the main hall to grab your"
    " newspaper and milk. But you don't see any. Confused, what will you choose to do: ")
    time.sleep(1)
    print("""    A. Go outside and check
    B. Turn on the television and check news
    C. lie down and consider it a dream""")
    choice=input(">>> ")
    if choice in answer_A:
        option_out()
    elif choice in answer_B:
        option_tv()
    elif choice in answer_C:
        print("\nThis is not a dream. Choose another option and face reality. \n")
        intro()
    else:
        print(required)
        intro()

def option_out():
    print("\nYou go outside and see that there was no usual "
          "movement of the residents of the building. Will you: ")
    time.sleep(1)
    print("""    A. Go back inside your house
    B. Ring the neighbour's bell and ask them about it""")
    choice=input(">>> ")
    if choice in answer_A:
        option_inside()
    elif choice in answer_B:
        option_neighbour()
    else:
        print(required1)
        option_out()

def option_tv():
    print("\nYou turn on a news channel and find out about a global"
          " pandemic. It is the Corona virus and it has infected many"
          " people through physical contact. You also find out that "
          " the government has imposed a 1 month lockdown for the "
          " entire country and going out of your house is allowed only"
          " for any essentials.  ")
    print(end)

def option_inside():
    print("\nYou head back in your home and now:")
    time.sleep(1)
    print("""    A. Turn ON the television
    B. Call someone and ask""")
    choice=input(">>> ")
    if choice in answer_A:
        option_tv()
    elif choice in answer_B:
        option_call()
    else:
        print(required1)
        option_inside()

def option_neighbour():
    print("\nYou go and ring your 60 year old neighbour's doorbell. He answers "
          "door. You notice that he is wearing a mask. Avoiding the strange"
          " behaviour you ask to him about the ongoing situation. He begins to"
          " answer but suddenly starts coughing a lot. Seeing this, what will "
          "you do:")
    time.sleep(1)
    print("""    A.Call an ambulance for him
    B.Take him to the hospital in your own car""")
    choice=input(">>> ")
    if choice in answer_A:
        print("\nHe is coughing a lot in the ambulance too. You think to yourself:"
              "poor man living all by himself!\nYou reach the hospital and find out "
              "about a pandemic. The hospital was filled with patients coughing and "
              "vomiting blood. After admitting him, stll confused, you look at the "
              "news on the hospital televsion. You find out about a global"
              " pandemic. It is the Corona virus and it has infected many"
              " people through physical contact. You also find out that "
              " the government has imposed a 1 month lockdown for the "
              " entire country and going out of your house is allowed only"
              " for any essentials.")
        print(end)
    elif choice in answer_B:
        print("\nHe is coughing a lot in the car too. You think to yourself:"
              "poor man living all by himself!\nYou reach the hospital and find out "
              "about a pandemic. The hospital was filled with patients coughing and "
              "vomiting blood. After admitting him, stll confused, you look at the"
              " news on the hospital televsion. You find out about a global"
              " pandemic. It is the Corona virus and it has infected many"
              " people through physical contact. You also find out that "
              " the government has imposed a 1 month lockdown for the "
              " entire country and going out of your house is allowed only"
              " for any essentials.")
        print(end)
    else:
        print(required1)
        option_neighbour()
        
def option_call():
    print("\nYou decide to call someone and ask them about it. "
    "Whom will you call?:")
    time.sleep(1)
    print("""    A. Your parents
    B. Your sibling
    C. Your close friend""")
    choice=input(">>> ")
    if choice in answer_A:
        print("\nYou call your parents and ask them about the unsual activity "
              "you're noticing. They then tell you about a global"
              " pandemic. It is the Corona virus and it has infected many"
              " people through physical contact. They also tell you that "
              " the government has imposed a 1 month lockdown for the "
              " entire country and going out of your house is allowed only"
              " for any essentials.You tell them to take care and then hangup the call.")
        print(end)
    elif choice in answer_B:
        print("\nYou call your sibling and ask her about the unsual activity "
              "you're noticing. She then tells you about a global"
              " pandemic. It is the Corona virus and it has infected many"
              " people through physical contact. She also tells you that "
              " the government has imposed a 1 month lockdown for the "
              " entire country and going out of your house is allowed only"
              " for any essentials.You tell her to take care and then hangup the call.")
        print(end)
    elif choice in answer_C:
        print("\nYou call your friend and ask him about the unsual activity "
              "you're noticing. He then tells you about a global"
              " pandemic. It is the Corona virus and it has infected many"
              " people through physical contact. He also tells you that "
              " the government has imposed a 1 month lockdown for the "
              " entire country and going out of your house is allowed only"
              " for any essentials.You tell him to take care and then hangup the call.")
        print(end)
    else:
        print(required)
        option_call()

intro()

time.sleep(2)

#Day2(stocking)
def stock():
    print("\nDay 2 of your survival has begun ^_^ \nCurrent Corona patients:38  Deaths: 9 "
          "\nCurrent immunity:" , i, "Current food stock: " , f 
          , " \nToday, you want to stock up on the "
          " essentials for your home. Keeping in mind your food-stock and immunity stats,"
          " you choose to stock up the supplies by:")
    time.sleep(1)
    print("""    A. Going to the market
    B. Ordering it through an online grocery delivery app""")
    choice=input(">>> ")
    if choice in answer_A:
        option_market()
    elif choice in answer_B:
        option_order()
    else:
        print(required1)
        stock()

def option_market():
    print("You grab a mask and head towards the store to buy supplies. You buy some stuff "
          "and see that the police has started patroling the area. You were able to grab"
          " only 75% of the things that you aimed to buy. You head back to your home.")
    global f,i
    f=f+37
    i=i-20
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

def option_order():
    print("You decide to order the essentials at your home through an app. "
          "You place the order through:")
    time.sleep(1)
    print("""    A. Grofers
    B. DMart""")
    choice=input(">>> ")
    if choice in answer_A:
          print("\nYou place your order.\nIt is evening and you have received your "
                "complete order and have stocked up on the essentials. Although, due to"
                " contact with the delivery person, you lose some immunity.")
    elif choice in answer_B:
          print("\nYou place your order.\nIt is evening and you have received your "
                "complete order and have stocked up on the essentials. Although, due to"
                " contact with the delivery person, you lose some immunity.")
    else:
        print(required1)
        option_order()
    global f,i
    f=f+50
    i=i-10
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

stock()

time.sleep(2)

#Day5(Household activity)
def activity():
    print("\nDay 5 of your survival has begun ^_^ \nCurrent Corona patients:169  Deaths: 42 "
          "\nCurrent immunity:" , i, "Current food stock:" , f 
          , "  \nToday, you have to do any 2 household activities out of 3."
          "Each one has different rewards. Your 3 activities are: Cleaning windows, Doing laundry"
          " and Mopping floor. You choose these 2 of the 3 activities:")
    time.sleep(1)
    print("""    A. Cleaning windows and Doing laundry
    B. Doing laundry and Mopping Floor
    C. Mopping floor and Cleaning windows""")
    choice=input(">>> ")
    if choice in answer_A:
        option_winlaun() #i=+5,f=-10
    elif choice in answer_B:
        option_launmop() #i=+5,f=-5
    elif choice in answer_C:
        option_mopwin() #i=+10,f=-15
    else:
        print(required)
        activity()

def option_winlaun():
    print("\nYou choose to clean windows and do laundry. You are rewarded with "
          "+10 immunity but lose 15 food")
    global i,f
    f=f-15
    i=i+10
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)
def option_launmop():
    print("\nYou choose to do laundry and Mop the floors. You are rewarded with "
          "+15 immunity but lose 20 food")
    global i,f
    f=f-20
    i=i+15
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

def option_mopwin():
    print("\nYou choose to Mop the floors and clean the windows. You are rewarded with "
          "+15 immunity but lose 25 food")
    global i,f
    f=f-25
    i=i+15
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)
    
activity()

time.sleep(2)

#Day 9(Skill)
sk=0
def skill():
    print("\nDay 9 of your survival has begun ^_^ \nCurrent Corona patients:969  Deaths: 196 "
          "\nCurrent immunity:" , i, "Current food stock: " , f 
          , )
    global sk     
    print("Today, amidst the lockdown, you decide to learn a new skill to pass your time "
          "and also because everyone else is doing it too :) You have 3 options in hand,"
          " you choose:")
    time.sleep(1)
    print("""    A. to learn to play guitar
    B. to learn a new language
    C. to learn to make a new dish""")
    choice=input(">>> ")
    if choice in answer_A:
        sk=1
        option_instru()
    elif choice in answer_B:
        sk=2
        option_lang()
    elif choice in answer_C:
        sk=3
        option_dish()
    else:
        print(required)
        skill()

def option_instru():
    print("\nYou decide to learn to play guitar. You gain +5 immunity but lose 15 food"
          " because of all the hardwork while learning it. ")
    global i,f
    f=f-15
    i=i+5
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

def option_lang():
    print("\nYou decide to learn a new language. You gain +0 immunity but lose 10 food"
          " because of all the hardwork while learning it. ")
    global i,f
    f=f-10
    i=i+0
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

def option_dish():
    print("\nYou decide to learn to make a new dish. You gain +5 immunity but lose 15 food"
          " because of the consumption of food while making it. ")
    global i,f
    f=f-15
    i=i+5
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

skill()

time.sleep(2)

#Day 11(restock)
def day11():
    print("\nDay 11 of your survival has begun ^_^ \nCurrent Corona patients: 1420  Deaths: 304"
          "\nCurrent immunity:" , i, "Current food stock: " , f 
          , )
    print("\nToday, you have to restock the food items again for yourself to survive. So, you"
          " need to go grocery shopping. You want to restock by:")
    time.sleep(1)
    print("""    A. Going to the market
    B. Ordering it through an online grocery delivery app""")
    choice=input(">>> ")
    if choice in answer_A:
        option_market2()
    elif choice in answer_B:
        option_order2()
    else:
        print(required1)
        day11()    
        
def option_market2():
    print("\nThis time, you take all the necesarry precations while going out like mask,"
          "gloves and hand sanitizer. You buy all the necesarry items and are all stocked"
          "up.")

def option_order2():
    print("Instead of going out, you decide to order in all the items .So, you buy it from:")
    time.sleep(1)
    print("""    A. Grofers
    B. DMart""")
    choice=input(">>> ")
    if choice in answer_A:
          print("\nYou place your order.\nIt is evening and you have received your "
                "complete order and have stocked up on the essentials. Although, due to"
                " contact with the delivery person, you lose some immunity.")
    elif choice in answer_B:
          print("\nYou place your order.\nIt is evening and you have received your "
                "complete order and have stocked up on the essentials. Although, due to"
                " contact with the delivery person, you lose some immunity.")
    else:
        print(required1)
        option_order2()
day11()

def movie():
    print("After the restocking, you now want to relax and watch a movie. You pick your"
          " favourite genre:")
    time.sleep(1)
    print("""    A. Horror
    B. Thriller
    C. Rom-Com""")
    choice=input(">>> ")
    if choice in answer_A:
        print("\nYou're now enjoying your horror movie and are reaching towards the end of "
              "the day.")
        
    elif choice in answer_B:
        print("\nYou're now enjoying your thriller movie and are reaching towards the end of "
              "the day.")
       
    elif choice in answer_C:
        print("\nYou're now enjoying your rom-com movie and are reaching towards the end of "
              "the day.")
    else:
        print(required)
        movie()
    global f,i
    f=f+50
    i=i-15
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)
movie()

time.sleep(2)

#Day 15(Video call)
def vcall():
    print("\nDay 15 of your survival has begun ^_^ \nCurrent Corona patients: 2120  Deaths: 454"
          "\nCurrent immunity:" , i, "Current food stock: " , f 
          , )
    print("\nToday, amongst the increasing Corona virus around, you want to talk to someone on"
          " a video call. So, you decide to call: ")
    time.sleep(1)
    print("""    A. Your parents
    B. Your friends""")
    choice=input(">>> ")
    if choice in answer_A:
        option_parentsvc()
    elif choice in answer_B:
        option_friendsvc()
    else:
        print(required1)
        vcall()

def option_parentsvc():
    print("\nYou decide to call your parents. The platform you choose for making the video call"
          " is: ")
    time.sleep(1)
    print("""    A. Zoom 
    B. Google Meet 
    C. Facetime""")
    choice=input(">>> ")
    if choice in answer_A:
        option_zoom()
    elif choice in answer_B:
        option_meet()
    elif choice in answer_C:
        option_facetime()
    else:
        print(required)
        option_parentsvc()

def option_friendsvc():
    print("\nYou decide to call your friends. The platform you choose for making the video call"
          " is: ")
    time.sleep(1)
    print("""    A. Zoom 
    B. Google Meet 
    C. Facetime""")
    choice=input(">>> ")
    if choice in answer_A:
        option_zoom()
    elif choice in answer_B:
        option_meet()
    elif choice in answer_C:
        option_facetime()
    else:
        print(required)
        option_friendsvc()
    
def option_zoom():
    print("\nYou start a video call on Zoom. You feel good after talking with them now."
          " You end you day peacefully today.")
    global f,i
    f=f-10
    i=i
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

def option_meet():
    print("\nYou start a video call on Google Meet. You feel good after talking with them now."
          " You end you day peacefully today.")
    global f,i
    i=i
    f=f-10
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

def option_facetime():
    print("\nYou start a video call on Facetime. You feel good after talking with them now."
          " You end you day peacefully today.")
    global f,i
    i=i
    f=f-10
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end)

vcall()

time.sleep(2)

#Day 21(use of skill)
def useskill():
    global i,f
    print("\nDay 21 of your survival has begun ^_^ \nCurrent Corona patients: 4928  Deaths: 719"
          "\nCurrent immunity:" , i, "Current food stock: " , f 
          , )
    print("Today, you are gonna put your learned skill to use. The skill you chose was: ")
    if sk==1:
        print("To learn guitar.")
        print("While at home, you have mastered playing guitar. So, you take part in a local"
              " 'Online Guitar Playing Competition'. It winning candidate gets a cash prize of INR 10k"
              "The competition starts and soon it is your turn. You play wornderfully. "
              "The results are being announced: '- and on the first place is (you)!!!!!' "
              "You recieve the voucher through Paytm. You gain immunity and lose some food ")
        f=f-10
        i=i+5
        print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
        print(end)
    
    elif sk==2:
        print("To learn a new language")
        print("While at home, you learnt a new language and in some days your office has an international"
              " client meeting. So now you a opportunity to impress your boss by taking up this"
              " international project. So now you decide to take it and make good profit out of it."
              " The day is here and you flaunt your flawless skill and have impressed your boss"
              " which might lead to a promotion. Good Job!!!!! You gain immunity and lose some food ")
        f=f-10
        i=i+5
        print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
        print(end)
        
    else:
        print("To learn a new dish")
        print("While at home, you learnt to cook good food so you decide to share some with your"
              " 60 year old neighbour too. You prepare a nice dish as a welcome home from the "
              "hospital gift. You lost some food while preparing the dish. The neighbour "
              "on the contrary gives you some food as a return favour, too. Splendid work!!!!"
              " Altough you lose some immunity as you come in contact of a covid positive patient.")
        f=f+5
        i=i-5
        print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
        print(end)
        
useskill()

time.sleep(6)

#Day 30(THE D-DAY)
def dday():
    print("\nDay 30, the final day of your survival has begun ^_^ \nCurrent Corona patients: 6969  Deaths: 1042"
          "\nCurrent immunity:" , i, "Current food stock: " , f 
          , )
    print("\nToday is the final day of your survival :0  Government has finalised safe vaccines"
          " for public use. You are an eligible citizen to get the vaccine and vaccine is "
          "already available for you. So you decide to: ")
    time.sleep(1)
    print("""    A. Take the vaccine
    B. Avoid the vaccine""")
    choice=input(">>> ")
    if choice in answer_A:
        option_take()
    elif choice in answer_B:
        option_donttake()
    else:
        print(required1)
        dday()

def option_take():
    print("\nYou take the vaccine like a responsible citizen. After being at home for so many days"
          " you are bored and you want to go out but the fear of corona virus haunts you. So,"
          " what will you choose:")
    time.sleep(1)
    print("""    A. Go out and finally release the boredom
    B. Stay at home and find something interesting to do""")
    choice=input(">>> ")
    if choice in answer_A:
        option_takeout()
    elif choice in answer_B:
        option_takestay()
    else:
        print(required1)
        option_take()

def option_takeout():
    print("\nYou go out and meet your friends after taking the vaccine. Unforunately, you get"
          " affected by the Corona virus from one of your friend and DIE instantly due to"
          " shortage of oxygen at that moment. YOU SHOULD'VE LISTENED TO THE GOVERNMENT! ")
    print("\nCurrent immunity stats: 0")
    print(end2)
def option_takestay():
    print("\nYou stay at your home like a responsible citizen after taking the vaccine. "
          "CONGRATULATIONS!!! You survive the pandemic. You are now rewarded with extra "
          "years to live:) ")
    print(end2)

def option_donttake():
    print("\nYou don't take the vaccine because you are scared of needles :0 You now have"
          " the option to either stay at home or go out and have a break from the daily life.")
    time.sleep(1)
    print("""    A. Go out and finally release the boredom
    B. Stay at home and find something interesting to do""")
    choice=input(">>> ")
    if choice in answer_A:
        option_dtakeout()
    elif choice in answer_B:
        option_dtakestay()
    else:
        print(required1)
        option_donttake()

def option_dtakeout():
    print("\nYou go out and meet your friends after taking the vaccine. Unforunately, you get"
          " affected by the Corona virus from one of your friend and DIE instantly due to"
          " shortage of oxygen at that moment. YOU SHOULD'VE LISTENED TO THE GOVERNMENT! ")
    print("\nCurrent immunity stats: 0")
    print(end2)

def option_dtakestay():
    print("\nYou decide to stay at home. Although your immunity drops drastically now. You fall sick."
          " You could still do better at surviving the pandemic :) ")
    global f,i
    f=f-10
    i=i%2
    print("\nCurrent immunity stats:", i, "\nCurrent food stock stats:",f)
    print(end2)

dday()
