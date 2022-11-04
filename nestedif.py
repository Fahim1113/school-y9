#nested if
print("Can I have a PS5")

ans1 = input("Have you done your chores?")

if ans1 == "yes":
  ans2 = input("Have you fed your fish?")
  if ans2 == "yes":
    ans3 = input("Have you fed your cat?")
    if ans3 == "yes":
      ans4 = input("Have you fed your snake?")
      if ans4 == "yes":
        ans5 = input("Have you fed your dog?")
        if ans5 == "yes":
          print("You can have a PS5")
        else:
          print("no")
      else:
        print("no")
    else:
      print("no")
  else:
    print("no")
else:
  print("no")