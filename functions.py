no1 = int(input("Enter the first number: "))
no2 = int(input("Enter the second number: "))

def sum(no1, no2):
    return no1 + no2

def sub(no1, no2):
    return no1 - no2

def mul(no1, no2):
    return no1 * no2

def div(no1, no2):
    return no1 / no2

print(f"{no1}+{no2}={sum(no1, no2)}")
print(f"{no1}-{no2}={sub(no1, no2)}")
print(f"{no1}x{no2}={mul(no1, no2)}")
print(f"{no1}/{no2}={div(no1, no2)}")
