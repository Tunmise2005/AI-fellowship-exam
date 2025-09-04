# Question 1: Basic Calculator
# Functions
def add(num1, num2):
    return(num1 + num2)

def Subtract(num1, num2):
    return(num1 - num2)

def multiply(num1, num2):
    return(num1 * num2)

def divide(num1, num2):
    if num2 != 0:
        return(num1 / num2)
print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("Basic Calculator")
print("0. exit")
while True:

    try:
        choice = input("Choose operation (1, 2, 3, 4, 0): ")
        if choice == "0":
            print("Exiting calculator... Goodbye")
            break

        num1 = input("Enter first number: ") 
        num2 = input("Enter second number: ")

        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            print(f"Result: {num1 / num2}")
    except Exception as e:
        print("Error")


# Question 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


# Question 3
while True:
    age = int(input("Enter your age (or type exit to quit): "))
    
    if age == exit:
        print("Goodbye!")
        break
    
    try:
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")