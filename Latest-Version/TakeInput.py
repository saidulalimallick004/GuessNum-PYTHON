

def takeFromUser(size):

    print(f"\nYou have to Guess {size} Numbers.\n\n\n")
    usr_num=[]
    for i in range(size):
        try:
            usr_num.append(int(input(f"Enter Num_{i}: ")))
        except:
            print("Enter between:0-9")
            

    return usr_num