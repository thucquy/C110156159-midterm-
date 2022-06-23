x = int(input("請輸入第一個要判斷的數字："))
y = int(input("請輸入第二個要判斷的數字："))
a = True
for i in range(2,y):
    if y%2 == 0:
        a = False
if a:
    print("Y")
else:
    print("N")