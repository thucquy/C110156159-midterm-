lap = range(1,11)
ds = []
gt = 1
for i in lap:
    print("請輸入第",i,"個數字:",gt)
    gt=int(input())
    ds.append(gt)
ln = ds[0]
lx = ds[0]
for i in ds:
    if i > ln:
        ln = i
    else:
        i < lx
        lx = i
print("最大的數字",ln)
print("最小的數字",lx)

