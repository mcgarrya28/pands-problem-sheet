# Python Collatz
# Author: Anthony Mc Garry

number = int(input("Enter a positive integer: ")) 
print(number)  

while number != 1:
    if number % 2 == 0:  # if the value is even
        number = number // 2  # divide by 2
    else:  # if the value is odd
        number = number * 3 + 1  # multiply by 3 and add 1
    print(number)  # print the updated value

print("The program has ended.")  # print a message indicating the program has ended