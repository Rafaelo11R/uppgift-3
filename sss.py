import os
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to calculator")
def devide_nums():
   
    while True:
        num1 = int(input("Type a number"))
        num2 = int(input("Type a number"))

        result = num1 // num2
        print(f"{num1} devided with {num2} is {result}")

        input("Press Enter to continue")
        os.system('cls')
        break

def times_num():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        num1 =  int(input("Add a number:"))
        num2 = int(input("Add a number:"))

        result = num1 * num2
        print(f"The result of {num1} times {num2} is {result}")
        break
    os.system('cls' if os.name == 'nt' else 'clear')




devide_nums()
times_num()














#def devide_nums(number1, number2):

    #result = number1 // number2
   # print(f"{number1} devided with {number2} is {result}")

#number1 = int(input("Type a number"))
#number2 = int(input("Type a number"))


#devide_nums(number1, number2)