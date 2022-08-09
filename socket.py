d={1:'I',2:'am',3:'priya'}
k={1:'i',2:'am',3:'from',4:'klu'}
print(d,k)
f=k.copy()
print(f)
d[1]='hi'
print(d)
d.clear()
print(d)
k.pop(1)
print(k)
k.popitem()
print(k)
d.update({2:'i am'})
print(d)
print(d.values())
print(k.keys())