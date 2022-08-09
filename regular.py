import re
txt="Use of python in Machine Learning"
x=re.search("^Use.*Learning$",txt)
if (x):
    print("YES! We have a match!")
else:
    print("NO match")