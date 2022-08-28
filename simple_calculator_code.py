# This is a simple calculator program.
num1 = input("First Number:\n")
operator = input("Operator (+, -, *, /):\n")
num2 = input("Second Number:\n")

num1 = float(num1)
num2 = float(num2)

output = 0

if operator == "+":
    output =  num1 + num2
elif operator == "-":
    output = num1 - num2
elif operator == "*":
    output = num1 * num2
elif operator == "/":
    output = num1 / num2
    
print("Answer: " + str(output))
