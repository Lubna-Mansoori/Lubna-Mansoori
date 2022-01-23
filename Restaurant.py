
print("Welcome to the Restaurant")
input_list =[int(item) for item in input("Enter your list...\n").split(" ")]
list_1 = list(reversed(input_list))
print("Reversing using reverse ",list_1)
print("Reversing using slicing ",input_list[::-1])
leng = int(len(input_list)/2)
for i in range(0, leng):
    input_list[i], input_list[-i-1] = input_list[-i-1], input_list[i]
print("Reversing using swapping",input_list)
