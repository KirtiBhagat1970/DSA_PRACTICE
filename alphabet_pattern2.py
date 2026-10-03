n=int(input("enter a number:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")

    print()

# dryrun
#  n=5
# i=1 first row
# j=1 2  2 cannot be run because end value means range upto
# so print only A on frist line

# i=2 second row
# j=1 2 3 
# so print  A  B on second line


# i=3 third row
# j=1 2 3 4
# so print  A  B C  on third line

# i=4 fourth row
# j=1 2 3 4 5 
# so print  A  B C D  on fourth line

# i=5
# False


