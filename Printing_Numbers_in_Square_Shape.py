'''
Python Pattern Program - Printing Numbers in Square Shape
'''

num = int(input("enter the number of rows: "))
n_list = [[0 for x in range(num)] for y in range(num)]

n=1
low = 0
high = num - 1 
count= int((num+1)/2)
for i in range(count):
    for j in range(low,high+1):
        n_list[i][j]=n
        n+= 1
    for j in range(low+1,high+1):
        n_list[j][high]=n
        n+= 1
    for j in range(high-1,low-1,-1):
        n_list[high][j]=n
        n+= 1
    for j in range(high-1,low,-1):
        n_list[j][low]=n
        n+= 1
    low+=1
    high-=1
for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="\t")
    print()
