n=int(input("enter a number:"))
for i in range(1,n+1):
    print(" "*(n-i)*2,end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()

# n=5
# i=1
# j=" "*(n-i)*2 = (5-1)*2=8
# j= range(1,2) j=1
# j=range(i-1,0,-1) =range(0,0,-1) =0
# =1

# i=2
# j=" "*(n-i)*2 = (5-2)*2=6
# j=range(1,3)= 1 2
# j=range(2-1,0,-1)=1
# =121

# i=3
# j=" "*(n-i)*2 = (5-3)*2=4
# j=range(1,4)= 1 2 3
# j=range(3-1,0,-1)=2  1
# =12321

# i=4
# j=" "*(n-i)*2 = (5-4)*2=2
# j=range(1,5)= 1 2 3 4
# j=range(4-1,0,-1)=3 2  1
# =123421

# i=5
# j=" "*(n-i)*2 = (5-5)*2=0
# j=range(1,6)= 1 2 3 4 5
# j=range(5-1,0,-1)=4 3 2  1
# =123454321


