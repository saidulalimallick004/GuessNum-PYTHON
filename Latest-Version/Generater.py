import random

def numGenerator(a):
    num=[]

    for i in range(a):
        num.append(random.randint(0,9))


    print(num)
    return num