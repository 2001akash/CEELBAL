# reverse the list
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []

# Using a loop to reverse the list
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])

print("Reversed list:", reversed_numbers)
