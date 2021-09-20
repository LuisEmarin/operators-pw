# #Python Prework 1-5

# #Question 1
# #Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
# def hello_name(user_name):
#     print("hello_"+ (user_name).upper() + "!")

# hello_name('Luis')

# #Question 2
# for number in range(0, 101):
#     if number % 2 != 0:
#         print(number)

# Question 3
# def max_num_in_list(a_list1):
#    max = a_list1[0]
#    for x in a_list1:
#       if x > max :
#          max = x
#    return max
# a_list1 = [1, 2, 3, 4, 6]
# print(max_num_in_list(a_list1)) 

# # Question 4 
# def is_leap_year(a_year):  
#   if((a_year % 400 == 0) or  
#      (a_year % 100 != 0) and
#      (a_year % 4 == 0)):   
#     print("Year is a leap Year");   
#   else:
#     print ("Year is not a leap Year")  
#     a_year= input("number")
# is_leap_year(1700) 

# Question 5
def is_consecutive(a_list):
    return (a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [1, 2, 4, 5]
print(is_consecutive(a_list))