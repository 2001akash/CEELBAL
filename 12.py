# Reverse a given integer number
number = int(input("Enter an integer number: "))
reverse = 0

while number != 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number //= 10

print("Reversed number:", reverse)
