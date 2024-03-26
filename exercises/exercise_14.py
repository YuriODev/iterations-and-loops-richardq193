# Your solution to Exercise 14
total = 0
n = int(input())
integer = 0
for i in range (n):
  integer = int(input())
  if integer == 0:
    total = total + 1
print(total)