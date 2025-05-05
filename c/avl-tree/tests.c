#include <stdio.h>
#include "avltree.h"

void test_initialize() {
  initialize();
  printf("tree initialized\n");
}

void test_insert() {
  int arr[] = { 40, 20, 60, 10, 30, 50, 70, 36, 49 };

  for (int i = 0; i < 9; i++) {
    insert(arr[i]);
  }
}

void test_print_tree() {
  printf("---\n");
  print_tree();
}

void test_print_levels() {
  printf("---\n");
  print_levels();
}

void runalltests() {
  test_initialize();
  test_insert();
  test_print_tree();
  test_print_levels();

  printf("all tests passed\n");
}