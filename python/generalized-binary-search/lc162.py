# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is
# always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, 
# or index number 5 where the peak element is 6.

# Input: nums = [1, 2, 3, 4]
# Output: 3
# Explanation: 4 is the peak element, at index 3 (elements in the array > elements out of the array)

# note that the condition that nums[-1] = nums[n] = -infinity means that every array has a peak.
# note that for any index, there are four scenarios:
# - arr[index] is a peak: we can just return index here
# - arr[index] is part of a descending sequence: 
# (arr[index - 1] >= arr[index] >= arr[index + 1]): in this case, a peak has to be to the left
# - arr[index] is part of an ascending sequence:
# (arr[index - 1] <= arr[index] <= arr[index + 1]): in this case, a peak has to be the right
# - arr[index] is a local minima:
# (arr[index - 1] >= arr[index] and arr[index] <= arr[index + 1])
# in this case, a peak has to be on either side, pick one

def find_peak(nums):
  def is_peak(nums, index):
    if (index == 0):
      if (len(nums) == 1):
        return True
      else:
        return nums[index] > nums[index + 1]
    elif (index == len(nums) - 1):
      return nums[index] > nums[index - 1]
    else:
      return nums[index] > nums[index - 1] and nums[index] > nums[index + 1]
    
  def is_ascending(nums, index):
    if (index == 0):
      return nums[index] < nums[index + 1]
    elif (index == len(nums) - 1):
      return False
    else:
      return nums[index - 1] <= nums[index] <= nums[index + 1]

  def is_descending(nums, index):
    if (index == 0):
      return False
    elif (index == len(nums) - 1):
      return nums[index - 1] >= nums[index]
    else:
      return nums[index - 1] >= nums[index] >= nums[index + 1]

  left, right = 0, len(nums) - 1
  
  while (left < right):
    mid = left + (right - left) // 2

    if (is_peak(nums, mid)):
      return mid
    elif (is_ascending(nums, mid)):
      left = mid + 1
    elif (is_descending(nums, mid)):
      right = mid

  return right

if __name__ == "__main__":
  nums1 = [1, 2, 3, 1]
  nums2 = [1, 2, 1, 3, 5, 6, 4]
  nums3 = [1, 2, 3, 4]
  nums4 = [4, 3, 2, 1]

  print(find_peak(nums1)) # 2
  print(find_peak(nums2)) # 2 or 5
  print(find_peak(nums3)) # 3
  print(find_peak(nums4)) # 0