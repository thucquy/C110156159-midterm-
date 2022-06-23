from calendar import month

yours = int(input("請輸入日為："))
mon = int(input("請輸入月為："))
if mon==1:
    if yours >=21:
        print("星座為: Aquarious")
    if yours <=20:
        print("星座為: Capricorn")
if mon==2:
    if yours <=18:
        print("星座為: Aquarious")
    if yours >=19:
        print("星座為: Pisces")
if mon==3:
    if yours <=20:
        print("星座為: Pisces")
    if yours >=21:
        print("星座為: Aries")
if mon==4:
    if yours <=20:
        print("星座為: Aries")
    if yours >=21:
        print("星座為: Taurus")
if mon==5:
    if yours <=21:
        print("星座為: Taurus")
    if yours >=22:
        print("星座為: Gemini")
if mon==6:
    if yours <=21:
        print("星座為: Gemini")
    if yours >=22:
        print("星座為: Cancer")
if mon==7:
    if yours <=22:
        print("星座為: Cancer")
    if yours >=23:
        print("星座為: Leo ")
if mon==8:
    if yours <=23:
        print("星座為: Leo")
    if yours >=24:
        print("星座為: Virgo")
if mon==9:
    if yours <=23:
        print("星座為: Virgo")
    if yours >=24:
        print("星座為: Libra")
if mon==10:
    if yours <=23:
        print("星座為: Libra")
    if yours >=24:
        print("星座為: Scorpio")
if mon==11:
    if yours <=22:
        print("星座為: Scorpio")
    if yours >=23:
        print("星座為: Sagittarius")
if mon==12:
    if yours <=21:
        print("星座為: Sagittarius")
    if yours >=22:
        print("星座為: Capricorn")
else:
    if mon >12:
        if yours >=32:
            print("錯誤！請重打一次")


