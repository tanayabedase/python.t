# pythonlist
mylist = (28, 11)
print(mylist)
mylist = [3, 6, 9, 'blue', 'green']
print(mylist[2])
print(mylist[3])
print(mylist[1])
print(mylist[4])
print(len(mylist))

# acces list items
mylist = [11, 77, True, False, 'maya', 'max']
print(mylist[-3])
print(mylist[4])
print(mylist[5])
print(mylist[2:6])
print(mylist[1:3])

# change add remove list items
mylist = [15, 30, 45, 60, 75]
mylist[4] = 90
print(mylist)

# change a range addcof items on a list
mylist[1:2] = [150, 300]
print(mylist)
mylist[2:4] = [150, 300]
print(mylist)

# extend
mylist1 = [15, 30, 45, 60]
mylist2 = [75, 90, 105, 120]
mylist.extend(mylist)
print(mylist1)
print(mylist2)

# remove list items
mylist = ["fearless", "habit", "defenseless"]
mylist.remove("habit")
print(mylist)
mylist.remove("defenseless")

# remove an item by specifyinng its index
# pop()
mylist = ["away", "from", "home", "festival"]
mylist.pop(1)
print(mylist)
# del()
mylist = ["away", "from", "home", "festival"]
del mylist[0]
print(mylist)
# empty list
mylist.clear()
print(mylist)