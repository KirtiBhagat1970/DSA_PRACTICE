n=int(input("enter a number:"))
ch=64
for i in range(1,n):
    for j in range(i):
        print(chr(ch+i) ,end=" ")
    print()