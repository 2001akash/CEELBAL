#  Write a program to display all prime numbers within a range
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # Prime numbers are greater than 1
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
