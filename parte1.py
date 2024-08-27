f = open("nombres.txt")
num = 0

for line in f: 
  num +=1 

print(num)
f.close()