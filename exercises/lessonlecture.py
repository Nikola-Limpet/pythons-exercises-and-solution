# # # fibonaci number 
# # def fibo(n):
# #   # """Compute fibonaci number for 8 values"""
# #   pre,curr = 0, 1
# #   k = 2 
# #   while k < n:
# #     pre, curr= curr, pre + curr
# #     k=+1
# #   return curr
# # result= fibo(8)
# # print(result)


# # from fractions import Fraction
# # f =Fraction(3,4)
# # print(f)

# # creating the dog class
# # class Dog():
# #   """"A simple attempt to model a dog."""
# #   def __init__(self, name, age):
# #     """Initialize name and age attributes"""
# #     self.name = name
# #     self.age = age
# #   def sit(self):
# #     """Simulate a dog sitting in response to command."""
# #     print(self.name.title() + "is now sitting.")
# #   def roll_over(self):
# #     """Simulate rolling over in response to command."""
# #     print(self.name.title()+ "rolled over!")

class Car(object):
  def __init__(self, make, model, year):
    self.make = make 
    self.model = model 
    self.year = year
    self.odometer_reading = 0 # kong tor first start 0. add initial value to odometer attribute

  def get_descriptive_name(self):
    long_name = str(self.year) + " " + self.make + " " + self.model 
    return long_name.title()
  
  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")
  def update_odometer(self , mileage): 
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage 
    else: 
      print("You can't roll back an odometer!")
  def increment_odometer(self, miles):
    self.odometer_reading =+ miles
class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""
  def __init__(self, make, model, year):
      super().__init__(make, model, year)
      self.battery_size = 70
  def describe_battery(self):
    """Print a statement describing the battery size."""
    print("This car has a", str(self.battery_size) + "-Kwh battery.")  
my_tesla  = ElectricCar("tesla", "model s0" , 2027)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
  
# sequence iteration 
# digits = [1, 8 , 2 , 8 ]
# def count(s, value):
#   """Count the number of occurrences of values in sequence s."""
#   total, index = 0
#   while index < len(s): # step over len of s
#     if s[index] == value:
#       total = total + 1  # return true while it bound to 1 ...
#     index = index + 1 
#   return total 
# count(digits , 8)

# to improve this using for statement to simplify this fun body
# def count(s , value):
#   total = 0
#   for elem in s:
#     if elem == value:
#       total += 1 
#   return total


# Lesson: for statement is excuted by the following procedure:

# Syntax: for <name> in <expression>:  evaluate expres.
 #             <suite>       then bind name to that vale in the current frame 
                      #       excute the suite


# sequences unpacking 
# same_count = 0 
# pairs = [[1,2] , [2 ,2] , [2 , 3] , [ 4, 4]]
# for x ,y in pairs:
#   if x == y:
#     same_count  += 1

# OP: 2
# digits = [1, 8 , 2 , 8 ]

# pop(index): Removes and returns the item at the given index from the list.
# insert(index, item): Add the item at the specified position(index) in the list
# append(item): Add item at the end of the list.


from datetime import date
tues = date(2024, 1 , 26)
  


