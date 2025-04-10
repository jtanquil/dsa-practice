#include <stdio.h>
#include "queue.h"

void main() {
  struct cbuffer *buf = initialize(10, 1);

  printf("buffer initialized. size: %d, empty: %d\n", size(buf), empty(buf));
  print_buf(buf);

  for (int i = 1; i <= 5; i++) {
    enqueue(buf, i * i);
    printf("enqueueing %d: ", i * i);
    print_buf(buf);
  }

  for (int i = 0; i < 3; i++) {
    printf("dequeueing %d: ", dequeue(buf));
    print_buf(buf);
  }

  for (int i = 1; i <= 12; i++) {
    enqueue(buf, -i * i * i);
    printf("enqueueing %d: ", -i * i * i);
    print_buf(buf);

    printf("dequeueing %d: ", dequeue(buf));
    print_buf(buf);
  }
}