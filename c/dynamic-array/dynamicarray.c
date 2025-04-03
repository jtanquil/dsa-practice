// Specification for a vector/dynamic array from 
// https://github.com/jwasham/coding-interview-university?tab=readme-ov-file#arrays

#include <stdio.h>
#include <stdlib.h>

#define INITIAL_SIZE 16
#define RESIZE_FACTOR 2

static int *arr;
static int _size;
static int _capacity;

void initialize() {
  _size = 0;
  _capacity = INITIAL_SIZE;
  arr = (int*) malloc(INITIAL_SIZE * sizeof(int));

  printf("initialized array\nsize: %d\ncapacity: %d\n", _size, _capacity);
}

int size() {
  return _size;
}

int capacity() {
  return _capacity;
}

int is_empty() {
  return _size == 0;
}

int at(int index) {
  if (index >= 0 && index < _size) {
    return *(arr + index * sizeof(int));
  } else {
    printf("error: index %d is out of bounds\n", index);
    return -1;
  }
}

int push(int item) {
  if (_size < _capacity) {
    *(arr + _size * sizeof(int)) = item;
    _size++;
    return _size;
  } else {
    printf("placeholder for resize\n");
    return -1;
  }
}