# Python Operators


#  Arithmetic Operators

print(2+8) #addition

print(8-2) #substraction

print(2*8) #multiplication

print(8/2) #division

print(8%2) #Modulus

print( 13 // 2) #floor division  6.5 but ith rounds the result to the nearest whole number

print(13 // 4)



x = 2 
y = 8


print(x ** y) #//exponential same as 2*2*2


#2   Assignment operators

a=8 #assiging the value 8 to varibale a
print(a)
a+=4 #it means same as a=a+4
print(a)
a-=2 #it means same as a=a-2
print(a)
a*=8 #it means same as a=a*8
print(a)
a/=7 #it means same as a=a/6
print(a)
a%=2 #it means same as a=a%2
print(a)
a**=4 #it means same as a=a**4
print(a)
a//=4 #it means same as a=a//4
print(a)

#  Comparison operators

print(2 == 8) #Equal

print(2 != 8) #Not equal

print (2>8) #greater than

print (2<8)  #less than

print (2>=8) #greater than equal

print (2<=8)  #less than equal

#  Logical operators

x = 2

print(x < 2 and x < 8) #Return True if both the statements are true
print(x < 2 and x > 8)

print(x < 2 or x > 8) #Return True, if anyone of the condition is met

print(x > 4 or x > 10)


print(not(x < 2 and x < 8)) #reverses the result for exa -> if the result is true it will retuen false and vice versa

#5  Identity operators

a=[28,369]
b=[28,369]
c=a
print(a is c) #returns true if both the variables are the same object pointing to a same memory location
print(b is a) ##it will return false because only object is same but the memory location is different here


#Membership Operators

# These operators are used to test if a sequence is present or not in an object

a = [3,6,9,28]

print(6 in a)

print(6 not in a)

# in => it returns true if a sequence is present in an object
# not in => it returns true if a sequence is not present in an object

# BITWISE OPERATORS
# They are used to compare binary numbers

# & => AND => if both bits are 1, it sets each bit to 1 , otherwise 0

# | => OR => if one of the two bits is 1 , it sets each bit to 1 , otherwise 0

# ^ => XOR => if only one of the two bits is 1 , it sets each bit to 1

# ~ => NOT => complement operator, it returns one's complement of the number

# << => Zero fill left shift => the binary number is appended with 0's at the end

# >> => Right SHift => In simple terms, the right side of the bits are removed


x = 28
y = 7

print(x & y)
print(x | y)
print(x ^ y)
print(x % y)
print(x << y)
print(x >> y)
