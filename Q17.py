
x = [[[],[]],[[],[]]]
for i in range(2):
    print("Enter matrix %d:" %(i+1))
    for j in range(2):
        for k in range(2):
            print("[%d, %d]: " %(j+1,k+1),end='')
            x[i][j].append(eval(input()))

for i in range(2):
    print("Matrix %d:" %(i+1))
    for j in range(2):
        for k in range(2):
            print("%d" %x[i][j][k], end='')
        print()

print("The sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        print("%d" %(x[0][i][j] + x[1][i][j]), end='')
    print()