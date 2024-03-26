n = int(input())
sentence = ""
for i in range (1,n+1):
  if i%2 == 1:
    continue
  else:
    sentence = sentence + str(i) + " "
print(sentence)