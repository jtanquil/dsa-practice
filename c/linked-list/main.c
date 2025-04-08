#include <stdio.h>
#include "linkedlist.h"

void printall() {
  printf("---\n");

  for (int i = 0; i < size(); i++) {
    printf("list[%d]: %d\n", i, value_at(i));
  }
}

void main() {
  printf("size: %d, empty: %d\n", size(), empty());

  for (int i = 0; i < 4; i++) {
    push_front(i * i);
  }

  printf("head element: %d\n", front());
  printf("tail element: %d\n", back());
  printf("size: %d\n", size());

  for (int i = 0; i < 7; i++) {
    push_back(-i * i);
  }

  printall();

  printf("head element: %d\n", front());
  printf("tail element: %d\n", back());
  printf("size: %d\n", size());

  printf("pop_front: %d\n", pop_front());
  printf("pop_back: %d\n", pop_back());
  printf("head: %d, tail: %d, size: %d\n", front(), back(), size());

  printall();

  insert(2, 256);
  insert(3, -73);
  insert(1, 112);

  printall();

  erase(1);
  erase(0);
  erase(size() - 1);

  printall();

  printf("---\n");

  for (int i = 0; i < size(); i++) {
    printf("list[%d]: %d\n", size() - 1 - i, value_n_from_end(i));
  }

  remove_value(0);
  remove_value(0);

  printall();

  remove_value(0);

  printall();

  reverse();

  printall();
}