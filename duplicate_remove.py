num=int(input("enter a number:"))
arr=[]
for i in range(num):
    x=int(input("enter a element:"))
    arr.append(x)

result=[]
for n in arr:
    if n not in result:
        result.append(n)
print(result)


# arr=[1,2,1,3,5,2,1]
# result=list(set(arr))
# print(result)

