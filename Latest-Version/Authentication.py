
def signUp():
    print("----------SignUp-----------")

    set_name=input("Set player NickName: ")

    try:
        niknam=open(f"Latest-Version\kt\.hidden\{set_name}.ook","r")
        print("Nickname Already Exist!!")
        print("Try another One.....")    
        

    except:
        set_password=input("set Password: ")
        niknam=open(f"Latest-Version\kt\.hidden\{set_name}.ook","w")
        niknam.write(f"{set_password}")
        return True,set_name





        
#-------------------------------------------------------------------------------



def login():
    print("-------------Login-------------")
    input_name=input("Enter Nickname: ")
    input_password=input("Enter Password: ")

    i=3
    while(i>=1):
        try:
            niknam=open(f"Latest-Version\kt\.hidden\{input_name}.ook","r")
            origina_password=niknam.read()
            if(origina_password==input_password):

                return True,input_name

        except FileNotFoundError:
            print("Autentication Failed\n invalid login Detail")

        i-=1
    #----------------------------------------------------------------------