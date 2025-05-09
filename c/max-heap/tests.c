#include <stdio.h>
#include "maxheap.h"

void test_initialize() {
  initialize();
  printf("heap initialized\n");
}

void test_print_heap() {
  printf("printing heap\n");
  print_heap();
}

void test_insert() {
  for (int i = 1; i < 17; i++) {
    insert(i);
  }

  print_heap();
}

void test_size() {
  printf("size: %d, empty?: %d\n", get_size(), is_empty());
}

void test_extract_max() {
  for (int i = 1; i < 12; i++) {
    printf("removed max: %d\n", extract_max());
    print_heap();
    test_size();
  }
}

void test_remove() {
  printf("removed %d\n", _remove(2));
  print_heap();
  printf("removed %d\n", _remove(3));
  print_heap();
}

void test_heap_sort() {
  int arr[] = { 5, 1, 9, 0, 3, 4, 7, 8, 6, 2 };
  int size = 10;

  heap_sort(arr, size);
  test_print_heap();
}

void runalltests() {
  test_initialize();
  test_print_heap();
  test_size();
  test_insert();
  test_extract_max();
  test_remove();
  test_heap_sort();

  printf("all tests passed\n");
}