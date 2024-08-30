

def takeFromUser(size):
    print(f"\n\n\n\nYou have to Guess {size} Numbers.\n")
    usr_num=[]
    for i in range(size):
        usr_num.append(int(input(f"Enter Num_{i}: ")))


    return usr_num