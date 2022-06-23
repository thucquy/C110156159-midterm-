x = int(input("請輸入一個正整數(<10):"))
num = 1
if x>10:
    print("Incorrect!")
else:
    for r in range (1, x+1):
        for c in range(1, r+1):
            print(num, end=" ")
            num+=1
        print()