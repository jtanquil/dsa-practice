#include <stdio.h>
#include "dynamicarray.h"

void main() {
  initialize();

  printf("---\n");

  for (int i = 0; i < 17; i++) {
    push(i * i);
    printf("arr[%d]: %d\n", i, at(i));
  }

  printf("---\n");

  insert(15, -2);
  prepend(3);

  for (int j = 0; j < 19; j++) {
    printf("arr[%d]: %d\n", j, at(j));
  }

  printf("---\n");

  printf("delete: %d\n", delete(15));
  printf("pop: %d\n", pop());

  printf("---\n");

  for (int j = 0; j < 17; j++) {
    printf("arr[%d]: %d\n", j, at(j));
  }

  printf("---\n");

  printf("find 25 at index %d\n", find(25));
  printf("find 420 at index %d\n", find(420));
}