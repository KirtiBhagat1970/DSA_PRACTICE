# num=int(input("enter a number:"))
# arr=[]
# for i in num:
#     x=int(input("enter element:"))
#     x.append(arr[i])
# print(x)

arr=[12,56,89,45,3,6,9,4]
count_even=0
count_odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count_even+=1
    print(count_even)
    if arr[i]%2!=0:
        count_odd+=1
    print(count_odd)
    
