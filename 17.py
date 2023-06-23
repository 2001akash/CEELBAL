# Given a string of odd length greater than 7, return a new string made of the middle three characters of a given string
def get_middle_three_chars(string):
    length = len(string)
    middle_index = length // 2
    return string[middle_index - 1:middle_index + 2]

str1 = "JhonDipPeta"
str2 = "JaSonAy"

result1 = get_middle_three_chars(str1)
result2 = get_middle_three_chars(str2)

print("Output:")
print(result1)
print(result2)
