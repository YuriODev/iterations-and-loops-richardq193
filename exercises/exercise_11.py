# Write a program to calculate the sum of the expression 1/2 + 2/3 + 3/4 + …​ + n/(n + 1) for a given value of n.
n = int(input())
sum = 0
for i in range (1,n):
  n = float(n)
  sum = sum + i/(i+1) 
sum = sum + n/(n+1)
rounded = round(sum,2)
print(rounded)