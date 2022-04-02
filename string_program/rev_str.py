# program to reverse the character in string
def reverse_str(str_arr):
    revrse_str = []
    for i in range(len(str_arr)):
        revrse_str.append(str_arr[-i])
    print(revrse_str)
    revrse_str = str_arr[::-1]
    print(revrse_str)


input_str = " hello world"
reverse_str(input_str)