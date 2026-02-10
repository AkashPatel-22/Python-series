# largest number among a b c

def largestnum(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
    
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

print("largest Number is: ", largestnum(num1,num2,num3))