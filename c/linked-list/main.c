#include <stdio.h>
#include "linkedlist.h"

void main() {
  printf("size: %d, empty: %d\n", size(), empty());

  for (int i = 0; i < 5; i++) {
    push_front(i * i);
  }

  printf("head element: %d\n", front());
  printf("tail element: %d\n", back());
  printf("size: %d\n", size());

  for (int i = 0; i < 5; i++) {
    push_back(-i * i);
  }

  for (int i = 0; i < 10; i++) {
    printf("list[%d]: %d\n", i, value_at(i));
  }

  printf("head element: %d\n", front());
  printf("tail element: %d\n", back());
  printf("size: %d\n", size());

  printf("pop_front: %d\n", pop_front());
  printf("pop_back: %d\n", pop_back());
  printf("head: %d, tail: %d, size: %d\n", front(), back(), size());

  for (int i = 0; i < size(); i++) {
    printf("list[%d]: %d\n", i, value_at(i));
  }

  insert(3, 256);
  insert(5, -73);
  insert(1, 112);

  for (int i = 0; i < size(); i++) {
    printf("list[%d]: %d\n", i, value_at(i));
  }
}