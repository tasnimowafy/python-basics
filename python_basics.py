#Create a Boolean variable named x

x = True

#Create an integer variable named y

y = 15

#Create a float variable named z

z = 1.5

#Create a string variable names s

s = 'hello world!!!'

#Convert the int variable to float

a = 5
b = float (a)

#Can we convert the str to int ?

#YES by using the built in function int()

#Create a list of numbers from 1 to 5

lst = [1,2,3,4,5]

#Create a tuple from 10 to 15

tup = (10,11,12,13,14,15)

#Convert the list to tuple

tup2 = tuple(lst)

#Create a dict of 3 values

dic = { "fruit": "apple",
  "color": "red",
  "price": 12,}

#Can we use semi colon ; with python

#YES

#Python is interpreted or compiled ?

#interpreted 

#What is the differences between low level & high level

#high level :easy to understand,programmer friendly
#low level :Machines can understand it,They are not very easy to understand

#What is the differences between = , ==

# == : comparison operator
# = : assignment operator

#What do we mean by using !=

#if two operands not equal then it's true

#What is the operator precedence

#PEMDAS

#Create a variable x with value of 10

X = 10

#Increase x value by 15 using assignment operators

X += 15

#Divide the x value by 5 using assignment operators

X /= 5

#Multiply the x value by 10 using assignment operator

X *= 10

#Get module of x on 3 using assignment operators

X %= 3

#Using python print the module of 11 to 4

mod = 11%4
print(mod)

#Print the exponent of 2,3

expo = 2**3
print(expo)

#Divide 11 by 3 using python division

div = 11/3

#Can we divide 11 by 3 and get an integer number ?

div2 = int(div)

#Check if 10 is bigger than 15 or not

com = 10 > 15

#If 10 is not bigger than15 print x is smaller than 15

if 10 < 15 :
  print("x is smaller than 15")


#In which cases we will use all
  
#Returns true if all of the items are True 

#What is the differences between all , and

#all is for multiple conditions statement
#and is for two conditions statment

#What is the differences between any , or

#any is for multiple conditions statement
#or is for two conditions statment

#If we need all the conditions to be true we will use ….

#all()
  
#What is the differences between if , elif

#if can be used once , checks all conditions 
#elif can be used multiple times ,tests only as many as needed , if it finds one condition that is True it stops and doesn't evaluate the rest 
  
#What is the differences between elif , else

#elif allows you to evaluate multiple statements before closing the loop
#else evaluates a single statement before closing the loop
  
#Can we use more than one elif

#YES
  
#Can we use more than one else

#NO

#write s simple ternary operator
  
print("x is smaller than 15") if 10 < 15 else print("x") 
  
#in elif , python will check all the conditions no matter what ?

#NO

#in elif we use else for ... ?

#for the last condition

#if we have this list [2,4,6,8,10] :
lst2 = [2,4,6,8,10]
# ○ check to see if 4 in this list or not

if 4 in lst2  :
    print('true')
else :
    print('false')

# ○ check to see if 4 and 6 in this list on not

if 4 in lst2 and 6 in lst2:
    
    print('true')
else :
    print('false')

# ○ check to see if 3 or 6 in this list

if 3 in lst2 or 6 in lst2:
    
    print('true')
else :
    print('false')

# ○ check to see if 2 , 4 and 5 in this list


if  all ([2,4,5])in lst2:
    
    print('true')
else :
    print('false')

