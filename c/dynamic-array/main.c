#include <stdio.h>
#include "dynamicarray.h"

void main() {
  initialize();

  for (int i = 0; i < 14; i++) {
    push(i * 3);
  }

  for (int j = 0; j < 14; j++) {
    printf("arr[%d]: %d\n", j, at(j));
  }
}