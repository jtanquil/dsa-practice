#include <stdio.h>
#include <stdlib.h>

#define INITIAL_SIZE 8
#define RESIZE_FACTOR 2

static int *max_heap;
static int heap_capacity;
static int size;
// flag that indicates whether the array is static or dynamic
// use static for in-place heapsort
static int static_heap = 0;

// use a dynamic array for storage
void initialize() {
  max_heap = malloc(INITIAL_SIZE * sizeof(int));
  heap_capacity = INITIAL_SIZE;
  size = 0;

  // for testing's sake, use zeroes as a null flag
  for (int i = 0; i < heap_capacity; i++) {
    max_heap[i] = 0;
  }
}

void print_heap() {
  for (int i = 0; i < heap_capacity; i++) {
    printf("[%d]: %d\n", i, max_heap[i]);
  }
}

int get_size() {
  return size;
}

int is_empty() {
  return size == 0;
}

int left_index(int node_index) {
  return 2 * node_index + 1;
}

int right_index(int node_index) {
  return left_index(node_index) + 1;
}

int parent_index(int node_index) {
  return (node_index - 1) / 2;
}

// grow is a boolean that indicates whether to grow (true) or shrink (false) the array
void resize(int grow) {
  int new_size = (grow) ? heap_capacity * RESIZE_FACTOR : heap_capacity / RESIZE_FACTOR;
  int *new_heap = malloc(new_size * sizeof(int));
  heap_capacity = new_size;

  for (int i = 0; i < heap_capacity ; i++) {
    if (i < size) {
      new_heap[i] = max_heap[i];
    } else {
      new_heap[i] = 0;
    }
  }

  free(max_heap);
  max_heap = new_heap;
}

// compare current index to its parent
// if current > parent, swap them
// call on parent recursively until current <= parent
void sift_up(int current_index) {
  int current_parent = parent_index(current_index);

  if (max_heap[current_parent] < max_heap[current_index]) {
    int temp = max_heap[current_parent];
    max_heap[current_parent] = max_heap[current_index];
    max_heap[current_index] = temp;
    sift_up(current_parent);
  }
}

// insert into the first empty (zero) slot
// resize if necessary first
// then heapify up - swap nodes to satisfy the max heap property
void insert(int key) {
  if ((size == heap_capacity) && !static_heap) {
    resize(1);
  } 

  max_heap[size] = key;
  sift_up(size++);
}

int get_max() {
  return max_heap[0];
}

// compare current_index to its biggest child
// if current < child, swap them
// recursively call on child until current >= child
// stop recursion if going beyond the size of the heap - three cases:
// 1. left is out of bounds, then we can't go any further
// 2. right is out of bounds, then we can still test the left child
// 3. neither are out of bounds, then test both
void sift_down(int current_index) {
  int left = left_index(current_index);

  if (left >= size) {
    return;
  }

  int right = right_index(current_index);
  int biggest_child, biggest_child_index;

  if (right >= size) {
    biggest_child_index = left;
    biggest_child = max_heap[left];
  } else {
    biggest_child = (max_heap[left] > max_heap[right]) ? max_heap[left] : max_heap[right];
    biggest_child_index = (biggest_child == max_heap[left]) ? left : right;
  }

  if (max_heap[current_index] < biggest_child) {
    int temp = biggest_child;
    max_heap[biggest_child_index] = max_heap[current_index];
    max_heap[current_index] = biggest_child;
    sift_down(biggest_child_index);
  }
}

// save max_heap[index] to return, then swap it with the last element
// set the last element to 0, resize if necessary
// then heapify down starting from max_heap[index]
int _remove(int index) {
  int element = max_heap[index];
  max_heap[index] = max_heap[size - 1];

  // in the static case, we actually want to perform the swap
  max_heap[size - 1] = (static_heap) ? element : 0;
  size--;

  if ((size < heap_capacity / 4) && !static_heap) {
    resize(0);
  }

  sift_down(index);
  return element;
}

int extract_max() {
  return _remove(0);
}

// reassign max_heap to a fixed-size array
// initialize heap as an empty prefix of arr
void heapify(int *arr, int array_size) {
  if (max_heap) {
    free(max_heap);
  }

  max_heap = arr;
  heap_capacity = array_size;
  size = 0;
  static_heap = 1;
}

// initialize heap as an empty prefix of arr
// insert elements into the heap until the size == array_size
// then remove the maximum element, swapping elements, until size == 0
// end result is that arr will be sorted in place
void heap_sort(int *arr, int array_size) {
  heapify(arr, array_size);

  while (size < array_size) {
    insert(arr[size]);
  }

  while (size > 0) {
    extract_max();
  }
}