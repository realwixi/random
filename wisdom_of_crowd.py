#wisdom of crowd
from statistics import mean
#getting input from users
list=[]
r=int(input("number of sample==>"))
print("elementsV")
for i in range(r+1):
    y=int(input())
    list.append(y)
#printing list before execution
print(list)
#sorting list
list.sort()
#calculating for terminating the value (according to concept of wisdom of crowd)
tv=int(r*0.1)
#terminating the lowest value
list=list[tv:]
#terminating the highest value
list=list[:r-tv]
#printing the mean i.e the end value
print(mean(list))

    


