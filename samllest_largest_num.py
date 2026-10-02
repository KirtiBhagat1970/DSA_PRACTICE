# arr=[2,9,3,12,19,6,4,3]
# for i in range(len(arr)):
#     arr.sort()
# print(arr)
# print("first smallest number:",arr[0])
# print("second smallest number:",arr[1])
# print("first largest number:",[-1])
# print("second largest  number:",arr[-2])

# arr=[2,9,3,12,19,6,4,3]
# largest=arr[0]
# for i in range(len(arr)):
#     if arr[i] > largest:
#         largest=arr[i]
# print("first largest:",largest)

# arr=[10,5,6,23,89,1,7,45]
# smallest=arr[0]
# for i in range(len(arr)):
#     if arr[i] < smallest:
#         smallest=arr[i]
# print("first smallest:",smallest)



# for i in range(len(arr)):
#     if arr[i] > largest:
#         second_largest=arr[i]
#     if arr[i] < smallest:
#         second_smallest=arr[i]
# second_largest=smallest
# second_smallest=largest


# for i in range(len(arr)):
#     if arr[i]!=smallest and arr[i] < second_smallest:
#         second_smallest=arr[i]
#     if arr[i]!=largest and arr[i] > second_largest:
#         second_largest=arr[i]
# print(second_largest)
# print(second_smallest)



arr=[10,3,45,6,8,23,42,56,30]
max=min=arr[0]
for num in arr:
    if num > max:
        smallmax=max
        max=num
    elif (num > smallmax and num!=max):
        smallmax=num 

    if num < min:
        smallmin=min
        min=num
    elif (num < smallmin and num!=min):
        smallmin=num 
print("minimum:",min)
print("second minimum:",smallmin)
print("maximum:",max)
print("second maximum:",smallmax)
