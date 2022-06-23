
list = input("請輸入一字元為：")
def checklist(list):
    for i in list:
        if list.count(i)>1:
            return True
        return False
result = checklist(list)
if result:
    print("True")
else:
    print("False")

