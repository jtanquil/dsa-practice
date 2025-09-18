# LC 33. There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown
# pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and
# become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return
# the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# If the array is rotated by some pivot index k, then when splitting the array
# down the middle there are two cases:
# - the pivot is at mid
# - the pivot is to the left or right of mid
# => in the first case, both the left and right halves are already sorted
# => in the second, one half will be sorted, the other will be sorted with a pivot
# in either case, we can just recursively search each half and return left half | right half
# (note that this works since the array elements are distinct)
# since we're cutting the array in half each iteration this will be O(2 log n/2) = O(log n)

def rotated_binary_search(nums, target):
  val = recursive_rotated_binary_search(nums, target, 0, len(nums) - 1)

  return -1 if val is False else val

def recursive_rotated_binary_search(nums, target, left, right):
  if (left > right):
    return False
  elif (left == right):
    return left if nums[left] == target else False
  else:
    mid = left + (right - left) // 2

    if nums[mid] == target:
      return mid
    else:
      return recursive_rotated_binary_search(nums, target, left, mid - 1) or recursive_rotated_binary_search(nums, target, mid + 1, right)

if __name__ == "__main__":
  nums1 = [4, 5, 6, 7, 0, 1, 2]
  nums2 = [1]

  print(rotated_binary_search(nums1, 0)) # 4
  print(rotated_binary_search(nums1, 3)) # -1
  print(rotated_binary_search(nums2, 0)) # -1