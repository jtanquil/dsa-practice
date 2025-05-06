#include <stdio.h>
#include "avltree.h"

void test_initialize() {
  initialize();
  printf("tree initialized\n");
}

void test_insert() {
  int arr[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

  for (int i = 0; i < 10; i++) {
    printf("inserting %d\n", arr[i]);
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

void test_get_size() {
  printf("current tree size: %d\n", get_size());
}

void test_delete_value() {
  delete_value(8);
  delete_value(9);
  delete_value(1);
  delete_value(-5);
  delete_value(2);
  delete_value(0);
}

void runalltests() {
  test_initialize();
  test_get_size();
  test_insert();
  test_get_size();
  test_print_tree();
  test_print_levels();
  test_delete_value();
  test_print_levels();
  test_get_size();

  printf("all tests passed\n");
}