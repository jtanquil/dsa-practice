#include <stdio.h>
#include <assert.h>
#include "binarysearchtree.h"

void initialize_test() {
  initialize();
  printf("succesfully initialized\n");
}

void print_values_test() {
  printf("---\n");
  print_values();
}

void insert_values_test() {
  int arr[] = { 8, 10, 16, 0, 6, 12, 4, 14, 18, 2, 20 };

  for (int i = 0; i < 11; i++) {
    insert(arr[i]);
  }
}

void node_count_test() {
  printf("node count: %d\n", get_node_count());
}

void is_in_tree_test() {
  int arr[] = { 2, 4, 8, 7, -5, 25 };
  
  for (int i = 0; i < 6; i++) {
    printf("%d is in the tree: %d\n", arr[i], is_in_tree(arr[i]));
  }
}

void get_height_test() {
  printf("height: %d\n", get_height());
}

void runalltests() {
  initialize_test();
  print_values_test();
  insert_values_test();
  print_values_test();
  node_count_test();
  is_in_tree_test();
  get_height_test();

  printf("all tests passed\n");
}