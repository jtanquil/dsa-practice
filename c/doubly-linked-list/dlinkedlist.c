#include <stdio.h>
#include <stdlib.h>

struct dlnode {
  int item;
  struct dlnode *next;
  struct dlnode *prev;
};

static int _size = 0;
static struct dlnode *sentinel;

// sentinel->next points to the head, sentinel->prev points to the tail
// creates a circularly linked structure:
// ... <-> node <-> ... <-> tail <-> sentinel <-> head <-> ... <-> node <-> ...
void initialize() {
  struct dlnode *new_sentinel = malloc(sizeof(struct dlnode));
  new_sentinel->item = NULL;
  new_sentinel->next = NULL;
  new_sentinel->prev = NULL;
  sentinel = new_sentinel;

  printf("initialized doubly linked list\n");
}

int size() {
  return _size;
}

int empty() {
  return _size == 0;
}

struct dlnode *create_node(int item) {
  struct dlnode *node = malloc(sizeof(struct dlnode));
  node->item = item;
  node->next = NULL;
  node->prev = NULL;

  return node;
}

// if it's the first element of the list, it's the new head and tail
// otherwise it's just the new head
void push_front(int item) {
  struct dlnode *node = create_node(item);
  node->prev = sentinel;

  if (_size == 0) {
    node->next = sentinel;
    sentinel->next = node;
    sentinel->prev = node;
  } else {
    node->next = sentinel->next;
    sentinel->next->prev = node;
    sentinel->next = node;
  }

  _size++;
}

// if it's the first element of the list, it's the new head and tail
// otherwise it's just the new tail
void push_back(int item) {
  struct dlnode *node = create_node(item);
  node->next = sentinel;

  if (_size == 0) {
    node->prev = sentinel;
    sentinel->next = node;
    sentinel->prev = node;
  } else {
    node->prev = sentinel->prev;
    sentinel->prev->next = node;
    sentinel->prev = node;
  }

  _size++;
}

int front() {
  if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    return sentinel->next->item;
  }
}

int back() {
  if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    return sentinel->prev->item;
  }
}

int value_at(int index) {
  if (index < 0 || index >= _size) {
    printf("error: index %d out of bounds", index);
    return NULL;
  } else if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    struct dlnode *current_node = sentinel->next;

    for (int i = 0; i < index; i++) {
      current_node = current_node->next;
    }

    return current_node->item;
  }
}

int value_n_from_end(int index) {
  return value_at(size() - 1 - index);
}

int pop_front(void) {
  if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    struct dlnode *current_head = sentinel->next;
    int head_item = current_head->item;

    // two cases: head == tail (size 1) or head != tail
    if (_size == 1) {
      sentinel->next = NULL;
      sentinel->prev = NULL;
    } else {
      struct dlnode *new_head = current_head->next;
      sentinel->next = new_head;
      new_head->prev = sentinel;
    }

    free(current_head);
    _size--;
    return head_item;
  }
}

int pop_back(void) {
  if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    struct dlnode *current_tail = sentinel->prev;
    int tail_item = current_tail->item;

    // two cases: head == tail (size 1) or head != tail
    if (_size == 1) {
      sentinel->next = NULL;
      sentinel->prev = NULL;
    } else {
      struct dlnode *new_tail = current_tail->prev;
      sentinel->prev = new_tail;
      new_tail->next = sentinel;
    }

    free(current_tail);
    _size--;
    return tail_item;
  }
}

void insert(int index, int item) {
  if (index == 0) {
    push_front(item);
  } else if (index == _size) {
    push_back(item);
  } else if (index < 0 || index > _size) {
    printf("error: index %d out of bounds\n", index);
  } else {
    struct dlnode *current_node = sentinel->next;

    for (int i = 0; i < index; i++) {
      current_node = current_node->next;
    }

    struct dlnode *previous_node = current_node->prev;
    
    // create the new node and splice it into the list
    struct dlnode *new_node = create_node(item);
    new_node->prev = previous_node;
    new_node->next = current_node;
    current_node->prev = new_node;
    previous_node->next = new_node;

    _size++;
  }
}

void erase(int index) {
  if (index == 0) {
    pop_front();
  } else if (index == _size - 1) {
    pop_back();
  } else if (index < 0 || index >= _size) {
    printf("error: index %d out of bounds\n", index);
  } else {
    struct dlnode *current_node = sentinel->next;

    for (int i = 0; i < index; i++) {
      current_node = current_node->next;
    }

    struct dlnode *previous_node = current_node->prev;
    struct dlnode *next_node = current_node->next;

    // splice the node out of the list
    previous_node->next = next_node;
    next_node->prev = previous_node;

    free(current_node);
    _size--;
  }
}

int remove_value(int item) {
  if (_size == 0) {
    printf("error: list is empty\n");
    return -1;
  } else {
    struct dlnode *current_node = sentinel->next;
    int index = 0;

    while (current_node != sentinel && current_node->item != item) {
      current_node = current_node->next;
      index++;
    }

    if (current_node == sentinel) {
      printf("element %d not found\n", item);
      return -1;
    } else {
      erase(index);
      return index;
    }
  }
}

void reverse() {
  if (_size == 0) {
    printf("error: list is empty\n");
  } else if (_size > 1) { // don't need to do anything if the list has one element
    struct dlnode *current_node = sentinel;
    
    // traverse through the sentinel and the list, swapping the next/prev 
    // pointers of each node
    for (int i = 0; i <= _size; i++) {
      struct dlnode *swap = current_node->next;
      current_node->next = current_node->prev;
      current_node->prev = swap;
      current_node = current_node->next;
    }
  }
}