import random

count = 0
score = 0
total = 3

while count<total:
  a = random.randint(0,100)
  b = random.randint(0,100)
  ans = int(input("what is "+str(a)+"+"+str(b)+"? "))

  if ans == a+b:
    print("correct")
    score+=1
  else:
    print("incorrect")
  
  count+=1
  
print("you got", score, "/", total)