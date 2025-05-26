from random import randint, seed

RADIX = 10 # set 10 to easily verify correctness
MAX_INT = 2 ** 31 - 1

def count_digits(radix = RADIX, max_val = MAX_INT):
  digits = 0

  while (max_val > 0):
    max_val = max_val // radix
    digits += 1

  return digits

# to get the ith digit:
# divide by radix ^ (digit - 1) and truncate
# the least sig. digit can be obtain by taking mod (radix)
def get_digit(val, digit, radix = RADIX):
  return (val // radix ** digit) % radix

# sorts starting from least significant digit, then moving to the left
# for each digit, do a counting sort on that digit
def counting_sort(arr, digit, radix, start, stop):
  counts = [0] * radix

  for i in range(start, stop):
    counts[get_digit(arr[i], digit, radix)] += 1
  
  running_total = 0

  for j in range(len(counts)):
    running_total, counts[j] = running_total + counts[j], running_total

  # offset the scan by start
  for j in range(len(counts)):
    counts[j] += start

  sorted = [None] * (stop - start)
  for i in range(start, stop):
    val_digit = get_digit(arr[i], digit, radix)
    sorted[counts[val_digit] - start] = arr[i]
    counts[val_digit] += 1
  
  for i in range(stop - start):
    arr[start + i] = sorted[i]

  return counts

# sort by each digit, starting from the least significant digit going left
# works because this is a lexicographic sort
def lsd_radix_sort(arr, max_val = MAX_INT, radix = RADIX):
  digits = count_digits(radix, max_val)

  for digit in range(digits):
    counting_sort(arr, digit, radix, 0, len(arr))

# sort by each digit, starting from the most significant digit going right
# sort by most significant digit, use the array returned by counting sort to
# partition the input, recursively sort each partition by the next most significant digit
def msd_radix_sort_recursive(arr, digit, radix, start, stop):
  if (digit < 0 or start >= stop - 1):
    pass
  else:
    partitions = counting_sort(arr, digit, radix, start, stop)

    # partitions are start....partitions[0], partitions[0]...partitions[1], ... 
    # partitions[k - 2] ... partiitons[radix - 1] = stop
    # insert start to make indexing consistent
    partitions.insert(0, start)

    for k in range(radix):
      msd_radix_sort_recursive(arr, digit - 1, radix, partitions[k], partitions[k + 1])

def msd_radix_sort(arr, max_val = MAX_INT, radix = RADIX):
  digits = count_digits(radix, max_val)

  msd_radix_sort_recursive(arr, digits - 1, radix, 0, len(arr))

if __name__ == "__main__":
  min_test = [randint(0, MAX_INT) for i in range(20)]
  max_test = min_test[:]
  test_copy = min_test[:]
  test_copy.sort()

  print(min_test)
  lsd_radix_sort(min_test)
  print(f'lsd sorted: {min_test}')
  print(min_test == test_copy)

  print(max_test)
  msd_radix_sort(max_test)
  print(f'msd sorted: {max_test}')
  print(max_test == test_copy)