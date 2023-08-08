def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

def rectangle_area(length, width):
    return length * width

while True:
    print("Main Menu:")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Calculate triangle area")
    print("6. Calculate circle area")
    print("7. Calculate rectangle area")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("Exit.")
        break
    elif choice < 1 or choice > 7:
        print("Invalid choice, try again")
        continue

    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = sum(num1, num2)
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = subtract(num1, num2)
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = multiply(num1, num2)
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = divide(num1, num2)
    elif choice == 5:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        result = triangle_area(base, height)
    elif choice == 6:
        radius = float(input("Enter the radius of the circle: "))
        result = circle_area(radius)
    elif choice == 7:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        result = rectangle_area(length, width)
    else:
        result = "Invalid choice"

    print("Result:", result)

