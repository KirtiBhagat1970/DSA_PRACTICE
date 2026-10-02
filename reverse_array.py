num=int(input("enter a number:"))
arr=[]
for i in range(num):
    x=int(input("enter a element:"))
    arr.append(x)
print(arr)   
result=[]
for i in range(len(arr)-1,-1,-1):
    result.append(arr[i])
print(result)
    
# reverse=arr[::-1]
# print(reverse)

# nums=[10,20,33,56,89,12,46]
# left=0
# right=len(nums)-1
# while left < right:
#     nums[left],nums[right]=nums[right],nums[left]
#     left+=1
#     right-=1
# print(nums)