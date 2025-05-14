from random import randint, seed

def quick_sort_recursive(arr, low, high):
  """Recursively quicksort arr[low:high] in-place."""
  if (low >= high):
    return
  else:
    pivot_index = randint(low, high)
    pivot = arr[pivot_index]
    new_low = low
    new_high = high - 1

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    while (new_low <= new_high):
      while (arr[new_low] < pivot):
        new_low += 1

      while (arr[new_high] >= pivot and new_low <= new_high):
        new_high -= 1

      if (new_low < new_high):
        arr[new_low], arr[new_high] = arr[new_high], arr[new_low]

    arr[high], arr[new_low] = arr[new_low], arr[high]

    quick_sort_recursive(arr, low, new_low - 1)
    quick_sort_recursive(arr, new_low + 1, high)

def quick_sort(arr):
  quick_sort_recursive(arr, 0, len(arr) - 1)

if __name__ == "__main__":
  test = [randint(0, 100) for i in range(10)]
  
  print(test, len(test))

  quick_sort(test)

  print(test, len(test))