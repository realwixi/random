#wisdom of crowd
from statistics import mean
list=[]
r=int(input("number of sample==>"))
print("elementsV")
for i in range(r+1):
    y=int(input())
    list.append(y)
print(list)
list.sort()
tv=int(r*0.1)
list=list[tv:]
list=list[:r-tv]
print(mean(list))

    


