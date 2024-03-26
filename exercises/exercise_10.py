def pounds_to_kilograms(n):
  for i in range(1, n+1):
      kilograms = i * 0.453592
      print(f"{i} {kilograms:.2f}")
n = int(input())
pounds_to_kilograms(n)