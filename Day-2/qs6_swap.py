#program to swap the values of two numbers entered by user

a = int(input("enter number a:"))
b = int(input("enter number b :"))

temp = a
a = b
b = temp

print("after swapping:")
print(a)
print(b)
