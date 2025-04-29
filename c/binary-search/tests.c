#include <stdio.h>
#include <assert.h>
#include "binarysearch.h"

static int arr1[] = {};
static int arr2[] = { 1, 3, 4, 5, 7 };
static int arr3[] = { 2, 5, 6, 9, 10, 12 };

void it_test_empty_array() {
  assert(iterative_binary_search(arr1, 3, len(arr1)) == -1);
}

void it_test_right_element() {
  assert(iterative_binary_search(arr2, 7, len(arr2)) == 4);
}

void it_test_mid_element() {
  assert(iterative_binary_search(arr2, 4, len(arr2)) == 2);
}

void it_test_left_element() {
  assert(iterative_binary_search(arr2, 1, len(arr2)) == 0);
}

void it_test_left_side_element() {
  assert(iterative_binary_search(arr2, 3, len(arr2)) == 1);
}

void it_test_right_side_not_found() {
  assert(iterative_binary_search(arr2, 6, len(arr2)) == -1);
}

void it_test_mid_left_element_not_found() {
  assert(iterative_binary_search(arr3, 8, len(arr3)) == -1);
}

void it_test_mid_right_element() {
  assert(iterative_binary_search(arr3, 9, len(arr3)) == 3);
}

void it_test_left_side_not_found() {
  assert(iterative_binary_search(arr3, -1, len(arr3)) == -1);
}

void rec_test_empty_array() {
  assert(recursive_binary_search(arr1, 3, 0, len(arr1) - 1) == -1);
}

void rec_test_right_element() {
  assert(recursive_binary_search(arr2, 7, 0, len(arr2) - 1) == 4);
}

void rec_test_mid_element() {
  assert(recursive_binary_search(arr2, 4, 0, len(arr2) - 1) == 2);
}

void rec_test_left_element() {
  assert(recursive_binary_search(arr2, 1, 0, len(arr2) - 1) == 0);
}

void rec_test_left_side_element() {
  assert(recursive_binary_search(arr2, 3, 0, len(arr2) - 1) == 1);
}

void rec_test_right_side_not_found() {
  assert(recursive_binary_search(arr2, 6, 0, len(arr2) - 1) == -1);
}

void rec_test_mid_left_element_not_found() {
  assert(recursive_binary_search(arr3, 8, 0, len(arr3) - 1) == -1);
}

void rec_test_mid_right_element() {
  assert(recursive_binary_search(arr3, 9, 0, len(arr3) - 1) == 3);
}

void rec_test_left_side_not_found() {
  assert(recursive_binary_search(arr3, -1, 0, len(arr3) - 1) == -1);
}

void runalltests() {
  it_test_empty_array();
  it_test_right_element();
  it_test_mid_element();
  it_test_left_element();
  it_test_left_side_element();
  it_test_right_side_not_found();
  it_test_mid_left_element_not_found();
  it_test_mid_right_element();
  it_test_left_side_not_found();

  rec_test_empty_array();
  rec_test_right_element();
  rec_test_mid_element();
  rec_test_left_element();
  rec_test_left_side_element();
  rec_test_right_side_not_found();
  rec_test_mid_left_element_not_found();
  rec_test_mid_right_element();
  rec_test_left_side_not_found();

  printf("all tests passed\n");
}