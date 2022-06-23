from posixpath import split

x = input("請輸入Ａ的好友")
y = input("請輸入Ｂ的好友a")
mylist = len(set(x) & set(y))
print(mylist)
  