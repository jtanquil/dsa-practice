#include <stdio.h>
#include "avltree.h"

void test_initialize() {
  initialize();
  printf("tree initialized\n");
}

void test_insert() {
  int arr[] = { 0, -2, -5, -3, -6, -4 };

  for (int i = 0; i < 6; i++) {
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
  delete_value(-5);
  delete_value(36);
  delete_value(49);
  delete_value(60);
  delete_value(40);
}

void runalltests() {
  test_initialize();
  test_get_size();
  test_insert();
  test_get_size();
  test_print_tree();
  test_print_levels();
  //test_delete_value();
  //test_print_levels();
  test_get_size();

  printf("all tests passed\n");
}