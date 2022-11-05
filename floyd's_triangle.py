n = int(input("Number of rows: "))
k = 0
for i in range(n):
    k+=i
m = n+k
for i in range(n):
    for j in range(i+1):
        print(format(m,"<5"),end=" ")
        m-=1
    print()