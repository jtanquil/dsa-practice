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
def counting_sort(arr, digit, radix = RADIX):
  counts = [0] * radix

  for i in range(len(arr)):
    counts[get_digit(arr[i], digit, radix)] += 1
  
  running_total = 0

  for j in range(len(counts)):
    running_total, counts[j] = running_total + counts[j], running_total

  sorted = [None] * len(arr)

  for i in range(len(arr)):
    val_digit = get_digit(arr[i], digit, radix)
    sorted[counts[val_digit]] = arr[i]
    counts[val_digit] += 1
  
  for i in range(len(arr)):
    arr[i] = sorted[i]

def lsd_radix_sort(arr, max_val = MAX_INT, radix = RADIX):
  digits = count_digits(radix, max_val)

  for digit in range(digits):
    counting_sort(arr, digit)

# def msd_radix_sort(arr, max_val = MAX_INT, radix = RADIX):
#   digits = count_digits(radix, max_val)

#   for digit in range(digits - 1, -1, -1):
#     print(digit)
#     counting_sort(arr, digit)

if __name__ == "__main__":
  min_test = [randint(0, MAX_INT) for i in range(20)]
  max_test = min_test[:]
  test_copy = min_test[:]
  test_copy.sort()

  print(min_test)
  lsd_radix_sort(min_test)
  print(f'sorted: {min_test}')
  print(min_test == test_copy)

  # print(max_test)
  # msd_radix_sort(max_test)
  # print(max_test)
  # print(test_copy)
  # print(max_test == test_copy)