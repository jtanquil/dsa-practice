from random import randint, seed

# given an array arr and target
# set start = 0, end = len(arr) - 1
#
# let mid be the middle index of the array: start + (end - start) // 2
# if arr[mid] is the target, return mid
# while start < end (while there's anything left to search)
# otherwise two cases:
#   if arr[mid] < target, search the right half of the array: set start = mid + 1
#   if arr[mid] >= target, search the left half of the array: set end = mid
# check mid = start + (end - start) // 2 again
#
# if start >= end, nothing left to search:
#   if arr[start] == target, return start
#   otherwise, return - 1
# [1, 5, 6, 7, 8, 8, 9, 15, 15, 19]
# ex/target = 7
# start = 0, end = 9, mid = 4, arr[mid] = 8
# left half: start = 0, end = 4, mid = 1, arr[mid] = 5
# right half: start = 1, end = 4, mid = 2, arr[mid] = 6
# right half: start = 2, end = 4, mid = 3, arr[mid] = 7, return 3
def binary_search_iteration(arr, target):
  start, end = 0, len(arr) - 1
  mid = start + (end - start) // 2

  while start < end:
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      start = mid + 1
    elif arr[mid] >= target:
      end = mid

    mid = start + (end - start) // 2

  if arr[mid] == target:
    return mid
  else:
    return -1

def binary_search_recursion(arr, target):
  def _binary_search_recursion(start, end, arr, target):
    if start > end:
      return -1
    elif start == end:
      return start if arr[start] == target else -1
    else:
      mid = start + (end - start) // 2

      if arr[mid] == target:
        return mid
      elif arr[mid] < target:
        return _binary_search_recursion(mid + 1, end, arr, target)
      elif arr[mid] >= target:
        return _binary_search_recursion(start, mid, arr, target)

  return _binary_search_recursion(0, len(arr) - 1, arr, target)

if __name__ == "__main__":
  seed(3413)
  test = []

  for i in range(10):
    test.append(randint(0, 20))

  test.sort()

  print(test) # [1, 5, 6, 7, 8, 8, 9, 15, 15, 19]
  test_targets = [randint(-20, 20) for i in range(20)]

  for ele in test_targets:
    print(f'{ele} : {binary_search_iteration(test, ele)} (iteration)')
    print(f'{ele} : {binary_search_recursion(test, ele)} (recursion)')