
x = int(input("請輸入Ｘ座標的位置上："))
y = int(input("請輸入Ｙ座標的位置上："))
if x>0 and y>0:
    print("該點位於第一象限，離原點距離為根號：",(x**2+y**2))
elif x>0 and y<0:
    print("該點位於第四象限，離原點距離為根號：",(x**2+y**2))
elif x<0 and y<0:
    print("該點位於第三象限，離原點距離為根號：",(x**2+y**2))
elif x<0 and y>0:
    print("該點位於第二象限，離原點距離為根號：",(x**2+y**2))
elif x==0 and y==0:
    print("該點位於原點")
elif x==0 and y<0:
    print("該點位於下半平面Ｙ抽上，離原點距離為根號：",(x**2+y**2))
elif x==0 and y>0:
    print("該點位於上半平面Ｙ抽上，離原點距離為根號：",(x**2+y**2))
elif x>0 and y==0:
    print("該點位於右半平面Ｘ抽上，離原點距離為根號：",(x**2+y**2))
elif x<0 and y==0:
    print("該點位於右左半平面Ｘ抽上，離原點距離為根號：",(x**2+y**2))