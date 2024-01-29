# 1. Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

# Answer 

# a = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\n\tHow I wonder what you are"
# print(a)

# Ex3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
# import datetime
# datetime_now = datetime.datetime.now()
# print("Current date and time :")
# print(datetime_now.strftime("%Y %m %D, %h:%M:%S"))



# EX4.Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# Solution:
# import math

# from cmath import pi


# def i(r):
#   area = pi * r * r
#   return area
# r= float(input("Enter raduis:"))
# area=i(r)
# print("Area of raduis=", r, "is", area)

# Ex5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them
#  Solution
# a = input("Enter your first name:")
# b = input("your last name:")
# print(b+" "+a)
 
#Ex6.Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# print("List :", "['3', ' 5', ' 7', ' 23']")
# print("Tuple :", "('3', ' 5', ' 7', ' 23')")
# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
# values = input("Input some comma-separated numbers: ")

# Split the 'values' string into a list using commas as separators and store it in the 'list' variable
# list = values.split(",")

# Convert the 'list' into a tuple and store it in the 'tuple' variable
# tuple = tuple(list)

# Print the list
# print('List : ', list)

# Print the tuple
# print('Tuple : ', tuple)



#  Lecuture lesson on nested function
# def g(x):
#   def h():
#     x ="abc"
#   x=x+1
#   print("g:x=",x)
#   h()
#   return x
# x=3
# z=g(x)


# Ex7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java



# Ex8.  Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# solution
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[3])



# Ex9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
# solution 
# exam_st_date = (11, 12, 2014)
# The '%i' placeholders are filled with the values from the 'exam_st_date' tuple
# print("The examination will start from: %i / %i / %i" %exam_st_date)

# Ex10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
# solution
# n = int(5)

# print(n+(n,n)+(n,n,n))

# def main():
#    print_square(3)
  
# def print_square(size):
#    for _ in range(size): # mean ney tha vea 3 jour mok 
#     print("#" * size) # men ney tha vea print jenh 3 times

# main()


# def main():
#   print_square(3)

# def print_square(size):

#   # for each row in square
#   for i in range(size):

#     # for each brick in row

#     for j in range(size):

#       # print brick 
#       print("#", end="")
#     print() # print a new line
# main()




# n = input("Now you are in the forest\n\nYou have to find a way to go out the forest\n\n\n##############################################\n##############################################    \n\n\t\t:)  \n\n\n##############################################\n##############################################\n\nDo you love me or not?")
# while n == "No" or n == "no":
#   print("\n\n\n##############################################\n##############################################    \n\n\t\t:)  \n\n\n##############################################\n##############################################")
#   n = input("you are in the forest again :(. Do you love me or not?")
# while n == "Yes" or n =="yes":
#   print("\n\nYou make a right decesion now", "I will help you out :)\n\n\n##############################################\n##############################################    \n\n\t\t :)     (/o,o/)  \n\n\n##############################################\n##############################################")
#   break
 


# To do 
#  Create container to hold values
# Take input from user; fruits
# Get calories for the fruits
# Ignore any values that are not fruit


# Split a string into a list of words based on whitespace characters:
# words = "This is a sentence".split()
# print(words)

# # Split a string into a list of characters:
# characters = "Hello".split()
# print(characters)

# # Split a string into a list of words based on a comma delimiter:
# words = "This,is,a,sentence".split(",")
# print(words)

# # Split a string into a list of words, splitting at most 2 times:
# words = "This is a sentence".split(" ", 2)
# print(words)

# Ex11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

# solution 
# Print the docstring (documentation) of the 'abs' function
# print(abs.__doc__)

# import builtins
# print(builtins.abs.__doc__)

# Ex12. Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.
# Python calendar.month(theyear, themonth, w=0, l=0):

# import calendar
# y = int(input("What the current year is?: "))
# m = int(input("What the current month is?: " ))
# print(calendar.month(y,m))

# Ex13. Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# def digit_sum(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return n+digit_sum(n-1)

# def digital_root(n):

#     if n<10:
#         return n
#     else:
#         return digit_sum(n // 10)
    
# digital_root(120)

