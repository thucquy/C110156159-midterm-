chine = int(input("國文"))
eng = int(input("英文"))
cal= int(input("微積分"))
pd = int(input("體育"))
com = int(input("程式設計"))
list = [chine,eng,cal,pd,com]
print(max(list))
print(min(list))
if 0< chine and eng and cal and pd and com <=100:
    avg = (chine + eng + cal + pd + com)/5
    print("評分程式",avg,"分")
