# Calculate the cube of all numbers from 1 to a given number
number = int(input("Enter a number: "))

print("Cubes of numbers from 1 to", number, ":")

for num in range(1, number + 1):
    cube = num ** 3
    print(cube)
