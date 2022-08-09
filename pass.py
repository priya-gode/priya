
class ticket:
    def t1(self):
        s=str(input('source: '))
        d=str(input('destination: '))
        while True:
              x=int(input('enter choice'))
              y = int(input('enter seats'))
              if x == 1:
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
              elif x == 2:
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

              elif x == 3:
                  print('godavari exp')
                  u = input('enter class')
                  while True:

                      if u == 1:
                         print('cost is', y * 150)
                         break
                      elif u == 2:
                         print('no sleeper ')
                         break
              elif x==4 :
                   break

print('welcome to ticket booking centre')
while True:
    print('enter 1 for booking')
    ch=int(input('enter choice'))
    if ch==1:
        obj = ticket()
        obj.t1()
    elif ch==2:
        break