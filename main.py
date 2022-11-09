import random

a = random.randint(0,100)
b = random.randint(0,100)

count = 0
score = 0
total = 10

ans = int(input("what is "+str(a)+"+"+str(b)+"? "))

while count<total:
  
  print("incorrect")
  
  a = random.randint(0,100)
  b = random.randint(0,100)
  ans = int(input("what is "+str(a)+"+"+str(b)+"? "))
  
print("correct")