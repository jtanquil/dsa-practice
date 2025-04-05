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
  arr = malloc(INITIAL_SIZE * sizeof(int));

  printf("initialized array\nsize: %d\ncapacity: %d\narray elements: ", _size, _capacity);
  for (int i = 0; i < _capacity; i++) {
    printf("%d ", *(arr + i));
  }
  printf("\n");
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
    return *(arr + index);
  } else {
    printf("error: index %d is out of bounds\n", index);
    return -1;
  }
}

void resize(int new_size) {
  int *newarr = calloc(new_size, sizeof(int));

  for (int i = 0; i < _size; i++) {
    *(newarr + i) = *(arr + i);
  }

  _capacity = new_size;

  free(arr);
  arr = newarr; 
}

int push(int item) {
  if (_size < _capacity) {
    *(arr + _size) = item;
    _size++;
    return _size;
  } else {
    resize(_capacity * RESIZE_FACTOR);
    return push(item);
  }
}

int insert(int index, int item) {
  if (index < 0 || index >= _size) {
    printf("error: index out of bounds\n");
    return NULL;
  } else {
    if (_size == _capacity) {
      resize(_capacity * RESIZE_FACTOR);
    }

    if (_size == index) {
      return push(item);
    } else {
      for (int j = _size - 1; j >= index; j--) {
        *(arr + j + 1) = *(arr + j);
      }

      *(arr + index) = item;
      _size++;
      return _size;
    }
  }
}

int prepend(int item) {
  return insert(0, item);
}

int delete(int index) {
  if (index < 0 || index >= _capacity) {
    printf("error: index out of bounds\n");
    return NULL;
  } else {
    int val = *(arr + index);

    for (int i = index; i < _size; i++) {
      *(arr + i) = *(arr + i + 1);
    }

    _size--;

    if (_size <= 0.25 * _capacity) {
      resize(_capacity / RESIZE_FACTOR);
    }

    return val;
  }
}

int pop() {
  return delete(0);
}

int find(int item) {
  for (int i = 0; i < _size; i++) {
    if (*(arr + i) == item) {
      return i;
    }
  }

  return -1;
}