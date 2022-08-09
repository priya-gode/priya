l1=[1,2]
l2=[2,3]
for i in range (0,len(l1)):
    res=l1[i]*l2[i]
    print(res)
l1[1]=4
print(l1)