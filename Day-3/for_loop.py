# for varaiable in sequnence
#   block of code

# example - print 1 to 5

# for i in range(15):
#     print(i)

# in --> to check th presence of item in the sequence
# example
word = "priemee"

# for ch in word: # looping over str to print charachters of prime
#     print(ch) 
    
# if 'i' in word: # to check i exits in word or not
#     print("letter exits")

count = 0
for ch in word:
    if ch == 'e':
        count += 1
print(f"i occurs {count} times.")        
    