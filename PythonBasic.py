name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)


num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


for i in range(1, 6):
    print(i)
i = 1
while i <= 5:
    print(i)
    i += 1

def add(a, b):
    return a + b
result = add(10, 20)
print("Sum:", result)

numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.remove(20)
print(numbers)

with open("sample.txt", "w") as f:
    f.write("Hello World!\nThis is a sample file.")
with open("sample.txt", "r") as f:
    print(f.read())
