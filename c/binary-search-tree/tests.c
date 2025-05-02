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

void get_min_max_test() {
  printf("min: %d\n", get_min());
  printf("max: %d\n", get_max());
}

void delete_test() {
  delete_value(7);
  delete_value(20);
  delete_value(4);
  delete_value(16);
}

void print_levels_test() {
  printf("---\n");
  printf("levels:\n");
  print_levels();
}

void delete_tree_test() {
  printf("deleting tree...\n");
  delete_tree();
  print_values_test();
}

void get_successor_predecessor_test() {
  int arr[] = { 40, 20, 60, 10, 30, 50, 70, 36, 49 };

  for (int i = 0; i < 9; i++) {
    insert(arr[i]);
  }

  int arr2[] = { 35, 45, 75, 5 };

  for (int i = 0; i < 4; i++) {
    printf("successor of %d: %d\n", arr2[i], get_successor(arr2[i]));
    printf("predecessor of %d: %d\n", arr2[i], get_predecessor(arr2[i]));
  }
}

void runalltests() {
  initialize_test();
  print_values_test();
  insert_values_test();
  print_values_test();
  node_count_test();
  is_in_tree_test();
  get_height_test();
  get_min_max_test();
  print_levels_test();
  delete_test();
  print_levels_test();
  print_values_test();
  node_count_test();
  delete_tree_test();
  get_successor_predecessor_test();

  printf("all tests passed\n");
}