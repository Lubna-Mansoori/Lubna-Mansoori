print("Welcome to next palindrome generator !!")
no_of_inputs = int(input("Enter number of test cases: "))
user_list = []
for i in range(no_of_inputs):
    user_input = input("Enter your number: ")
    user_list.append(int(user_input))
for items in user_list:
    if items > 99:
        num = str(items)
        if len(num) % 2 == 0:
            leng = int(len(num) / 2)
            left = num[:leng][::-1]
            new_num = num[:leng] + left
            if int(new_num) < int(num):
                no1 = int(new_num[leng - 1])+1
                no2 = int(new_num[leng])+1
                new_num = new_num[:leng - 1] + str(no1) + str(no2) + new_num[leng + 1:]
        else:
            leng = int(len(num) / 2)
            left = num[:leng][::-1]
            new_num = num[:leng+1] + left
            if int(new_num) < int(num):
                no = int(new_num[leng])
                no = no + 1
                new_num = new_num[:leng] + str(no) + new_num[leng + 1:]
        print(f"Next palindrome of {items} is {new_num}")
    else:
        print("Invalid number !!")
