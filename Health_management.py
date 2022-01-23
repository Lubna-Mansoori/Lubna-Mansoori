def getdate():
    import datetime
    return datetime.datetime.now()
def log_input_Patient_1(log):
    f = open("Patient_1.txt","a")
    f.write(str(getdate()))
    f.write(" ")
    f.write(log)
    f.write(" \n")
    f.close()
def log_input_Patient_2(log):
    f = open("Patient_2.txt", "a")
    f.write(str(getdate()))
    f.write(" ")
    f.write(log)
    f.write(" \n")
    f.close()
def log_input_Patient_3(log):
    f = open("Patient_3","a")
    f.write(str(getdate()))
    f.write(" ")
    f.write(log)
    f.write(" \n")
    f.close()

def retrieve_Patient_1():
    f = open("Patient_1.txt")
    a =f.read()
    print(a)
    f.close()
def retrieve_Patient_2():
    f = open("Patient_2.txt")
    a =f.read()
    print(a)
    f.close()
def retrieve_Patient_3():
    f = open("Patient_3.txt")
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
                          "1. Patient_1 \n 2. Patient_2 \n 3. Patient_2 \n")
        user_action = input("Enter action you want to perform: \n"
                            "1. Log into file\n 2. Retrieve data\n")
        if user_name == "1":
            if user_action == "1":
                user_log = input("Enter the data you want to insert: \n")
                log_input_Patient_1(user_log)
                print("Thank you! \n Your input has been saved..\n")
                inputs = False
            elif user_action == "2":
                retrieve_Patient_1()
                inputs = False
        if user_name == "2":
            if user_action == "1":
                user_log = input("Enter the data you want to insert: \n")
                log_input_Patient_2(user_log)
                print("Thank you! \n Your input has been saved..\n")
                inputs = False
            elif user_action == "2":
                retrieve_Patient_2()
                inputs = False
        if user_name == "3":
            if user_action == "1":
                user_log = input("Enter the data you want to insert: \n")
                log_input_Patient_3(user_log)
                print("Thank you! \n Your input has been saved..\n")
                inputs = False
            elif user_action == "2":
                retrieve_Patient_3()
                inputs = False
    if inputs == False:
        print("Do you wish to perform other action or exit? \n")
        ans = input("Press Y to continue \n E to exit\n")
        if ans == "Y":
            health()
        elif ans == "E":
            exit()

health()
