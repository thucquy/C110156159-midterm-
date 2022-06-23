x = input("請輸入一字元為：")
a = len(x)
i = 0
count = 1
while i <= (a/2):
    if x[i] == x[a-i-1]:
        count = 1
        i = i + 1
    else:
        count = 0
        break
if count == 1:
    print("YES")
else:
    print("NO")