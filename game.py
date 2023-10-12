#Define Function............

def check_input1(password):
    print("======LEVEL 1======")
    for i in range(10):
        print("<__>")
        pass1=int(input("1st Num >>"))
        pass2=int(input("2nd Num >>"))
        if(pass1==password[0]):
            print("1st Number is Correct <_>")
            if(pass2==password[1]):
                print("2nd Number is also currect <_>")
                print(password)
                print("Congratulations!!\n <->You crack the password<->")

                return
            else:
                print("2nd number is False!!\n Try Again!!")

        elif(pass2==password[1]):
            print("1st Number is incorrect!!")
            print("2nd Number is Correct <_>")

        else:
            print("Both are incorrect!!\n Try again!!")

#-------------------------------------------------------

#main programs......
print("Welcome........")
name_user=input("Enter Your Name: \n  >>")
print("Hello",name_user)


start=input("Enter 'S' to Start\n  >>")
if(start=='s' or start=='S'):

    print("Let's Begin the GAME......")
    print("Press 1=Level 1")
    print("Press 2=Level 2")
    print("Press 3=Level 3")
    game_level=int(input("  >>"))
    password=[]
    if(game_level==1):
        for i in range(2):
            import random
            p1=(random.randint(0, 9))
            password.append(p1)
        check_input1(password)

    else:
        print("You can play only Level 1.\nOther Level Coming Soon!!")

print(" Good Bye!!\n See you again!!")
