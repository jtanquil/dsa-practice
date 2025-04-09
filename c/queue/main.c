#include <stdio.h>
#include "queue.h"

void main() {
  struct dlist *list = initialize();

  printf("size: %d, empty: %d\n", size(list), empty(list));

  for (int i = 0; i < 5; i++) {
    enqueue(list, i * i);
    printf("enqueued %d\n", i * i);
  }

  printf("size: %d, empty: %d\n", size(list), empty(list));

  for (int i = 0; i < 5; i++) {
    printf("dequeued %d\n", dequeue(list));
  }

  printf("size: %d, empty: %d\n", size(list), empty(list));
}