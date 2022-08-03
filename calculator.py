num_1 = int(input('Enter first number: '))            # the number that we want to start with
operator = input('Enter your operator: ')             # the operator that we want to use
num_2 = int(input('Enter your second number: '))      # the number we want to finish with
if operator == '+':
    print(num_1 + num_2)
elif operator == '-':
    print(num_1 - num_2)
elif operator == '*':
    print(num_1 * num_2)
else:
    operator == '/'
    print(num_1 / num_2)