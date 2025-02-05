# slicing
from operator import length_hint
from pickletools import pylist
from tkinter import Y


x = "hello legends"
print(x[3:9])

# negative index
print(x[-6:-3])

# modifying the string
x = "you can to it day by day"
print(x.lower())
print(x.upper())

# splited text
x = "cause we made it"
print(x.split())

# replace elements with another one
x = "got ths antidote"
print(x.replace("s", "e"))

x = 'oops'
y = 'hi'
z = x+y
print(z)