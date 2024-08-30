import Authentication
import QuickModeGame

print("\n\n\nWelcome.................")

#-----------------------Authentication------------------------
i=1
while(i==1):
    print("\n\n---------------Select Option------------")
    print("1.Login\n2.Sign Up(New Player)\n3.Exit()\n")

    option=int(input("   >>"))

    if(option==1):
        is_player,player_name=Authentication.login()
        print(f"\n\nWelcome Back,  {player_name}")
        i+=1
    elif(option==2):
        is_player,player_name=Authentication.signUp()
        print(f"\n\nHello {player_name}")
        i+=1
    elif(option==3):
        print("Bye Bye ")
        i+=1
        exit()
    else:
        print("Invalid Choice!!")

#-----------------------Authentication------------------------




#-----------------------Game------------------------
x=1
while(x==1):
    print("\nLets Play")
    print("\n------------Select Mode----------")
    print(" 1.Quick Mode(Easy,Normal,Hard,.....)\n 2.Carrier Mode(level)\n 3. Exit(Don't Want to play Right now!!) ")
    choice=int(input("   >>"))

    if(choice==1):
        i=5
        while(i>=0):
            print("\n\n\n-----------Quick Mode---------------")
            print(" 1.Easy\n 2.Normal\n 3.Hard\n 4.Exit(Don't Want to play Right now!!) ")
            choice=int(input("   >>"))
            if(choice==1):
                QuickModeGame.easy(player_name)

            elif(choice==2):
                QuickModeGame.Normal(player_name)

            elif(choice==3):
                QuickModeGame.Hard(player_name)

            elif(choice==4):
                print(f"Bye Bye {player_name}")
                exit()
            else:
                print("Invalid Choice!!")

        
            i-=1



    elif(choice==2):
        print("-----------Carrier Mode--------------")
        print("Comming Soon!!")


    elif(choice==3):
        print("Exiting--------->")
        print("  #Good Bye!!\n  #See Yoy Again")


    else:
        print("Invalid Choice!!")



#-----------------------Game------------------------



print("-----End------End------End-------End------End-----End-------End-------End-------End----")