# sum of all positive and negative numbers separately from 1 array
num = int(input("enter how many number you want to enter : "))
integer_list = []
for i in range(num):
    integer_list.append(int(input("Enter any positive and  negative integer : ")))

print(integer_list)
sum_posi = 0
neg_posi = 0
for j in range(num):
    if integer_list[j] > 0:
        sum_posi += integer_list[j]
    if integer_list[j] < 0:
        neg_posi += integer_list[j]
print("sum of positive integer is : ", sum_posi)
print("sum of negative integer is : ", neg_posi)