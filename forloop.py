# basic forloop
for x in range(100, 0, -5):
  print(x)

#nine times table with forloop
for x in range(1, 21):
  print(str(x)+"*9="+str(x*9))

#times table
a = int(input("what timetable "))
b = int(input("upto "))
for x in range(1, b+1):
  print(str(x)+"*"+str(a)+"="+str(x*a))