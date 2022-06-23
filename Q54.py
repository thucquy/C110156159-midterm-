x = float(input("請輸入路程公里數："))
if x<=1.5:
    print("所需車資為：",75)
else:
    km = x - 1.5
    kmm = 5*km/0.25
    cost = kmm+75 
    print("所需車資為：",cost)