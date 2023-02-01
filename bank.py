# Python Bank Account
#vAuthor: Anthony Mc Garry

# User enter the amount of exact cents they are lodging
cent_1 = int(input("Please enter the 1st amount in cents: "))
cent_2 = int(input("Please enter the 2nd amount in cents: "))

# Add the two amounts together
total =  int(cent_1 + cent_2)/100

#Print the total of the two amounts
print(f' The total amount lodged today is €{total}')