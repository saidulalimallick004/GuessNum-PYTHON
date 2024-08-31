import Generater
import Checker
import TakeInput

def easy(player_name):
    print("\n\n\n>>Mode: Easy----------------------------------------------------------")
    size=2

    ans_num=Generater.numGenerator(size)
    
    i=10
    while(i>=0):
        usr_num=TakeInput.takeFromUser(size)
        if(Checker.check(ans_num,usr_num)):
            print("Congratulation!!\n   >>You Crack the Password ^_^")
            print(f"   >>{player_name}, You are Great")
            return 
        else:
            print("Wrong !!\n   >>Try Again!!")
            print(f"   >>{player_name}, You can do it.....")
            i-=1



def Normal(player_name):
    print("\n\n\n>>Mode: Normal----------------------------------------------------------")
    size=3

    ans_num=Generater.numGenerator(size)
    
    i=10
    while(i>=0):
        usr_num=TakeInput.takeFromUser(size)
        if(Checker.check(ans_num,usr_num)):
            print("Congratulation!!\n   >>You Crack the Password ^_^")
            print(f"   >>{player_name}, You are Great")
            return 
        else:
            print("Wrong !!\n   >>Try Again!!")
            print(f"   >>{player_name}, You can do it.....")
            i-=1




def Hard(player_name):
    print("\n\n\n>>Mode: Hard----------------------------------------------------------")
    size=4

    ans_num=Generater.numGenerator(size)
    
    i=10
    while(i>=0):
        usr_num=TakeInput.takeFromUser(size)
        if(Checker.check(ans_num,usr_num)):
            print("Congratulation!!\n   >>You Crack the Password ^_^")
            print(f"   >>{player_name}, You are Great")
            return 
        else:
            print("Wrong !!\n   >>Try Again!!")
            print(f"   >>{player_name}, You can do it.....")
            i-=1
