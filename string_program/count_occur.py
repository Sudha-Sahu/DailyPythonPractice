# program to calculate occurence of each letter in the sentence

def get_occurance(string_arr):
    count_char = {}

    for ch in string_arr:
        if ch in count_char:
            count_char[ch] += 1
        else:
            count_char[ch] = 1
    print(count_char)


string_list = "hello How  are you, doing well?"
get_occurance(string_list)