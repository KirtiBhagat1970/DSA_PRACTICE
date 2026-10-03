n=int(input("enter a number:"))
mid=n//2
for i in range(n):
    for j in range(n):
        if i==mid or j==mid:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# dryrun
# n=5
# mid=5//2=2
# i=0 1 2 3 4 5
# j=0 1 2 3 4 5
# if i==2 or j==2 print *
# else print space

