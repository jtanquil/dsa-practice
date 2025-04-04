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
  arr = calloc(INITIAL_SIZE, sizeof(int));

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

void resize(int new_size) {
  int *newarr = calloc(new_size, sizeof(int));

  for (int i = 0; i < _size; i++) {
    *(newarr + i * sizeof(int)) = *(arr + i * sizeof(int));
  }

  _capacity = new_size;

  free(arr);
  arr = newarr; 
}

int push(int item) {
  if (_size < _capacity) {
    *(arr + _size * sizeof(int)) = item;
    _size++;
    return _size;
  } else {
    resize(_capacity * RESIZE_FACTOR);
    return push(item);
  }
}

int insert(int index, int item) {
  if (index < 0 || index >= _capacity) {
    printf("error: index out of bounds\n");
    return -1;   
  } else {
    if (_size == _capacity) {
      resize(_capacity * RESIZE_FACTOR);
    }

    printf("---\n");

    for (int j = _size - 1; j >= index; j--) {
      *(arr + (j + 1) * sizeof(int)) = *(arr + j * sizeof(int));
      printf("arr[%d]: %d\n", j + 1, *(arr + (j + 1) * sizeof(int)));
    }

    printf("---\n");

    *(arr + index * sizeof(int)) = item;
    _size++;
    return 1;
  }
}