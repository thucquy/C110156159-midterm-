
mylist = [int(i)for i in input().split(',')]
mylist.sort()
ans = mylist[0]
while ans!=1:
    for i in range(1,len(mylist)):
        r = mylist[i]%ans
        if r != 0:
            mylist.insert(0,r)
            break
        if ans != mylist[0]:
            ans = mylist[0]
        else:
            break
print(ans)