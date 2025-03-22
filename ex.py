#This function checks if the numbers in a list are even or odd using a for loop and an if statement.
def kpk(numbers):
    for number in numbers:
       if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
numbers_list = [1, 2, 3, 4, 5, 6]
kpk(numbers_list)
