search = int(input("輸入查詢組數 N 為："))
if search == 3:
    print("您的餘款為：",9000)
elif search == 4:
    print("您的餘款為：",5000)
elif search == 5:
    print("您的餘款為：",6000)
elif search == 6:
    print("您的餘款為：",10000)
elif search == 7:
    print("您的餘款為：",12000)
elif search == 8:
    print("您的餘款為：",7000)
else:
    if len(int(search))>2:
        print("Erro!")
