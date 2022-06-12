from os import path as ospath
from sys import path
path.append(ospath.dirname(ospath.dirname(ospath.realpath(__file__))))
from classes.CStack import Stack

print("Hello World!")

s=Stack()

print(s.isEmpty())
s.push("Maria")
print(s.pop())


