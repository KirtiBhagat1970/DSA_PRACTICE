
# arr=[10,20,30,40]
# sum=0
# for i in range(len(arr)):
#     sum=sum+arr[i]
# print(sum)



num=int(input("enter a number:"))
arr=[]
for i in range(num):
    x=int(input("enter a element:"))
    arr.append(x)
print(arr) 
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
print(sum)