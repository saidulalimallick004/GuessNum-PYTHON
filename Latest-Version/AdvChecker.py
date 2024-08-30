def check(ans_num,usr_num):

    currect_match=0
    fully_wrong=0
    pos_incurrect=0

    for i in range(len(ans_num)):

        for j in range (len(usr_num)):

            if(ans_num[i]==usr_num[j] and i==j):
                currect_match+=1
            
            elif(ans_num[i]==usr_num[j] and i!=j):
                pos_incurrect+=1

            else:
                fully_wrong+=1
