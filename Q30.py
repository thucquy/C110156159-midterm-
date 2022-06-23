import random
import time
answer = random.sample(range(1,10),4)
print(answer)
a = b = n = 0
num = 0
t = time.time()
while a!=4:
    num += 1
    a = b = n = 0 
    user = list(input())
    for i in user:
        if int(user[n]) == answer[n]:
            a += 1
        else:
            if int(i) in answer:
                b += 1
        n += 1
    output = ','.join(user).replace(',','')
    print(f'{output}:{a}A{b}B')
 