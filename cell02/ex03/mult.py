first_n = int(input("Enter the first number: "))
second_n = int(input("Enter the second number: "))

product = first_n*second_n

print(first_n, " x ", second_n, " = ", product)

if product > 0:
    print("The result is positive")
elif product < 0:
    print("The result is negative")
else:
    print("The result is both postive and negative")