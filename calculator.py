number_1 = int(input("insert your 1st number: \n"))

number_2 = int(input("now instert 2nd Number: \n"))

solution = 0

operator = input("Which operator to apply?\n"
                "+ for Addition \n"
                "- for Substraction\n"
                "/ for Devision\n"
                "* for Multiplication \n")


def Calculater_logic(num1,num2,opr):
    if operator == "+":
        return number_1 + number_2
        
    elif operator == "-":
        return number_1 - number_2
    
    elif operator == "*":
        return number_1 * number_2
        
    elif operator == "/":
        if number_2 == 0:
            return "Error: Division by zero is not allowed."
        return number_1 / number_2
    else:
        return "Invalid operator\n" \
        "insert valid operator [+-/*] only"
        
    
solution = Calculater_logic(number_1, number_2, operator)
print(f"Your Answer is: {solution}")