from random import randint, seed

def merge(arr1, arr2):
  sorted = []

  while (len(arr1) > 0 and len(arr2) > 0):
    if (arr1[0] < arr2[0]):
      sorted.append(arr1.pop(0))
    else:
      sorted.append(arr2.pop(0))

  if (len(arr1) == 0):
    sorted += arr2
  else:
    sorted += arr1

  return sorted

def merge_sort(arr):
  if (len(arr) <= 1):
    return arr
  else:
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

if __name__ == "__main__":
  test = [randint(0, 100) for i in range(50)]

  print(test)

  sorted = merge_sort(test)

  print(sorted)