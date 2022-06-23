x = int(input("請輸入一正整數："))
i = x
while True:
    if i%x==0:
        break
    else:
        i+=1
print(i,"為新公倍數? Yes")
