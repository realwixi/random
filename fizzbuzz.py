def fizzbuzz(r):
    li=[]
    for i in range(1,r+1):
        a=i
        li.append(a)
    print(li)
    for i in range(len(li)):
        if (li[i]%3==0 and li[i]%5==0):
            print(li[i],"=izzbuzz")
        else:
            if (li[i]%3==0):
                print(li[i],"=fizz")
            else:
                if (li[i]%5==0):
                    print(li[i],"=buzz")
                else:
                    print(li[i])
