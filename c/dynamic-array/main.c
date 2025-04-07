#include <stdio.h>
#include "dynamicarray.h"

void main() {
  initialize();

  printf("---\n");

  for (int i = 0; i < 17; i++) {
    push(i * i);
    printf("arr[%d]: %d, capacity: %d\n", size(), at(i), capacity());
  }

  printf("---\n");

  update(3, 100);
  insert(15, -2);
  prepend(3);

  for (int j = 0; j < 19; j++) {
    printf("arr[%d]: %d, capacity: %d\n", j, at(j), capacity());
  }

  printf("---\n");

  printf("delete: %d\n", delete(15));
  printf("pop: %d\n", pop());

  printf("---\n");

  for (int j = 0; j < 17; j++) {
    printf("arr[%d]: %d, capacity: %d\n", j, at(j), capacity());
  }

  printf("---\n");

  printf("find 25 at index %d\n", find(25));
  printf("find 420 at index %d\n", find(420));

  printf("---\n");

  printf("delete at index 3: %d\n", delete(3));
  printf("pop: %d\n", pop());

  printf("---\n");

  while (!is_empty()) {
    printf("popping %d, capacity: %d\n", pop(), capacity());
  }

  for (int i = 0; i < 32; i++) {
    push(3);
    printf("arr[%d]: %d, capacity: %d\n", i, at(i), capacity());
  }

  push(4);

  _remove(3);

  for (int j = 0; j < size(); j++) {
    printf("arr[%d]: %d, capacity: %d\n", j, at(j), capacity());
  }

}