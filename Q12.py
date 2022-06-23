from itertools import count


list = input("請輸入一整列為：")
mylist = list.split()
count = 0
temp = 0
index = 0 
for x in range(0,len(mylist)):
    temp = mylist.count(mylist[x])

    if (temp>count):
        count = temp
        index = x
mostFrequentNumber = mylist[index]
print("過半元素為:", mostFrequentNumber)
