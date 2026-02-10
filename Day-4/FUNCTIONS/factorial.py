#factorial of number using function

def facto(n):
    fact = 1
    for i in range(1, n + 1 ):
        fact *= i
        
    return fact
    


# fact = 1

# for i in range (1, n + 1):
#     fact *= i
    
num = int(input("Enter number: "))
print("factorial = ", facto(num))
