from steps.oop_calculator import Calculator

def print_menu():
    print("Select an operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("--------------------")
    print("0. Exit")

user_choice = ""
calculator = Calculator()
while user_choice != '0':
    print_menu()
    user_choice = input("Enter choice(1/2/3/4): ")
    if user_choice in ('1', '2', '3', '4'):
        try:
            number_first = int(input("Enter first number: "))
            number_second = int(input("Enter second number: "))
            if user_choice == '1':
                result = calculator.add(number_first,number_second)
                print(result)
            elif user_choice == '2':
                result = calculator.subtract(number_first,number_second)
                print(result)
            elif user_choice == '3':
                result = calculator.multiply(number_first,number_second)
                print(result)
            elif user_choice == '4':
                result = calculator.divide(number_first,number_second)
                print(result)
        except:
            print('Invalid input from user')
    elif user_choice == '0':
        # თუ შემოყვანილი მნიშვნელობა 0ის ტოლია პროგრამა უნდა გაითიშოს
        print("Bye Bye!\nSee you soon") 
        break
    else:
        # თუ შემოყვანილი მნიშვნელობის ოპერაცია არ არსებობს
        print("Invalid input")