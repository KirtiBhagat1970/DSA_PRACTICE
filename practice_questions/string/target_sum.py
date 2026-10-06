nums=[10,20,30,5,4,6,9]
target=34
sum=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(nums[i],nums[j])