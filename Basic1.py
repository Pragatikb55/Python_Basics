dummy = "Hello world!"
print(dummy)
print(type(dummy))

num = 3
another_num = 3.0
print(type(num))
print(type(another_num))

val = True
print(type(val))

print(num)
print(another_num)
print(val)

test = 'banana\'s products are beautiful' 
print(test)
test = "Apple's products are beautiful" 
print(test)
text = "Hello World"
print(len(text))
text = "Hello Planet"
print(text[0])
print(text[4])

text = "Welcome to Python!"
print(text[2:5])
print(text[:2])
print(text[2:])

text = "Welcome to Python!"
print(type(text))
print(type(text[2:4]))

text = "heLLo worLD!"
print(text.upper())
print(text.lower())
print(text.title())

text = 'hello world'
print(text.count('l'))
print(text.count('rl'))
print(text.find('o'))
print(text.find('Z'))
print(text)            
print(text.count('H'))  
print(text.find('H'))

text = 'This is a beautiful world'
print(text.find('beautiful'))
print(text.count('beautiful'))   
print(text.count('is'))
print(text.replace('world', 'planet'))
print(text)
new_text = text.replace('world','planet')
print(new_text)
print(text)

fruit = 'applllllleeeeeee'
print(fruit.replace('e','E'))
print(fruit.replace('z','E'))

msg = '   Hello World    '
print(msg)
print(msg.strip())

print(msg.count(' '))
print(msg.strip().count(' '))

address = '102, Baker St, London'
print(address.split(','))

test = 'how are you doing'
print(test.split(' ')) 

output = test.split(' ')
print(output)
print(type(output))

first = 'Bill'
last = 'Musk'
name = first + last
print(name)
name = first + ' ' + last
print(name)
name = first + '    ' + last
print(name)
name = '{}{}'.format(first, last)
print(name)
name = '{} {}'.format(first, last)
print(name)
name = '  {}     {}  '.format(first, last)
print(name)
name = '  {}     {}  '.format(last, first)
print(name)
name = f'{first}{last}'
print(name)
name = f'{first} {last}'
print(name)
name = f'{first}    {last}'
print(name)
name = f'{first.upper()} {last.lower()}'
print(name)

num1 = 3
num2 = 5
print(num1, num2)
print(type(num1), type(num2))
res = num1 + num2
print(res)
print(num1-num2)
print(num1*num2)
print(num2 / num1)   # division sometimes may result in float
print(num2 // num1)  # this is called floor division i.e. the output is quotient without reminder
print(num2 % num1)  # this is called modulus i.e. the reminder after division
print(type(num2/num1))

new1 = 2.1
new2 = 0.3
print(new1 + new2)
print(new1 - new2)

fir = 3
sec = 0.1
print (fir + sec)

name = input('enter your name')   
print(name)
print(type(name))

text = input('Enter some text    ->')   
print(text.upper())
print(text.title())
print(text.find('e'))
print(text.count('e'))
print(text.replace('e','z'))
print(len(text))