try:
    number = int(input("Enter a Number: "))
    result = 100 / number
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input. Please enter a number.")
