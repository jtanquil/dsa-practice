from random import randint, seed

def quick_sort(arr, low = None, high = None):
  """Perform in-place quicksort on arr."""
  low = -1 if low is None else low
  high = len(arr) - 1 if high is None else high
  pivot_index = randint(low + 1, high)
  pivot = arr[pivot_index]

  arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

  while (low < high):
    while (True):
      low += 1

      if (arr[low] > pivot):
        break

    while (True):
      high -= 1

      if (arr[high] <= pivot):
        break
    
    arr[low], arr[high] = arr[high], arr[low]

  arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
  quick_sort(arr, 0, low)
  quick_sort(arr, high, len(arr))

if __name__ == "__main__":
  seed(3413)
  test = [randint(0, 100) for i in range(20)]

  print(test, len(test))

  quick_sort(test)

  print(test, len(test))