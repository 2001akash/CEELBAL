# Find the sum of the series upto n terms
def series_sum(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i

    return sum

number = int(input("Enter the number of terms: "))
result = series_sum(number)

print("Sum of the series up to", number, "terms:", result)