# ex.  Write a program to accept two numbers from the user and calculate multiplication 

# a= int(input("Enter first number: "))
# b= int(input("Enter second number: "))

# print(a*b)
# ex print('Name', 'Is', 'James') will display Name**Is**James
# print('Name', 'Is', 'James', sep="**")
# Exercise 3: Convert Decimal number to octal using print() output formatting
# given num = 8
# num = 8 
# print(oct(num)) 0o10

# Exercise 3: Convert Decimal number to octal using print() output formatting
# num = 458.541315
# print('%.2f' % num)

# e.x accept a list of 5 float numbers as an input from a user
# number = []


# for i in range(5):
#   print("Enter the location of your float number is at ", i)
#   items = float(input())

#   number.append(items)
# print(number)

# e.x6 write all contain of a given file into a new file by skipping line 5

# with open('test.txt', 'w') as fp:
#   fp.write("""
# line1
# line2
# line3
# line4
# line6
# line7 """)


# e.x 7  Accept any three string from input() call 
#  write a program to take three names as input from a user in single input() function call

# def call():
#   return input("Name 1:")+ " "+ input("Name 2:")+" "+input("Name 3:")

# print(call())

# str1, str2, str3 = input("enter three string ").split()
# print("Name1: ",str1)
# print("Name2: ",str2)
# print("Name3: ",str3)


#  ex. practise for loop 
# print first 10 natural numbers using while loop 

# n = 1
# while n <= 10:
#   print(n)
#   n+=1
 
# ex2 print the following pattern
# write a program to print the following nummber pattern using a loop.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# row = 5
# for i in range(1,row +1):
#   for j in range(1,i +1 ):    #row j dis play the range of i e.g i=3 will display 1 2 3
#     print(j,end=" ")
  
#   print(" ")

# ex 3. Calculate the sum of all numbers from 1 to a given number 
# write a progrm to accept a number from a user and calculate the sum of all number from 1 to a given number 

# expect output
# Enter a number 10
# Sum is: 55

# n= int(input("enter a number: "))
# for i in range(1,n):
#   # if i < n:
#     n= n + i
# print(n)


# x= int(input("enter a number: "))
# sum_of_num = sum(range(1,x+1))
# print(sum_of_num)



# Ex 5. Display numbers from a list using loop

# write  a program to display only those number from a list that satisfy the folllowing conditional
# the numbers msut be divisible by five
# if the numbers is greater than 150, then skip it and move to the next number
# if the numbers is greater than 500, then stop the loop


# given:

# numbers = [12, 75, 150 ,180, 145, 525, 50] 
# for i in numbers:
  
#   if i > 150:
#     continue
#   elif i > 525:
#     break
#   elif i%5 == 0:
#     print(i)

# Ex.6: Count the total number of digits in a number 
# write a program to count the total number of digits in a number using a while loop 

# for example, the number is 75869, so the output should be 5.


# s = 0 
# number = int(input("Enter number: "))
# while number != 0:
#     number = number//10   #reduce last digit 
#     s += 1
# print(s)


# Ex.7 print the following pattern 
# write a program to use  for loop to print the following reverse number pattern


  # expected output:
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1
# 2 1 
# 1

# row = 5
# max_number= 5
# for i in range(1, row +1) :
#   for j in range (max_number+1 - i, 0, -1):
#     print(j, end=" ")
    
#   print(" ")


# EX.8 Print list in reverse order using a loop 
# given 
# list1 = [10, 20, 30, 40, 50]
# item = reversed(list1)
# for item in list1:
#   print(item)

# list1 = [10, 20, 30, 40, 50]
# size = len(list1) - 1 # because index start from 0 you will get 6-1
# for i in range(size, -1, -1 ):   # index 5 4 3 2 1
#   print(list1[i]) # print slice from 50 to 10 beacause we have declared last indext in loop 
  # what we want is that we want  to use index that start from the end  the first by using for loop run 5times 

# Ex. 9 Display number from -10  to -1 using for loop 
# expected output 
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
# k=11
# for i in range(9,-1,-1):   or (10, 0, -1)
  # k= k -1
  # print(k)

