# # # #section 1.6 
# # # #ex.1
# # # # import dictionaries

# # # print("Welcome to Python", "Welcome to Computer Science", "Programming is fun.", sep="\n")


# # # #ex.2 
# # # print("Welcome to Python" * 5)

# # # # import turtle
# # # # turtle.write("Hello world!")
# # # # turtle.done()
# # # #ex3*: 
# # # def pattern_F():
# # #     return (
# # #         'FFFFFF   ',
# # #         'F        ',
# # #         'FFFFFF   ',
# # #         'F        ',
# # #         'F        '
# # #     )

# # # def pattern_U():
# # #     return (
# # #         'U      U',
# # #         'U      U',
# # #         'U      U',
# # #         ' U    U',
# # #         '  UUU '
# # #     )
# # # def pattern_N():
# # #     return (
# # #         'NN     NN',
# # #         'NNN    NN',
# # #         'NN N   NN',
# # #         ' NN  N  NN',
# # #         '  NN    NNN'
# # #     )
# # # for str in pattern_F():
# # #     print(str)
# # # print()
# # # for str in pattern_U():
# # #     print(str)
# # # print()
# # # for str in pattern_N():
# # #     print(str)
# # # print()
# # # patterns = zip(pattern_F(), pattern_U(), pattern_N())
# # # for row in patterns:
# # #     print(row)

# # # # Display on a single line with space between each character
# # # # for row in patterns:3
# # # #     print(' '.join(row))
# # # #for f,u,n in strpattern_F() , pattern_U(), pattern_N()):
# # #   #  print(f,u,n)

# # # # for row in patterns:
# # # #   print(' '.join(row))
    
# # # #ex.4
# # # # print("a", "a^2", "a^3")

# # # # for a in range(1,5):
# # # #     sqr_row = a ** 2
# # # #     cube_row = a ** 3 
# # # #     print(a , sqr_row , cube_row)

# # # #ex. 5 
# # # # print( (9.5*4.5 - 2.5*3) / (45.5 - 3.5) )

# # # # #ex.6
# # # # def sum(n):  
# # # #     return n*(n+1) // 2
# # # # print(sum(9))

# # # #ex.7
# # # # def num1(a):
# # # #     return -1 / ((2 ** a ) - 1)
# # # # def num2(a):  
# # # #     return 1 / (( 2 ** a) + 1)
# # # # print(res = (num1(a) + num2(a))) * 4

# # # #ex.8 
# # # # import math 
# # # # def area(r):
# # # #     return r * r * math.pi
# # # # def perimeter(r):
# # # #     return 2 * math.pi * r



# # # def sum_of_digits(number):
# # #     if number < 10:
# # #         return number 
# # #     else:
# # #         last = number % 10 
# # #         all_before_last  = number // 10 
# # #     return sum_of_digits(all_before_last) + last
# # # call = int(input("Enter a number between 0 and 1000: "))
# # # print(sum_of_digits(call))







# # number = input("Enter number between 0 too 1000: ")
# # sum = eval(number[0]) + eval(number[1]) + eval(number[2])

# # # # sum = number % 10 + number // 10
# # print(sum)




# # n = int(input("1 to 1000"))
# # sum = n % 10 



# # purpose: app year  and  day consuming minutes: type int
# # find hour, day remain , year
# # find year by take total day // 365
# # remain day: remain of total day divide by 365




# total_min = eval(input("Enter the number of minutes " )) # take input from the user 1 billions
# hour = total_min // 60  # compute hour by divide 60 
# total_days = hour // 24   
# years = total_days// 365 
# days_re = total_days % 365 # find day less by finding remainder of totoal day
# print(f"1000000000 minutes is approximately {years} years and {days_re} days")

#chapter 3 
# import random
# number1= random.randint(0 , 9)
# number2= random.randint(0 , 9)

# answer = eval(input("What is " + str(number1) + " + "  + str(number2) + "?" ))
# print(number1, "+", number2, "=" , answer, "is" , number1 + number2 == answer )

# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!
# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# user_range = input("Enter a range of letters (e.g., a-z): ")
# start, end = user_range.split("-")
# if start.islower():
#   alphabet = "abcdefghijklmnopqrstuvwxyz"
#   print(alphabet[alphabet.index(start):alphabet.index(end)+1])
# elif start.isupper():
#   alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#   print(alphabet[alphabet.index(start):alphabet.index(end)+1])


# import string
# user_range = input("Enter a range of letters (e.g., a-z): ")
# letters = list(string.ascii_uppercase)+list(string.ascii_lowercase)
# s, e = user_range.split('-')
# print(''.join(letters[letters.index(s):letters.index(e)+1]))






# user_range = input("Enter a range of letters (e.g., a-z): ")
# alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# start , end = user_range.split("-")
# result_string = alphabet[alphabet.index(start) : alphabet.index(end) + 1]
# print(result_string)





