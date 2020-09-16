print("Select an operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("-----------------")
print("0. Exit")

# ეს ფუნქცია დაგვიბრუნებს ორი რიცხვის განაყოფს
def divide(first_number,second_number):
    return first_number / second_number

# ეს ფუნქცია დაგვიბრუნებს ორი რიცხვის ნამრავლს
def multiply(first_number,second_number):
    return first_number * second_number

# ეს ფუნქცია დაგვიბრუნებს ორი რიცხვის სხვაობას
def subtract(first_number,second_number):
    return first_number - second_number

# ეს ფუნქცია დაგვიბრუნებს ორი რიცხვის ჯამს
def add(first_number,second_number):
    return first_number + second_number


user_choice = ""

while user_choice != '0':
    user_choice = input("Enter choice(1/2/3/4): ")
    if user_choice in ('1', '2', '3', '4'):
        try:
            number_first = int(input("Enter first number: "))
            number_second = int(input("Enter second number: "))
            if user_choice == '1':
                result = add(number_first,number_second)
                print(result)
            elif user_choice == '2':
                result = subtract(number_first,number_second)
                print(result)
            elif user_choice == '3':
                result = multiply(number_first,number_second)
                print(result)
            elif user_choice == '4':
                result = divide(number_first,number_second)
                print(result)
        except:
            print('Invalid input from user')
    elif user_choice == '0':
        # თუ შემოყვანილი მნიშვნელობა არის 0 პროგრამა უნდა გაითიშოს
        print("Bye Bye!\nSee you soon") 
        break
    else:
        # თუ შემოყვანილი მნიშვნელობის ოპერაცია არ არსებობს
        print("Invalid input")