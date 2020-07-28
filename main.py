# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# Sorting: Bubble Sort

"""
UPER:
U:
    > 

"""

nums = [5,1,6,3,12,2]

isSorted = False
count = 0

while not isSorted:
    isSorted = True
    for i in range(len(nums)-1):
        print('iteration: ',nums[i])
        if nums[i] > nums[i+1]:
            count += 1
            print('swap1: ', nums[i])
            print('swap2: ', nums[i+1])
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(nums)
            isSorted = False
print(f"Array is sorted in {count} swaps.")
