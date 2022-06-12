from sys import path
path.append('../')
from classes.CStack import Stack

print("Hello World!")

s=Stack()

print(s.isEmpty())
s.push("Maria")
print(s.pop())


