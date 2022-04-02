# Write a python program to find common char in two different string. eg. f(hello, world) ---> lo
s1 = input("Enter first string:")
s2 = input("Enter second string:")
common_char = list()
common_char.append(list(set(s1) & set(s2)))
print("The common letters are:", common_char)
