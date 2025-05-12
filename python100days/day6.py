import random
from shlex import join

num1 =[1,2,3,4,5,6]
num2 =[num ** 3 for num in num1]
print(num2) 
num3 = [num  for num in num1 if num > 3]
print(num3)
charlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

students = [''.join(random.choices(charlist, k=3)) for _ in range(30)]
print(students)


