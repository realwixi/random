#wisdom of crowd
from statistics import mean
li=[]
r=int(input("number of sample==>"))
print("elementsV")
for i in range(r+1):
    y=int(input())
    li.append(y)
print(li)
li.sort()
tv=int(r*0.1)
li=li[tv:]
li=li[:r-tv]
print(mean(li))

    


