# program to insert a number in a sorted list

def insert_num(arr, n):
    get_index = len(arr)
    for i in range(len(arr)):
        if arr[i] > n:
            get_index = i
            break
    if get_index == len(arr):
        arr = arr[:get_index] + [n]
    else:
        arr = arr[:get_index] + [n] + arr[get_index:]
    print(arr)


int_list = [1, 3, 5, 10, 12]
num = 61
insert_num(int_list, num)