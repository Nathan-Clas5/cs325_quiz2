def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print("Welcome to the basic calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")

choice = input("Enter choice (1/2): ")

if choice == '1':
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
elif choice == '2':
    print(f"The difference between {num1} and {num2} is {subtract(num1, num2)}")
else:
    print("Invalid choice.")
