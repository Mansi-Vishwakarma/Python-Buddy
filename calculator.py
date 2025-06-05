print("A for add")
print("B for substraction")
print("C for multiplication")
print("D for division")
user_input=input()
if(user_input=="A"):
  a=int(input("enter a num"))
  b=int(input("enter a numb"))
  c=(a+b)
  print(c)
if(user_input=="B"):
  a=int(input("enter a num"))
  b=int(input("enter a numb"))
  d=(a-b)
  print(d)
if(user_input=="C"):
   a=int(input("enter a num"))
   b=int(input("enter a numb"))
   e=(a*b)
   print(e)
if(user_input=="D"):
    a=int(input("enter a num"))
    b=int(input("enter a numb"))
    if( a==0 or b==0):
      print("the number cannot be calculated")
    else:
     f=(a/b)
     print(f)