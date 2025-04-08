// specification for singly linked list from
// https://github.com/jwasham/coding-interview-university?tab=readme-ov-file#linked-lists

#include <stdio.h>
#include <stdlib.h>

struct lnode {
  int item;
  struct lnode *next;
};

static int _size = 0;
static struct lnode *head;
static struct lnode *tail;

struct lnode *create_node(int item) {
  struct lnode *node;
  node = malloc(sizeof(struct lnode));
  node->item = item;
  node->next = NULL;

  return node;
}

int size() {
  return _size;
}

int empty() {
  return _size == 0;
}

int front() {
  if (head != NULL) {
    return head->item;
  } else {
    printf("error: list is empty\n");
    return NULL;
  }
}

int back() {
  if (head != NULL) {
    struct lnode *current_node = head;

    while (current_node->next != NULL) {
      current_node = current_node->next;
    }

    return current_node->item;
  } else {
    printf("error: list is empty\n");
    return NULL;
  }
}

void push_front(int item) {
  struct lnode *new_head = create_node(item);

  // if it's the first element of the list, set it to the head and tail
  // otherwise, just update the head
  if (_size == 0) {
    head = new_head;
    tail = new_head;
  } else {
    new_head->next = head;
    head = new_head;
  }

  _size++;
}

void push_back(int item) {
  struct lnode *new_tail = create_node(item);

  // if it's the first element of the list, set it to the head and tail
  // otherwise, just update the tail
  if (_size == 0) {
    head = new_tail;
    tail = new_tail;
  } else {
    tail->next = new_tail;
    tail = new_tail;
  }

  _size++;
}

void insert(int index, int item) {
  if (index == 0) {
    push_front(item);
  } else if (index == _size) {
    push_back(item);
  } else if (index < 0 || index >= _size) {
    printf("error: index %d is out of bounds\n", index);
  } else {
    // find the node before the given index
    struct lnode *prev_node = head;

    for (int i = 0; i < index - 1; i++) {
      prev_node = prev_node->next;
    }

    // create a new node and insert it at index
    struct lnode *new_node = create_node(item);
    new_node->next = prev_node->next;
    prev_node->next = new_node;

    _size++;
  }
}

int value_at(int index) {
  if (index < 0 || index >= _size) {
    printf("error: index %d is out of bounds\n", index);
    return NULL;
  } else if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    struct lnode *target_node = head;

    for (int i = 0; i < index; i++) {
      target_node = target_node->next;
    }

    return target_node->item;
  }
}

int value_n_from_end(int index) {
  if (index < 0 || index >= _size) {
    printf("error: index %d is out of bounds\n", index);
    return NULL;
  } else {
    return value_at(_size - 1 - index);
  }
}

int pop_front() {
  if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    struct lnode *old_head = head;
    int item = old_head->item;
    
    // will set head to NULL if there is only one element in the list
    head = old_head->next;

    // if this is the only element of the list, set tail to NULL
    if (_size == 1) {
      tail = NULL;
    }

    free(old_head);
    _size--;
    return item;
  }
}

int pop_back() {
  if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    struct lnode *old_tail = tail;
    int item = old_tail->item;

    // if it's the only element of the list, set head and tail to NULL
    // otherwise, traverse the list from head until getting the 2nd to last element
    if (_size == 1) {
      head = NULL;
      tail = NULL;
    } else {
      struct lnode *new_tail = head;

      while (new_tail->next != old_tail) {
        new_tail = new_tail->next;
      }

      new_tail->next = NULL;
      tail = new_tail;
    }

    free(old_tail);
    _size--;
    return item;
  }
}

void erase(int index) {
  if (index == 0) {
    pop_front();
  } else if (index == _size - 1) {
    pop_back();
  } else if (index < 0 || index >= _size) {
    printf("error: index %d is out of bounds\n", index);
  } else {
    // find the node before the given index
    struct lnode *prev_node = head;

    for (int i = 0; i < index - 1; i++) {
      prev_node = prev_node->next;
    }

    // this case only runs if there are at least three elements,
    // so prev_node->next != NULL
    struct lnode *node_to_erase = prev_node->next;

    // update the tail if necessary
    if (prev_node->next == tail) {
      tail = prev_node;
    }

    prev_node->next = prev_node->next->next;

    free(node_to_erase);
    _size--;
  }
}

int remove_value(int item) {
  if (_size == 0) {
    printf("error: list is empty\n");
    return NULL;
  } else {
    struct lnode *current_node = head;
    int index = 0;

    while (current_node != NULL && current_node->item != item) {
      current_node = current_node->next;
      index++;
    }

    if (current_node == NULL) {
      printf("element %d not found, size: %d\n", item, _size);
      return NULL;
    } else {
      erase(index);
      printf("element %d removed at index %d, size: %d\n", item, index, _size);
      return index;
    }
  }
}

// keep track of a current = head
// while current->next != NULL,
// keep track of next = current->next
// set current->next = current
// go to next 
void reverse() {
  if (_size == 0) {
    printf("error: list is empty\n");
  } else if (_size > 1) { // don't need to reverse the list if it has 1 element
    struct lnode *current = head;
    struct lnode *next = current->next;

    current->next = NULL;

    while (next != NULL) {
      if (next->next != NULL) {
        struct lnode *next_next = next->next;
        next->next = current;
        current = next;
        next = next_next;
      } else {
        next->next = current;
        break;
      }
    }

    // finally, swap the head and tail
    struct lnode *swap = head;
    head = tail;
    tail = swap;
  }
}