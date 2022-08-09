
class ticket:

 def t1(self):

    print("enter details")
    name=str(input("enter name"))
    age=int(input("enter age"))
    while True:
          p=int(input())
          print("enter location")
          location=str(input("location"))
          while True:
            if p==1:
                print ("enter slot")
                x=int(input())
                while True:
                   if x==1:
                         print("mng")
                         break
                   elif x==2:
                         print("after noon")
                         break
                   elif x==3:
                         print("eve")
                         break
                   elif x==4:
                         print("nyt")
                         break
                   elif x==5:
                         break
                   b = int(input('enter class'))
                   print('chennai exp')
                   while True:

                      if b == 1:
                          print('cost is', y * 155)
                          break
                      elif b == 2:
                          print('no sleeper ')
                          break
                      elif b == 3:
                          break
                      y = int(input('enter seats'))
                      z = int(input('enter class'))
                      print('rajadhani exp')
                      while True:
                          if z == 1:
                              print('cost is',y * 355)
                              break
                          elif z == 2:
                              print('cost is', y * 455)
                              break
                          elif z == 3:
                              print('cost is', y * 555)
                              break
                          elif z == 4:
                              print('cost is', y * 655)
                              break
                          elif z == 5:
                              break






while True:
      print("enter 1 for ticket booking")
      ch=int(input("enter ur choice"))
      if ch==1:
           obj=ticket()
           obj.t1()
           print("successfully booked")
      elif ch==2:
           break
