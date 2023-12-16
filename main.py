try:
    number_1 = float(input("Enter a number 1: "))
    number_2 = float(input("Enter a number 2: "))
    number_3 = float(input("Enter a number 3: "))

    print("Sum: ", number_1 + number_2 + number_3)
    print("Multiplication: ", number_1 * number_2 * number_3)

except Exception as e:
    print(e)