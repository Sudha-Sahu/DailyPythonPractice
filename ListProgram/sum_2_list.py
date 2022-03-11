# sum of elements of 2 array at position
def sum_of_list(arr1, arr2):
    new_list = []
    len_list = len(arr1)
    for x in range(len_list):
        new_list.append(arr1[x]+arr2[x])
    print("added elements of two different list : ", new_list)


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
sum_of_list(list1, list2)
