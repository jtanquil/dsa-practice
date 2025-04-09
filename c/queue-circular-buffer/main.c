#include <stdio.h>
#include "queue.h"

void main() {
  struct cbuffer *buf = initialize(10, 1);

  printf("buffer initialized. size: %d, empty: %d\n", size(buf), empty(buf));

  for (int i = 0; i < 20; i++) {
    enqueue(buf, i * i);
  }

  for (int i = 0; i < 10; i++) {
    printf("dequeued %d\n", dequeue(buf));
  }

  for (int i = 0; i < 30; i++) {
    enqueue(buf, i * i);

    if (i % 2 == 0) {
      printf("dequeued %d\n", dequeue(buf));
    }
  }
}