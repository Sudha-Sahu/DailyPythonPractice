# Get nth max/min from a list, take 3 params as input, 1. given list, 2. n, 3. min/max
def get_min_max(arr, k, _max=True):
    if _max:
        return arr[k-1]
    if not _max:
        return arr[-k]


if __name__ == "__main__":
    my_list = [1, 5, 8, 12, 3, 17, 13]
    print(my_list)
    my_list.sort()
    print(my_list)
    num1 = get_min_max(my_list, 2, _max=False)
    print("the max element : ", num1)
    num2 = get_min_max(my_list, 2)
    print("the min element : ", num2)