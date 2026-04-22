try:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print("Choose the operation: \nPRESS + FOR ADDITION\nPRESS - FOR SUBTRACTION\nPRESS * FOR MULTIPLICATION\nPRESS / FOR DIVISION")
    o=input("Enter the operator:")
    match o:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            if b==0:
                print("Cant divide ERROR:(b=0)!")
            else:
                print(a/b)
        case _:
            print("Entered wrong operator.")
except ValueError:
    print("Please Enter Correct Values!")
