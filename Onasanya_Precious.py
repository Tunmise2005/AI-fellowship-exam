# # Question 1: Basic Calculator
# # Functions
# def add(num1, num2):
#     return(num1 + num2)

# def Subtract(num1, num2):
#     return(num1 - num2)

# def multiply(num1, num2):
#     return(num1 * num2)

# def divide(num1, num2):
#     if num2 != 0:
#         return(num1 / num2)
#     else:
#         print("cannot divide by zero!")

# print("Basic Calculator")
# while True:

#     try:
#         choice = input("Choose operation (+, -, *, /) or 'exit to quit: ")
#         if choice == "+":
#             num1 = input("Enter first number: ")
#             num2 = input("Enter second number: ")
#             print(f"Result: {num1 + num2}")
#         elif choice == "-":
#             print(f"Result: {num1 - num2}")
#         elif choice == "*":
#             print(f"Result: {num1 * num2}")
#         elif choice == "/":
#             print(f"Result: {num1 / num2}")
#         elif choice == "exit":
#             print(f"Exiting calculator... Goodbye!")
#             break
#         else:
#             break
#     except Exception as e:
#         print("Error")

# # Question 2
# while True:
#     user_input = input("Enter a number (or type 'exit' to quit): ")
#     if user_input == "exit"__
#         print("Goodbye!")
#         break        # break out of loop
    
#     num = __________(user_input)   # convert to integer
    
#     if num % 2 == 0:
#         print("The number is ______")
#     else:
#         print("The number is ______")


# Question 3
while True:

    age = int(input("Enter your age (or type exit to quit): "))
    try:
        if age >= 18:
            print("You can vote")
        elif age == exit:
            print("Goodbye!")
            break
        else:
            print("You cannot vote")
    except Exception as e:
        print("Invalid input")