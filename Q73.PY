y = input("請輸入時間１（秒）：")
time1 = y * 3600
min1 = y * 60
ans = time1 + min1
print("時間１-",ans)
x = int(input("請輸入時間２（秒）："))
time = x // 3600
x = x % 3600
min = x // 60
x =x % 60
print("時間２",time,":",min,x)