# program to insert a list in a sorted list
def insert_num(arr1, arr2):
    get_index = len(arr1)
    for n in arr2:
        for i in range(len(arr1)):
            print(i)
            if arr1[i] > n:
                get_index = i
                break
        if get_index == len(arr1):
            arr1 = arr1[:get_index] + [n]
        else:
            arr1 = arr1[:get_index] + [n] + arr1[get_index:]
    print(arr1)


int_list1 = [1, 3, 5, 10, 12]
int_list2 = [2, 6, 11]
insert_num(int_list1, int_list2)