# e.x 10 use else block to display a message "Done" after successful excution of for loop 
# given

# for i in range(5):
#   print(i)
# else:
#   print("Done!")

# ex.11 write a program to dislay all prime number within a range 

# NOTE: A prime number is a number that cannot be made by mulitiplying other whole numbers. A prime number is a natural number greater than 1 that is not product of two smaller natural numbers.

# E.g. 6 is not a prime number beacuase it can be made by 2*3 
# 29 31 34 37 38 41 43 47 

#  Given  range 
# start = 25 
# end = 50 

# for num in range(start, end +1):    # stored pi 25 to 49 + 1 
#   if num > 1: # prime number is greater than 1
#       for i in range(2, num):     # to check whether it is mulplying by 2 to 50 or not
#         if num%i == 0:   #if the remainder equal 0 it means that it is not a prime number
#            break
#       else: 
#            print("Prime number:", num)


# EX. 13 Find the factorial of given number 

#  write a program to use  the loop to find the factorial of a given number.

#  5! = 120

# num = 5
# fact = 1
# if num <= 0:
#  print(" factorial is not a negative number")

# for i in range(1,num+1):
#  fact = fact * i  store first value then take that value to * next values of i 

# print (" factorail of n= 5:", fact)


# EX.15 Use a loop to display elements from  a given list presnets at odd index positions 

# Given 
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Expected output:
# 20 40 60 80 100

# for i in my_list[1::2]:   
#    print(i , end=" ")


# Ex 16. Calculate the cube of all numbers from 1 to a given number 

#expected output

# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216
 

# n = 6 
# for i in range(1, n+1):
#   i = i **3
#   print(i)



# Ex17. Find the sum of the series upto n terms

#  write a program to calculate the sum of series up to n terms.

# if n = 5 the series will become 2 + 22 + 222+ 2222+ 22222 =  24690

# n = 5 

# start = 2
# sum_seq = 0 
# for i in range(0,n):      #iterate 5 times 
#   print(start, end="+")   # first time 2, then second start has changed to 20+2, then thrid changed to 220+2 
#   sum_seq += start        # it calulate the sum of start that has changed and stored it as an abstraction 
#   start = start *10 + 2 
# print("\n")
# print("sum of this series is: ", sum_seq)


# Ex 18, Print the following pattern 
# write a program to print  the following start pattern using for loop 
# ''' expected output 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# '''

# for i in range(0,5):
#   for j in range(0, i+1):
#     print("*" , end=" ")
#   print()

# for i in range(5, 0, -1):
#   for j in range(0, i -1):
#       print("*" , end=" ")
#   print()


# Function ex
# Exercise 1: Create a function in Python
# write a program to create a function that takes two arguments, name and age, and print their value.

# def demo(name, age):
#   print(name, age)
# demo("Nikola", 18)





# Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.


# funcall  with 3 arguments

# fun1(20, 40, 60)
# fun1(80, 100)

# def fun1(*args):    # we use * to accepte any n number 
#   for i in args:
#     print(i)
# fun1(20, 40, 60)
  
# fun1(80, 100)

# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

#given 
# def calu(a, b):
#   #your code
#   plus = a +b
#   minus = a - b
#   return plus, minus

# res = calu(40, 10)
# print(res)

# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name , salary=9000):
#   return name, salary
# both= show_employee("Nikola" , 19000)
# withoutsalary= show_employee("jessi")
# print(both)
# print(withoutsalary)



# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it


# def main(a,b):
#   def calculate(a,b):
#     return a + b 
#   return calculate(a,b) + 5 
# print(main(5,10))


# Exercise 6: Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# A recursive function is a function that calls itself again and again.
# Expected output: 55 

# def sum(num):

#   match num:
#     case 0:
#        return 0 
#     case num:
#       return num + sum(num-1)
    
  # if num:
  #   return num + sum(num - 1)
  # else:
  #   return 0 
# print(sum(10))


# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name

# given 
# def display_student(name, age):
#   print(name, age)

# # display_student("emma", 26)

# # assign a new name to a function;
# show_student = display_student
# show_student("emma", 26)

# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# Expected Output
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


# print(list(range(4,30,2)))

#exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# print(max(x))

# list1 = []
# for i in range(4,30,2):
#     list1.append(i)
# print(list1)


# String exercise
#ex1A. Create a string made of the first, middle and last character 
# write a program to create a new string made of an inputing string's first, middle, and last character.


# Given: str1 = "James"

#expected output: Jms
# str1 = "James"
# res = str1[0] # first character 
# le = len(str1) 
# res = res + str1[le//2] + str1[le-1]
# print(res)

# Ex1B. Create a string made of the middle three characters

# Write a program to create a new string made of the mdidle three characters of an input string.
# given 
# case 1
# str1 = "JhonDipPeta"
# OP: Dip 
# case 2
# str2 = "JaSonAy"
# OP: Son 
# str_input = input("What's ur name?")
# leng = len(str_input)
# middle = leng // 2
# middle_name = str_input [middle-1:middle +2: ]
# print(middle_name) 

#Exercise 2: Append new string in the middle of a given string
#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1
# s1 = "Ault"
# s2 = "Kelly"
# #Op: AuKellylt
# lens1 = len(s1)
# middles1 = lens1//2
# s3 = s1[ :middles1:] + s2 + s1[middles1::]
# print(s3)

#Ex.3 Create a new string made of the first, middle, and last characters of each input string 
#Given two strings s1 and s2, write a program to return a new string made of s1 and s2's first, middle, and last characters 

#Given 
# s1 = "America"
# s2 = "Japan"

# #OP: AJrpan
# l1 = len(s1)
# l2 = len(s2)
# s3 = s1[0] + s2[0] + s1[l1 // 2] + s2[l2 // 2 ::]
# print(s3)

# other way by using function 
# def max_string(s1, s2):
#    first = s1[0] + s2[0]
#    middle = s1[int(len(s1)/2) : int(len(s1)/2) + 1] + s2[int(len(s2)/2) : int(len(s2)/2)+1]
#    last = s1[len(s1) - 1] + s2[len(s2)-1]
#    res = first + middle + last 
#    print("Mix String is ", res)
# s1 = "America"
# s2 = "Japan"
# max_string(s1, s2)

# Ex4. Arrange string characters such that lowercase letters should come first 
# Given string contains a combination of the lower and upper case letter. Write a program to arrange the characters of a string so a string so that all lowercase letters show come first

# given 
# str1 = "PyNaTive"
# #Op: yaivePNT
# lower = []   
# upper = []
# for char in str1:
#   if char.islower():
#     lower.append(char)
#   else:
#     upper.append(char)

# sorted_str = "".join(lower + upper)
# print("Result: ", sorted_str)


# print("Welcone to Dog Age to Human age Conversion APP")
# print("Please provide the following inforamtion")
# print("----------------------------------------")
# print("\n\n")
# a = input("Your name: ")
# b = int(input("Your dog age: "))
# print("Thank for using our APP: " , a)
# print("--------------------------------------------------------------------------")
# print("Your dog age equivalent to human is " + str(int(b * 7 )) + " years old" )
# print("--------------------------------------------------------------------------")



#Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!
# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

# Exercise : Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

# Given:
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
# expected output
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]

# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]


# odd_list=[]
# for index1, element1 in enumerate(l1):
#   if index1 % 2 == 1:
#     odd_list.append(element1)
# print(odd_list)
# even_list=[]
# for index2 , element2 in enumerate(l2):
#   if index2 % 2 == 0 :
#     even_list.append(element2)
# print(even_list)

# print(odd_list + even_list)

# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

# Given:

# list1 = [34, 54, 44, 27, 79, 91, 41]
# Expected Output:

# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]


# sample_list = [34, 54, 67, 89, 11, 43, 94]

# print("Original list ", sample_list)
# element = sample_list.pop(4)
# print("List After removing element at index 4 ", sample_list)

# sample_list.insert(2, element)
# print("List after Adding element at index 2 ", sample_list)

# sample_list.append(element)
# print("List after Adding element at last ", sample_list)


# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# Given:

# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Expected Outcome:

# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]

