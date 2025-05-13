from random import randint, seed

def selection_sort(arr):
  """Performs in-place selection sort of arr."""
  sorted_length = 0

  """
  Maintain the sorted array as a prefix of arr.

  For each iteration, find the smallest element still in the unsorted part of the array,
  and append it to the sorted part of the array.
  """
  for i in range(len(arr)):
    min = float("inf")
    min_index = -1

    for k in range(sorted_length, len(arr)):
      if arr[k] < min:
        min = arr[k]
        min_index = k
    
    arr[min_index], arr[sorted_length] = arr[sorted_length], arr[min_index]
    sorted_length += 1

if __name__ == "__main__":
  seed(3413)
  test = [randint(0, 100) for i in range(20)]

  print(test, len(test))

  selection_sort(test)

  print(test, len(test))