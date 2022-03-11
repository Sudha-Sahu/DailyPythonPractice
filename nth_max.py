# program to find the nth largest number in the array
def nth_largest(arr):
    arr.sort()
    return arr


my_list = [3, 5, 1, 4, 0, 2]
print(my_list)
posi = int(input("enter the position of nth largest element : "))
my_list = nth_largest(my_list)
print(my_list)
print("the nth largest number in the array is : ", my_list[-posi])
