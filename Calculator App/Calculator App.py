# CALULATOR APP 
running = True

while running:
    num1 = int(input("Enter first number : "))
    operator = input("Enter Operator : + , - , / , * : ")

    if operator == '+' or operator == '-' or operator == '*' or operator == '/' :

        num2 = int(input("Enter second number : "))
        verify = True

        if operator == '+':
            val = num1 + num2
        elif operator == '-' :
            val = num1 - num2 
        elif operator == '*' :
            val = num1 * num2
        elif operator == '/':
            val = num1 / num2
        else:
            print("Enter Valid Operator !")
            verify = False
        
        if verify is True:
            print(f"{num1} {operator} {num2} = {val}")   


            repeat = input("Do You Want To Exit Press YES / NO : ")
        
            if repeat == 'yes' or repeat == 'YES' or repeat == 'Yes':
                running = False
            else :
                running = True
    
    else:
        print("Enter Valid Operator !!!!!!") 