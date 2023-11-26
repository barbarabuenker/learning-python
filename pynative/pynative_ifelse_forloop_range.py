#  PYnative exercises: if else, for loop, and range() exercises

# Exercise 1: Print First 10 natural numbers using while loop:
## define number to iterate over
number = 1
## condition for while loop ("do this while number is smaller than or equals 10")
while number <= 10:
    print(number)
    ## make sure 1 is added after printing the number in each cycle
    number = number + 1

# Exercise 2: Print the following pattern:
rows = 5
for i in range(rows + 1):
    for j in range(i + 1):
        print(j, end = " ")
    print(end= " ")
## doesn't work - go have a look at it again later!

# Exercise 3: Calculate the sum of all numbers from 1 to a given number:
## Solution 1:
### create sum variable to store sum of numbers
sum = 0
### convert user input to integer, iterate over number 1 to number of user input
for number in range(int(input("Enter number"))+1):
    ## add current number to sum
    sum = sum + number
### print sum to screen
print("Sum is:", sum)
### Note: My approach is slightly different then in the solution; however, my output is as expected!

## Solution 2:
### create variable for user input, convert number to integer
number = int(input("Enter number"))
### calculate sum of all numbers from 0 to user input using range function
sum = sum(range(n+1))
### print sum to screen
print("Sum is:", sum)
### Note: My approach is slightly different then in the solution; however, my output is as expected!

# Exercise 4: Write a program to print multiplication table of a given number:
## set given numbe as 2
given_number = 2
## iterate over given number 10 times using the range function
for number in range(1,11):
    ## multiply given number by the current number in each iteration
    product = number * given_number
    ## print the product
    print(product)
## Note: My approach is slightly different then in the solution (they added a third value in the range function - "in steps of 1"); however, my output is as expected!

# Exercise 5: Display numbers from a list using loop:
## define given list of numbers
numbers = [12, 75, 150, 180, 145, 525, 50]
## iterate over every number in list of numbers using a for loop
for number in numbers:
    ## if number is divisibly by 5 and smaller than or equal to 150, print the number
    if number % 5 == 0 and number <= 150:
        print(number)
    ## if the number is greater than 500, stop the loop
    elif number > 500:
        break
### Note: My approach is slightly different then in the solution; however, my output is as expected!

# Exercise 6: Count the total number of digits in a number:
## Solution 1:
### can't think of a solution now - go have a look at it again later!

## Solution 2 (I came up with)
### define given number
given_number = 75869
### print number of digits of given number using the len function, convert it to str to be able to use len function
print(len(str(given_number)))

# Exercise 7: Print the following pattern:

# Exercise 8: Print list in reverse order using a loop:

# Exercise 9: Display numbers from -10 to -1 using for loop:

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop:

# Exercise 11: Write a program to display all prime numbers within a range:

# Exercise 12: Display Fibonacci series up to 10 terms:

# Exercise 13: Find the factorial of a given number:

# Exercise 14: Reverse a given integer number:

# Exercise 15: Use a loop to display elements from a given list present at odd index positions:

# Exercise 16: Calculate the cube of all numbers from 1 to a given number:

# Exercise 17: Find the sum of the series upto n terms:

# Exercise 18: Print the following pattern:
