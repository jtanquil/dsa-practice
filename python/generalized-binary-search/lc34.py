# LC 34. Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

# Example 4:

# Input: nums = [5, 7, 7, 8, 8, 10], target = 5
# Output: [0, 0]

# observation: the starting position is the smallest index such that arr[index] = target
# the ending positive is the largest index such that arr[index] = target

# idea: the smallest index and largest index can both be found w/binary search with
# different assumptions on the boundary:
# - to find the smallest index, just execute normal binary search
# - to find the largest index, note that if arr[mid] = target, then we might be
# looking for an index to the right of mid, so we search the right half of target
# this means that if arr[mid] <= target, then set left = mid, and if arr[mid] > target, 
# set right = mid - 1

# algorithm: given nums and target defined above,
# first, find the first/smallest index containing target:
# set left = 0, right = len(nums) - 1
# if left > right, return [-1, -1], there's no search space
# if left >= right, return [-1, -1] if arr[left] != target, otherwise return [left, left]
# set mid = left + (right - left) // 2
# if arr[mid] >= target, search the left half: set right = mid and go again
# if arr[mid] < target, search the right half: set left = mid + 1 and go again
# the final value will be the smallest index s.t arr[index] == target
# if it's -1, then target isn't in the index, return [-1, -1]
# otherwise, find the largest index:
# set left = 0, right = len(nums) - 1
# if left > right, return [-1, -1], there's no search space
# if left >= right, return [-1, -1] if arr[left] != target, otherwise return [left, left]
# set mid = left + (right - left) // 2
# if arr[mid] <= target, search the right half: set left = mid, go again
# if arr[mid] > target, search the left half: set right = mid - 1, go again
# the final value will be the largest index s.t. arr[index] == target

# alternatively, to find the largest: find the smallest index s.t arr[index] > target, then largest will be index - 1
# the splitting condition then is:
# if arr[index] > target, search the left half: set right = index
# if arr[index] <= target: search the right half: set left = index + 1

def first_and_last(nums, target):
  smallest, largest = -1, -1
  left, right = 0, len(nums) - 1

  if (left > right):
    return [smallest, largest]

  while (left < right):
    mid = left + (right - left) // 2

    # in other words: mid satisfies the condition 
    # "smallest possible target is at or to the left of nums[mid]"
    if (nums[mid] >= target):
        right = mid
    elif (nums[mid] < target):
        left = mid + 1

  smallest = left

  if (nums[smallest] != target):
    return [-1, -1]

  left, right = 0, len(nums) - 1

  while (left < right):
    mid = left + (right - left) // 2

    if (nums[mid] <= target):
        left = mid + 1
    # in other words: mid satisfies the condition
    # "largest possible target is to the left of nums[mid]"
    elif (nums[mid] > target):
        right = mid

  largest = right - 1

  return [smallest, largest]

if __name__ == "__main__":
  arr1 = [5, 7, 7, 8, 8, 10]
  arr2 = []

  print(first_and_last(arr1, 8)) # [3, 4]
  print(first_and_last(arr1, 6)) # [-1, -1]
  print(first_and_last(arr1, 5)) # [0, 0]
  print(first_and_last(arr2, 0)) # [-1, -1]