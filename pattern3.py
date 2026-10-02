n=int(input("enter a number:"))   
#upper half
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#lower half
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print() 

# upper half
# i=0,1,2,3,4
# j=n-i-1  5-0-1=4 5-1-1=3 5-2-1=2 5-3-1=1 5-4-1=0
# j=2*i+1  2*0+1=1 2*1+1=3 2*2+1=5 2*3+1=7 2*4+1=9
# if j==0 or j==2*i 2*0=0  2*1=2 2*2=4 2*3=6 2*4=8 

# i=0
# j=n-i-i = 5-0-1 =4 4 space print
# j=2*i+1 = 2*0+1 =1  0 to 1 1 is not consider in this only 0 
# so if j==0: print one *

# i=1
# j=n-i-1= 5-1-1=3 3 sapce are print means 0,1,2 
# j=2*i+1 =2*1+1=3 range(0 to 3) means o to 2 : 
#  j=0 print 1 * j=1 false j=2 print  2nd * s