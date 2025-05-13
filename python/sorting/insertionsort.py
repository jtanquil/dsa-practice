from random import randint, seed

def insertion_sort(arr):
  """Performs in-place insertion sort of arr."""
  sorted_length = 0
  
  """
  Maintain the sorted array as a prefix of the original array.

  Each iteration, add the next element to the prefix and splice it into the 
  prefix at the right spot.
  """
  for i in range(len(arr)):
    sorted_length += 1
    
    for j in range(sorted_length):
      if (arr[j] <= arr[i]):
        continue
      else:
        temp = arr[i]

        for k in range(sorted_length - 1, j, -1):
          arr[k] = arr[k - 1]

        arr[j] = temp

if __name__ == "__main__":
  seed(3413)
  test = [randint(0, 100) for i in range(20)]

  print(test, len(test))

  insertion_sort(test)

  print(test, len(test))