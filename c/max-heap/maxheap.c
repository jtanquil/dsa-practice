#include <stdio.h>
#include <stdlib.h>

#define INITIAL_SIZE 16
#define RESIZE_FACTOR 2

static int *max_heap;
static int heap_capacity;
static int size;

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
  if (size == heap_capacity) {
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
void sift_down(int current_index) {
  int left = left_index(current_index);
  int right = right_index(current_index);
  int biggest_child = (max_heap[left] > max_heap[right]) ? max_heap[left] : max_heap[right];

  if (max_heap[current_index] < biggest_child) {
    int temp = biggest_child;

    if (max_heap[left] == biggest_child) {
      max_heap[left] = max_heap[current_index];
      max_heap[current_index] = biggest_child;
      sift_down(left);
    } else {
      max_heap[right] = max_heap[current_index];
      max_heap[current_index] = biggest_child;
      sift_down(right);
    }
  }
}

// save max_heap[index] to return, then swap it with the last element
// set the last element to 0, resize if necessary
// then heapify down starting from max_heap[index]
int _remove(int index) {
  int element = max_heap[index];
  max_heap[index] = max_heap[size - 1];
  max_heap[size - 1] = 0;
  size--;

  if (size < heap_capacity / 4) {
    resize(0);
  }

  sift_down(index);
  return element;
}

int extract_max() {
  return _remove(0);
}

void heapify(int *heap);
void heap_sort(int *heap);