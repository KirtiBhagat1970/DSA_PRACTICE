num=int(input("enter a number:"))
arr=[]
for i in range(num):
    x=int(input("enter a element:"))
    arr.append(x)

print(arr)
result=[]
for num in arr:
    if num != 0:
        result.append(num)
for num in arr:
    if num == 0:
        result.append(num)
    
print(result)

