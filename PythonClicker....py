import random
import time 

def stackcount(times,variable,starting):                                                                   #For stack buy on item one and two
    price=0
    for i in range(times):
        price=price+starting
        starting=starting*variable
    return price
print("Welcome to the Mario python clicker! Press . , then enter. Type shop to buy something")
count=0
clickAmount=1
Onep=1
Twop=1
ThreeP=0
level=0
timePrev=time.time()
lvl1=False
lvl2=False
lvl3=False
lvl4=False
lvl5=False
lvl6=False
fiveMreward=20
while True:
    if time.time()-timePrev>300:
        timePrev=time.time()
        count+=fiveMreward
        print("You have played for 5 whole minutes! You get "+str(fiveMreward)+" clicks!")
    inpu=input("You have "+ str(count) + " clicks! Keep on going!")
    if count>10:                                                                     #level for unlocking shop items
        lvl1=True                                                                     #level for unlocking shop items
        level=1                                                                     #level for unlocking shop items
    if count>100:                                                                     #level for unlocking shop items
        lvl2=True                                                                     #level for unlocking shop items
        level=2                                                                     #level for unlocking shop items
    if count>500:
        lvl3=True
        level=3
    if count>1000:
        lvl4=True
        level=4
    if inpu==".":                                                                   #Pure click
        count=count+clickAmount                                                                    #Pure click
        print("    .-++=--=++-.    \n  :===:..  ..:===:  \n.-+=.   .--.   .=+-.\n:=-.    +  +    .-=-\n+=.     +  +     .=+\n+=      +  +      ++\n+=.     +  +     .=+\n:=-.    +  +    .-=-\n.-+=.   .--.   .=+=.\n  :===:..  ..:==+:  \n    .=++=--=++=.")
    if inpu=="shop":
        print("Type 1 musthroom that you let's you get +1 clicks per click. It costs "+str(Onep))                                       #Shop asking
        if lvl1==True:
            print("Type 2 for an Tanooki suit that reduces the cost of a item by 1. It costs "+str(Twop))                                          #Shop asking
        if lvl2==True:
            print("Type 3 for a mystery item. Some of the possible results include new items, clicks and more")
        if lvl3==True:
            print("Type 4 for an Flame flower that increases your 5 minute bonus by 10 for 15 clicks")                                                         #Shop asking
        print("Type exit to exit shop")                                                                                                    #Shop asking
        shopChoice=input()
        if shopChoice=="1":
            amount=int(input("How many?"))
            if stackcount(amount,2,Onep)<=count:                                                                                           #stack count check
                count=count-stackcount(amount,2,Onep)                                                                                      #taking away from count 
                print(str(amount)+" bought!")                                                                                              #Buy confirm
                print("       -+----+-       \n    .##.      .##-    \n  .###          ###.  \n .+###          ###+. \n ..###.        .###-..\n- +####+      +####+ -\n-.##################.-\n-####################+\n -###.  -    +  -###+ \n   --   +.  .+   --   \n   .            .    \n      .-.    .-.   ")
                clickAmount=clickAmount+1*amount                                                                                           #Implementing shop item
                Onep=Onep*2**amount                                                                                                        #Price increase 
            else:
                print("You do not have enough to buy this")                                                                                 #Not enogh message
        if shopChoice=="2" and lvl1==True:
            amount=int(input("How many?"))                                                                                                  #Number 2 check
            if Twop*stackcount(amount,3,Twop)<=count:                                                                                           #taking away from count check
                count=count-stackcount(amount,3,Twop)                                                                                           #taking away from count
                if Onep*stackcount(amount,3,Twop)>1:                                                                                                               #One shop cheapen check
                    Onep=Onep-1*amount                                                                                                          #One shop cheapen 
                    print("Number 2 bought")
                    print("                            .#########-             \n                          ---.          -+           \n                        .+.       -#-   .#.          \n                      .+.   -#-+#+      .#           \n                     --     ###+..    .--            \n                  +-  +-.+.          #-             \n                 -#    ###          -#               \n               --. .  ------.     .-.                \n               #-  #####-      +##.                  \n             -#  .+         -##.                     \n            -#####      ----                         \n           #####+.......                             \n           ##- ")                  
                if Twop*amount>1:
                    Twop=Twop*3*amount
                    Twop=Twop-1*amount
                else:
                    Twop=Twop*3*amount
            else:
                print("You do not have enough to buy this")
        if shopChoice=="3"and lvl2==True:
            print("What rarity?")
            print("Type 1 for common. It costs 50 clicks")
            if lvl3==True:
                print("2 for rare. It costs 500 clicks")
            if lvl4==True:
                print("3 for rare. It costs 5000 clicks")
            mysteryChoice=int(input())
            if mysteryChoice==1:    
                count=count-50
                mysteryBox=random.randint(1,15)
                if mysteryBox==1 or mysteryBox==11 or mysteryBox==12:
                    print("You gained 60 clicks!")
                    count=count+60
                if mysteryBox==2 or mysteryBox==13:
                    if count<5:
                        print("You didn't get anything")
                    else:
                        print("You lost 5 clicks...")
                        count=count-5
                if mysteryBox==3:
                    print("All your shop item's price increase by 1")
                    Onep=Onep+1
                    Twop=Twop+1
                if mysteryBox==4:
                    print("All your shop item's price decrease by 1!")
                    Onep=Onep-1
                    Twop=Twop-1
                if mysteryBox==5:
                    print("You got 70 clicks!")
                    count=count+70
                if mysteryBox==6:
                    print("You got 100 clicks!")
                    count=count+100
                if mysteryBox==7:
                    if count<20:
                        if count<=0:
                            print("You didn't get anything")
                        else:
                            print("You lost "+str(count)+" clicks...")
                            count=0
                    print("You lost 20 clicks...")
                    count=count-20
                if mysteryBox==8 or mysteryBox==14:
                    print("You got back your 50 clicks")
                    count=count+50
                if mysteryBox==9:
                    timeWait=time.time()
                    while time.time()-timeWait>60:
                        timePrev=time.time()
                if mysteryBox==10 or mysteryBox==15:
                    print("You didn't get anything...")
                #________________________________________________________rare
            if mysteryChoice==2 and lvl3==True:
                mysteryBox=random.randint(1,15)
                if mysteryBox==1:
                    if mysteryBox==1 or mysteryBox==11 or mysteryBox==12:
                        print("You gained 600 clicks!")
                    count=count+600
                if mysteryBox==2 or mysteryBox==13:
                    if count<125:
                        print("You didn't get anything")
                    else:
                        print("You lost 125 clicks...")
                        count=count-125
                if mysteryBox==3:
                    print("All your shop item's price increase by 10")
                    Onep=Onep+10
                    Twop=Twop+10
                if mysteryBox==4:
                    print("All your shop item's price decrease by 5...")
                    Onep=Onep-5
                    Twop=Twop-5
                if mysteryBox==5:
                    print("You got 700 clicks!")
                    count=count+700
                if mysteryBox==6:
                    print("You got 1000 clicks!")
                    count=count+1000
                if mysteryBox==7:
                    if count<100:
                        if count<=0:
                            print("You didn't get anything")
                        else:
                            print("You lost "+str(count)+" clicks...")
                            count=0
                    print("You lost 100 clicks...")
                    count=count-100
                if mysteryBox==8 or mysteryBox==14:
                    print("You got back your 500 clicks")
                    count=count+500
                if mysteryBox==9:
                    print("Wait 5 minute before continuing")
                    timeWait=time.time()
                    while time.time()-timeWait>300:
                        timePrev=time.time()
                if mysteryBox==10 or mysteryBox==15:
                    print("You didn't get anything...")
                                    #________________________________________________________legendary
            if mysteryChoice==3 and lvl4==True:
                mysteryBox=random.randint(1,15)
                if mysteryBox==1:
                    if mysteryBox==1 or mysteryBox==11 or mysteryBox==12:
                        print("You gained 6000 clicks!")
                    count=count+6000
                if mysteryBox==2 or mysteryBox==13:
                    if count<625:
                        print("You didn't get anything")
                    else:
                        print("You lost 625 clicks...")
                        count=count-625
                if mysteryBox==3:
                    print("All your shop item's price increase by 10")
                    Onep=Onep+10
                    Twop=Twop+10
                if mysteryBox==4:
                    print("All your shop item's price decrease by 5...")
                    Onep=Onep-5
                    Twop=Twop-5
                if mysteryBox==5:
                    print("You got 7000 clicks!")
                    count=count+7000
                if mysteryBox==6:
                    print("You got 10000 clicks!")
                    count=count+10000
                if mysteryBox==7:
                    if count<5000:
                        if count<=0:
                            print("You didn't get anything")
                        else:
                            print("You lost "+str(count)+" clicks...")
                            count=0
                    print("You lost 5000 clicks...")
                    count=count-5000
                if mysteryBox==8 or mysteryBox==14:
                    print("You got back your 500 clicks")
                    count=count+500
                if mysteryBox==9:
                    print("Wait 5 minute before continuing")
                    timeWait=time.time()
                    while time.time()-timeWait>300:
                        timePrev=time.time()
                if mysteryBox==10 or mysteryBox==15:
                    print("You didn't get anything...")
        if shopChoice=="4" and lvl3==True:
            amount=int(input("How many?"))
            if amount*ThreeP<=count:                                                                                           #stack count check
                count=count-amount*ThreeP                                                                                      #taking away from count 
                print(str(amount)+" bought!")                                                                                              #Buy confirm    
                fiveMreward+=10*amount                                                                                                            #Implementing shop item                                                                                            #Price increase 
            else:
                print("You do not have enough to buy this")      