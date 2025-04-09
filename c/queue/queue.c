// implementation w/doubly linked list
#include <stdio.h>
#include <stdlib.h>

struct dlnode {
  int item;
  struct dlnode *next;
  struct dlnode *prev;
};

struct dlist {
  int size;
  struct dlnode *sentinel;
};

struct dlist *initialize() {
  struct dlnode *sentinel = malloc(sizeof(struct dlnode));
  sentinel->item = NULL;
  sentinel->next = NULL;
  sentinel->prev = NULL;

  struct dlist *list = malloc(sizeof(struct dlist));
  list->size = 0;
  list->sentinel = sentinel;

  return list;
}

struct dlnode *create_node(int item) {
  struct dlnode *node = malloc(sizeof(struct dlnode));
  node->item = item;

  return node;
}

int empty(struct dlist *list) {
  return list->size == 0;
}

int size(struct dlist *list) {
  return list->size;
}

// push to the back of the queue
void enqueue(struct dlist *list, int item) {
  struct dlnode *node = create_node(item);
  node->next = list->sentinel;

  // if the list is empty, this is the new head and tail
  // otherwise, it's just the new tail
  if (empty(list)) {
    list->sentinel->next = node;
    list->sentinel->prev = node;
    node->prev = list->sentinel;
  } else {
    node->prev = list->sentinel->prev;
    node->prev->next = node;
    list->sentinel->prev = node;
  }

  (list->size)++;
}

// pop from the front of the queue
int dequeue(struct dlist *list) {
  if (empty(list)) {
    printf("error: list is empty");
    return NULL;
  } else {
    struct dlnode *node = list->sentinel->next;
    int item = node->item;

    // check if head == tail (equivalently, if the list has 1 element)
    if (list->sentinel->prev == list->sentinel->next) {
      list->sentinel->prev = NULL;
      list->sentinel->next = NULL;
    } else {
      list->sentinel->next = node->next;
      node->next->prev = list->sentinel;
    }

    free(node);
    (list->size)--;
    return item;
  }
}

