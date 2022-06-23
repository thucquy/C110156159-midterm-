#Test3
year = int(input("請輸入西年："))
y = year % 100
if y % 12 == 0:
    print("Rat")
elif y % 12 == 1:
    print("Ox")
elif y % 12 == 2:
    print("Tiger")
elif y % 12 == 3:
    print("Rabbit")
elif y % 12 == 4:
    print("Dragon")
elif y % 12 == 5:
    print("Snake")
elif y % 12 == 6:
    print("Horse")
elif y % 12 == 7:
    print("Sheep")
elif y % 12 == 8:
    print("Monkey")
elif y % 12 == 9:
    print("Rooster")
elif y % 12 == 10:
    print("Dog")
elif y % 12 == 11:
    print("Pig")
