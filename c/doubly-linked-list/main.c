#include <stdio.h>
#include "dlinkedlist.h"

void printall() {
  printf("---\n");

  for (int i = 0; i < size(); i++) {
    printf("list[%d]: %d\n", i, value_at(i));
  }
}

void printallreverse() {
  printf("---\n");

  for (int i = 0; i < size(); i++) {
    printf("list[%d]: %d\n", size() - 1 - i, value_n_from_end(i));
  }
}

void main() {
  initialize();

  printf("current size: %d\nempty: %d\n\n", size(), empty());

  for (int i = 0; i < 7; i++) {
    push_front(i * i);
  }

  for (int i = 0; i < 5; i++) {
    push_back(-i * i);
  }

  printall();

  printf("\nsize: %d\nfront: %d\nback: %d\n", size(), front(), back());

  printf("pop front: %d\n", pop_front());
  printf("pop back: %d\n", pop_back());

  printall();

  printallreverse();

  insert(0, 100);
  insert(size(), 1000);
  insert(3, -100);

  printall();
}