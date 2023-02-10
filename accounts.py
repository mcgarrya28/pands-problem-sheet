# Python Account
# Author: Anthony Mc Garry

# Task 3 Part 1 - Write a python program called accounts.py that reads in a 10 character /
# account number and outputs the account number with only the last 4 digits showing and the first 6 digits replaced with Xs

# User must enter maximum of 10 digit bank account number.
# A character count > 10 will give an error & ask the user to re-enter the number
# Where the user enters correctly the last 4 digits will be displayed to the user 

while True:
    account_no = input("Enter a 10 account no: ")
    if len(account_no) != 10:
        print("Error: Account no cannot be more than 10 digits.")
    else:
        print("x" * 6 + account_no[6:])
        break



# Task 3 Part 2 - Modify the program to deal with account numbers of any length

# **Assuming the second element of the task is to read in any number
# Then display all but the last character as "x"

# Input account number of any length
# Print all but the last 4 digits as "x"

account_no_1 = input("Enter a number: ")

print("x" * (len(account_no_1) - 4) + account_no_1[-4:])