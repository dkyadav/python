number1 = input("enter number1: ");
number2 = input("enter number2: ");
operator = input("choose operator +,-,*,/ :");

result = lambda number1, number2, operator: eval("{} {} {}".format(int(number1), operator, int(number2)))

print(result(number1,number2,operator))

