#print multiplication table for any number ,using while

n = int(input("Enter Number:"))

i = 1
while i <= 10:
    print(f"{n}*{i} = {n*i}")
    i += 1    
    