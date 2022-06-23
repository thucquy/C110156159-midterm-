x = int(input("請輸入一個度數："))
if x < 120:
    print("Summer months:",x*2.10)
    print("Non-Summer months",x*2.10)
elif 121<=x<=330:
    print("Summer months:",x*3.02)
    print("Non-summer months",x*2.68)
elif 331<=x<=500:
    print("Summer months:",x*4.39)
    print("Non-summer months:",x*3.61)
elif 501<=x<=700:
    print("Summer months:",x*4.97)
    print("Non-summer months:",x*4.01)
elif x>=701:
    print("Summer months:",x*5.63)
    print("Non-summer months:",x*4.50)