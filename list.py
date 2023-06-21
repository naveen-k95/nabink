# my_list= [1,3,5,7,9]
# print(my_list[1])
# my_list[2]=10
# print(my_list)

# my_list.append(12)
# print(my_list)
# my_list.remove(my_list[2])
# print(my_list)
# print(my_list[2:6])
# sliced_list=my_list[2:6]
# combined_list = my_list + sliced_list
# print(combined_list)
# print(8 in my_list)
# my_list.sort(reverse=True)
# print(my_list)

# my_list = (1,2,3,4,5)
# my_list[0]=99
# print(my_list)

my_tuple = (99,1,2,3,4,5)
# my_tuple[0]=(99,1,22,3,4,5)
# print(my_tuple+my_tuple)

# print(len my_tuple)
# count_1 = my_tuple.count(1)
# # new_tuple = sorted(my_tuple)
# print(my_tuple)
# new_tuple = sorted(my_tuple,reverse=True)
# print(type(new_tuple))
# print(type(tuple(new_tuple)))
# Define a tuple named my_tuple with the following elements: 10,
# 20, 'a', 'b', True.
# 2. Write the code to access and print the third element of the tuple
# my_tuple.
# 3. Concatenate two tuples: tuple1 with elements (1, 2, 3) and tuple2
# with elements ('x', 'y', 'z'). Store the result in a new tuple called
# concatenated_tuple.
# 4. Write a Python code snippet to repeat the tuple my_tuple three
# times and store the result in a new tuple named repeated_tuple.
# 5. Determine the length of the tuple concatenated_tuple using a
# built-in function and print the result.
# 6. Perform slicing on the tuple my_tuple to extract a new tuple with
# elements 'a', 'b', and True. Store the result in a variable called
# sliced_tuple.

# my_tuple = (10,20,'a','b',True)
# # print(my_tuple[2])
# # tuple_1 = (1,2,3)
# # tuple_2 = ('x','y','z')
# # new_tuple = tuple_1+tuple_2
# # print(new_tuple*3)
# # print(len(new_tuple))
# print(my_tuple[2:5])


# my_dist = {
#     "name":"rishabd",
#     "age":21,
#     "address":{
#         "home": "hetauda",
#         "zip":44800,
#         "zip1":4500
#     }
# }
# my_dist = {"college":"kmc"}
# my_dist["college"]="kmc"
# print(my_dist.get("age"))
# print(my_dist["zip1"])
# del my_dist["age"]
# new_age = my_dist.pop("age")

# write a program to show mutliplication table of first 20 prime numbers using nested for loop.

# def check_prime(a):
#     for i in range(2,int(a/2)+1):
#         if a%i==0:
#              return False
#     return True
# if check_prime(3):
#      print("prime")
# else:
#      [print("not prime")]


# def is_prime(number):
#     if number < 2:
#          return False
#     for i in range(2,int(number**0.5) +1):
#         if number%i==0:
#              return False
#     return True



# count=0
# number=1
# prime_list=[]
# while count<20:
#      if is_prime(number):
#           prime_list.append(number)
#           count = count+1
#      number = number+1

# print(prime_list)

# list=[]
# for j in range(1,100):
#      prime=True
#      for i in range(2,j):
#           if j%i==0:
#                prime=False
#                break
#      if prime==True:
#           list.append(j)
# print(list)

# print(len(list))

# wap to find simple interest
# wap to find perimeter of rectangular ground
# wap to find volume of irregular body
# wap to calculate volume of a cube
# wap to find square root of a number
# wap to find error percentage

# Principal= int(input("principal"))
# Rate= int(input("rate"))
# Time= int(input("time in years"))

# interest= (Principal*Rate*Time)/100
# print(interest)

# L= int(input("length"))
# B= int(input("breadth"))
# perimeter= (2*L)+(2*B)
# print(perimeter)

# L= int(input("length"))
# B= int(input("breadth"))
# H = int(input("height"))
# volume = L*B*H
# print(volume)

# L= int(input("lenght of cube: "))
# vol=L*L*L
# print(vol)


# num= int(input("enter number; "))
# SR=num**(1/2)
# print(SR)


# measured = 100
# actual= 80
# error= measured-actual
# print(error)
# EP= error/actual*100
# print(EP)

# print(error value)


# take a string from user and check wheather the string is rishab karki or not?

# string = input("enter string : ")
# substring = input("enter substring to check in string : ")

# if substring in string:
#     print("yes substring is present!!")

# else:
#     print("substring is absent!!..")


# wap to find area of a circle wirh radius 7.5,8.97, 20.39,100,129,139,600,1000,5.6,8.9,12.711.2,12.13

# radius =[7.5, 8.97, 20.39, 100, 129, 139, 600, 1000, 5.6, 8.9,12.7,11.2,12.13]
# pie = 3.14
# for i in range(len(radius)):
#     print(f" The area of the circle with radius{radius[i]} is {pie*radius[i]**2}")

# from copy import deepcopy
# list_a = [1,2,3,4]
# # list_b = list_a
# list_b= deepcopy(list_a)
# list_b[0]= "ram"
# print("list_b",list_b)
# print("list_a",list_a)


# enumerate function

# fruits = ["apple", "mango","orange"]
# for index, value in enumerate(fruits):
#     print(index+1,value)
# print(fruits[0])



# se = (1,2,3,4,5,6,7,8,9)
# print(se)

# list, tuple, dictonary set

# list = [1,2,3,4,5,6,7,8,9]
# print(list)
# print(set(list))



# a= [[1,2,3],[4,5,6],[7,8,9]]
# # print(a)
# for i in range (0,3):
#    for j in range(0,3):
#       a[i][j]=1+a[i][j]
# print(a)

#  square of list
# list = [2,3,4,5,6]
# a= (x**2 for x in list)
# # print(a)
# a=[]

# for x in list:
#     a.append(x**2)
# print(a)

# number=1000
# if number < 0:
#     print("number is negative")
# elif number == 0:
#     print("number is zero")
# elif number % 2 ==0:
#      print("number is even")
# else:
#     print("number is odd")











