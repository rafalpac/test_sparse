def divider(a, b):
    return a / b

try:
    print(divider(1,2))

except ZeroDivisionError:
    print("Can't divide by zero")