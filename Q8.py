a = int(input("請輸入一行正整數為："))
list = input("第二行中數列中的數字為：")
mylist = list.split()
x = 0
for i in mylist:
    if mylist.count(i)>x:
        x = mylist.count(i)
        y=i
print("最大出現次數的數字為：",y)
print("出現次數為：",x)
