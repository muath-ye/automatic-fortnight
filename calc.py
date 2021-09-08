# مدخلات
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
numberOp = str(input("Enter operation number: "))

# عمليات
if (numberOp == '+'):
    result = number1 + number2
elif (numberOp == '-'):
    result = number1 - number2
elif (numberOp == '*'):
    result = number1 * number2
elif (numberOp == '/'):
    result = number1 / number2
else:
    result = "You don\'t provide valid\\ operation."

# مخرجات
print(int(result))