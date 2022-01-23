def getdate():
    import datetime
    return datetime.datetime.now()
def log_input_lubna(log):
    f = open("Lubna.txt","a")
    f.write(str(getdate()))
    f.write(" ")
    f.write(log)
    f.write(" \n")
    f.close()
def log_input_nayla(log):
    f = open("Nayla.txt", "a")
    f.write(str(getdate()))
    f.write(" ")
    f.write(log)
    f.write(" \n")
    f.close()
def log_input_khushi(log):
    f = open("Khushi.txt","a")
    f.write(str(getdate()))
    f.write(" ")
    f.write(log)
    f.write(" \n")
    f.close()

def retrieve_lubna():
    f = open("Lubna.txt")
    a =f.read()
    print(a)
    f.close()
def retrieve_nayla():
    f = open("Nayla.txt")
    a =f.read()
    print(a)
    f.close()
def retrieve_khushi():
    f = open("Khushi.txt")
    a =f.read()
    print(a)
    f.close()
global inputs
inputs=True
def health():
    inputs = True
    while(inputs==True):
        print("Welcome to Health Management Portal !")
        user_name = input("Enter number corresponding to person's name who you want to "
                          "log/retrieve data: \n"
                          "1. Lubna \n 2. Nayla \n 3. Khushi \n")
        user_action = input("Enter action you want to perform: \n"
                            "1. Log into file\n 2. Retrieve data\n")
        if user_name == "1":
            if user_action == "1":
                user_log = input("Enter the data you want to insert: \n")
                log_input_lubna(user_log)
                print("Thank you! \n Your input has been saved..\n")
                inputs = False
            elif user_action == "2":
                retrieve_lubna()
                inputs = False
        if user_name == "2":
            if user_action == "1":
                user_log = input("Enter the data you want to insert: \n")
                log_input_nayla(user_log)
                print("Thank you! \n Your input has been saved..\n")
                inputs = False
            elif user_action == "2":
                retrieve_nayla()
                inputs = False
        if user_name == "3":
            if user_action == "1":
                user_log = input("Enter the data you want to insert: \n")
                log_input_khushi(user_log)
                print("Thank you! \n Your input has been saved..\n")
                inputs = False
            elif user_action == "2":
                retrieve_khushi()
                inputs = False
    if inputs == False:
        print("Do you wish to perform other action or exit? \n")
        ans = input("Press Y to continue \n E to exit\n")
        if ans == "Y":
            health()
        elif ans == "E":
            exit()

health()
