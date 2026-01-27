def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

    print("Welcome to the basic calculator!")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum_result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}")

    diff_result = subtract(num1, num2)
    print(f"The difference between {num1} and {num2} is {diff_result}")