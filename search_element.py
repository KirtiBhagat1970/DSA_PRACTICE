num=int(input("enter a number:"))
arr=[]
for i in range(num):
    x=int(input("enter a element:"))
    arr.append(x)
print(arr)

n=int(input("enter a number to search:"))
for i in range(len(arr)):
    if n==arr[i]:
        
        print("Element found")
        print("position",i)
        