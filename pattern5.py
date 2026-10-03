rows=5
columns=5
for i in range(rows):
    for j in range(columns):
        if (i+j)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

# rows=5
# columns=5
# i=0
# j=0
# if (0+0)%2==0 print 1
# if (0+1)%2!=0 print 0
# (0+2)%2==0 print 1
# (0+3)%2!=0 print 0
# (0+4)%2==0 print 1
# 10101

# i=1
# j=0
# if (1+0)%2!=0 print 0
# if (1+1)%2==0 print 1
# (1+2)%2!=0 print 0
# (1+3)%2==0 print 1
# (1+4)%2!=0 print 0
# 01010

