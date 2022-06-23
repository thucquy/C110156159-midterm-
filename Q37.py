
n = int(input("整數"))
while 0 < n < 1000000:
    print(n)
    if n == 1:
        break
    elif n % 2 == 1:
        n = 3 * n + 1
        print(n)
    else:
        n = n / 2
        print(n)
