num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
ch=input("Enter the operation you want to perform (+, -, *, /,**): ")
if ch == "+":
    print("The sum is: ", num1+num2)
elif ch == "-":
    print("The difference is: ", num1-num2)
elif ch == "*":
    print("The product is: ", num1*num2)
elif ch == "/":
    if num2!=0:
        print("The quotient is: ", num1/num2)
    else:
        print("Error: Division by zero is not allowed.")
elif ch == "**":
    print("The result is: ", num1**num2)
else:
    print("Invalid operation")
    