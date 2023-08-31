# lst = [3, 2, 4]
# lst.sort()
# print(lst)

def sort(nums):
    temp: int = 0
    for i in range(0, len(nums), 1):
        for j in range(0, i):
            if nums[i] < nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp


nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)
