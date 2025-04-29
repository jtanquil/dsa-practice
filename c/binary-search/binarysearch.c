#include <stdio.h>

int iterative_binary_search(int *arr, int element, int len) {
  int left = 0;
  int right = len - 1;

  while (left <= right) {
    if (left == right) {
      return (arr[left] == element) ? left : -1;
    }

    int mid = left + (right - left) / 2;

    if (arr[mid] == element) {
      return mid;
    } else if (arr[mid] < element) {
      left = mid + 1;
    } else if (arr[mid] > element) {
      right = mid;
    }
  }

  return -1;
}

int recursive_binary_search(int *arr, int element, int left, int right) {
  if (left > right) {
    return -1;
  } else if (left == right) {
    return (arr[left] == element) ? left : -1;
  } else {
    int mid = left + (right - left) / 2;

    if (arr[mid] == element) {
      return mid;
    } else if (arr[mid] < element) {
      return recursive_binary_search(arr, element, mid + 1, right);
    } else if (arr[mid] > element) {
      return recursive_binary_search(arr, element, left, mid);
    }
  }

  return -1;
}