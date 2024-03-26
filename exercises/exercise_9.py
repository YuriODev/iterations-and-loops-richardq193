a = int(input())
b = int(input())
c = int(input())
sentence = ""
for i in range (a, b):
  if i % c == 1:
    continue
  else:
    sentence = sentence + str(i) + " "
print(sentence)