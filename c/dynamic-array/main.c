#include <stdio.h>
#include "dynamicarray.h"

void main() {
  initialize();

  printf("\n");

  for (int i = 0; i < 10; i++) {
    push(i * i);
    printf("arr[%d]: %d\n", i, at(i));
  }

  insert(3, -1);

  for (int j = 0; j < 11; j++) {
    printf("arr[%d]: %d\n", j, at(j));
  }
}