n=int(input("enter a number:"))
sp=n
for i in range(1,n):
    for sp in range(0,n):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="")
    sp-=1
    print()
