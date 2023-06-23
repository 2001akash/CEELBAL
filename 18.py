# Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
s1 = "Ault"
s2 = "Kelly"

middle_index = len(s1) // 2
result = s1[:middle_index] + s2 + s1[middle_index:]

print("Expected Output:")
print(result)
