# Print Every element of an array
# arr = [10, 20, 30, 40, 50]
# for num in arr:
#     print(num)


# Reverse an array
# arr = [10, 20, 30, 40, 50]
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
#     print(arr)



# Sum of an array
# arr = [10, 20, 30, 40, 50]
# sum=0
# for num in arr:
#     sum+=num
# print(sum)



# Largest element of an array
# arr = [10, 20, 30, 40, 50]
# largest=arr[0]
# for num in arr:
#     if num>largest:
#         largest=num
# print(largest)        



# Count even numbers
# arr = [12, 7, 4, 9, 18, 21]
# count=0
# for num in arr:
#     if num%2==0:
#         count+=1
# print(count)




# Smallest element of an array
# arr = [8, 3, 12, 1, 7]
# smallest=arr[0]
# for num in arr:
#     if num<smallest:
#         smallest=num
# print(smallest)




# Second Largest Element
# arr = [10, 25, 7, 18, 30]
# largest=arr[0]
# second_largest=0
# for num in arr:
#     if num>largest:
#         largest,second_largest=num,largest
# print(second_largest)



# Find element
# arr = [5, 9, 2, 7, 1]
# target = 7
# is_found=True
# for num in arr:
#     if num==target:
#         is_found=True
#         break
#     else:
#         is_found=False
# if is_found==True:
#     print("Found")
# else:
#     print("Not Found")





# Count Elements greater than 20
# arr = [15, 22, 35, 10, 28, 5]
# count=0
# for num in arr:
#     if num>20:
#         count+=1
# print(count)



# Find Largest and smallest in single traversal
# arr = [12, 5, 30, 8, 17]
# smallest=arr[0]
# largest=arr[0]
# for num in arr:
#     if num>largest:
#         largest=num
#     elif num<smallest:
#         smallest=num
# print(largest,smallest)