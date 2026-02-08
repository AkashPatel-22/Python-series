#Ask the user for:Principal(P),Rate(R),Time(T).
#Convert all to float and compute simple interest:
#SI=(P∗R∗T)/100.

p = int(input("enter principle amount:"))
r = int(input("enter rate:"))
t = int(input("enter time:"))

P = float(p)
R = float(r)
T = float(t)

SI = (P*R*T)/100

print("after conserting to float")
print(P)
print(R)
print(T)

print("SimpleInterest is =",SI)

