#count the vowles in a word using forloop

word = input("enter word:")
count = 0
for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1
      
print("vowel count is =",count)  