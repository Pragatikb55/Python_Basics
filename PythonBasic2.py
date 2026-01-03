num1 = 3
num2 = 5
print(num1, num2)
print(type(num1), type(num2))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)
print(num2 // num1)  # this is called floor division i.e. the output is quotient without reminder i.e. discarding the numbers after decimal point
print(num2 % num1)   # this is called modulus i.e. the reminder after division
print(3 ** 2)        # exponent (^) ---> 3^2

print(9 // 3)
print(8 // 3)
print(7 // 3)
print(6 // 3)

print(9 % 3)
print(8 % 3)
print(7 % 3)
print(6 % 3)

print(5 * 4 + 1)          
print(1 + 5 * 4)          
print(5 * (4 + 1) )

print(2 == 2)   # if LHS = RHS, output True else False
print(2 == 1)   # Here LHS is not equal to RHS
print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 3)
print(3 >= 2)
print(3 <= 2)

# += is a shortcut for add and assign 
num = 4
print(num)
num += 1   # is equivalent to num = num + 1
print(num) 
# -= is a shortcut for subtract and assign
num = 4
print(num)
num -= 1   # is equivalent to num = num - 1
print(num) 
num = 4
num *= 2    # is equivalent to num = num * 2
print(num)
num = 4
num /= 2    # is equivalent to num = num / 2
print(num)

# Three cases of AND
print(True and True)
print(True and False)   # same as False and True
print(False & False)  

# Three cases of OR
print(True or True)   
print(True or False)
print(False | False)  

# not is opposite of something (bool)
print(not True)
print(not False)

# AND needs both conditions to be True
x = 5
print(x > 4 and x < 6)

# OR evaluates for atleast one true condition
x = 5
print(x > 3 or x < 4)  # if any one condition is true, answer is true

# NOt operater checks for opposite result
x = 5
print(not(x > 3 and x < 10))

# abs() function gives positive number
print(abs(-2))
print(abs(-2.1))

# round() function rounds off the digits after decimal point
print(round(3.45))
print(round(-3.95))

# round() function with precision
print(round(3.46, 1))   # round the number till 1 decimal place
print(round(3.46, 2))   # round the number till 2 decimal place
print(round(3.469, 1))   # round the number till 1 decimal place
print(round(3.469, 2))   # round the number till 2 decimal place

# Just like integer, arithmatic operations can be applied on float
new1 = 2.1
new2 = 0.3
print(new1 + new2)
print(new1 - new2)

# Float and integer can be added to each other
fir = 3  # int
sec = 0.1  # float
print (fir + sec)

# Funnily, if you add string and integer, you'll get a string
num1 = 'Hello'
num2 = '5'
print(num1 + num2)  


a = '2'
b = '3'
print(a, type(a))
print(b, type(b))
print('Addition = ', a+b)   # because this is string + string, the output will be simple concatenation of the digits i.e. output will be 23 instead of 5

print()                     # Leaves a blank space in output
a = int(a)
b = int(b)
print(a, type(a))       # here you'll get output as int
print(b, type(b))       # here you'll get output as int
print('Addition = ', a+b)

# Float to str
num = 2.0
print(type(num))
num = str(num)
print(type(num))

# str to bool
num = 'True'
print(type(num))
num = bool(num)
print(type(num))

# Note, anything that you write in input() is accepted as string, even if it is an integer. Try passing some integer as input and check its datatype.

num = input('enter some integer  -  ')   
print(num)
print(type(num))

# To convert string into integer which is passed in input(), you can simply wrap it up in int() or float() class

num = input('Enter some number --- ')     # pass some number e.g. 2   
print(num, type(num))
new = int(num)            # this is called typecasting (i.e. you are changing data type of variable) (this line will give you error if you pass some text in the input box, try it!)
print(new, type(new))

# Carry addition of two user-inputted numbers
num1 = input('Enter first number:  ')
num2 = input('Enter second number:  ')
print(num1 + num2)    # this will simply append the two numbers one after the other
print(int(num1) + int(num2))   # this will actuall carry out the addition 


x = 4
y = 3
if x > y:             # if is followed by condition which is followed by :    # That's standard syntax
  print('yes, x is indeed greater than y') 

  x = 14
y = 15
if x > y:             # if is followed by condition which is followed by :    # That's standard syntax
  print('yes, x is indeed greater than y') 
print('this statement is not part of if clause, hence there is no indent here')

x = 14
y = 13
if x > y:             # if is followed by condition which is followed by :    # That's standard syntax
  print('yes, x is indeed greater than y') 
  print('I want to be part of if clause as well, so i have given 4 indents before print()') 
print('this statement is not part of if clause, hence there is no indent here')

# else statement lies on the same level as if
if 4 > 5:
    print('four is greater than five')
else:
    print('four is smaller than five')

    # multiple if else => use elif
height = 176
if height < 140:
    print('too short')
elif height < 180:
    print('height is ok')
else:
    print('too tall')

    # You can pass boolean value (True or False) to the condition in if. In that case, you don't need any logical operator like == or !=


is_subscribed = True
if is_subscribed:              # Read it like - if True do THIS else do THAT
    print('Thank you for the subscription!')  
else:
    print('Please subscribe')

is_subscribed = False
if is_subscribed:
    print('Thank you for the subscription!')
else:
    print('Please subscribe')
    
x = 3
y = 4

if x < y and x + y > 5:
    print('both statements are true') 
if x < y or x > y:
    print('one of the statement is true') 
if x < y and not x + y < 5:
    print('both the statements must be true')

    # Nested If
x = 7
if x > 10:
    print('x is greater than 10')
    if x > 20:
        print('x is greater than 20')
        if x > 30:
            print('x is greater than 30')
        else:
            print('x is smaller than 30')
    else:
        print('x is smaller than 20')
else:
    print('x is smaller than 10')

    # To find out if inputted number is within the range of 3 to 10 
# if both conditions are True only then answer will be True else false

x = int(input("Enter any number within range 10: "))     # if you pass anything other than integer, it'll throw error. Because we are typecasting here itself
print(x >= 3 and x <= 10)