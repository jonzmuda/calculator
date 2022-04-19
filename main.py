while True:
    value = input("What would you like to do? \n1) Add\n2) Subtract\n3) Divide\n4) Multiply\n")    
    if value == "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        sum =  num1 + num2
        print(f"The sum of {num1} + {num2} = {sum}")
    elif value == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        diffrence =  num1 - num2
        print(f"The diffrence of {num1} - {num2} = {diffrence}")
    elif value == "3":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        quotient =  num1 / num2
        print(f"The diffrence of {num1} / {num2} = {quotient}")
    elif value == "4":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        product =  num1 * num2
        print(f"The diffrence of {num1} x {num2} = {product}")