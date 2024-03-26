n = int(input())
sum = 0
for i in range (100,999):
  if n%3 != 0:
    continue
  else:
    sun = sum + i 
print(sum)