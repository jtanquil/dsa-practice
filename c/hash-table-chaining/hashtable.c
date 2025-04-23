#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 13
#define POLYNOMIAL_CONSTANT 255

struct node {
  char *key;
  char *value;
};

struct listnode {
  struct node *val;
  struct listnode *next;
};

static struct listnode *table[TABLE_SIZE];

void initialize() {
  for (int i = 0; i < TABLE_SIZE; i++) {
    table[i] = NULL;
  }
}

struct node *create_node(char *key, char *value) {
  struct node *new_node = malloc(sizeof(struct node));
  new_node->key = key;
  new_node->value = value;
  return new_node;
}

struct listnode *create_list_node(char *key, char *value) {
  struct node *val = create_node(key, value);
  struct listnode *new_listnode = malloc(sizeof(struct listnode));
  new_listnode->val = val;
  new_listnode->next = NULL;
  return new_listnode;
}

// polynomial hash
int hash(char *key) {
  int i = 0;

  for (; *key != '\0'; key++) {
    i = (*key + i * POLYNOMIAL_CONSTANT) % TABLE_SIZE;
  }

  return i;
}

struct listnode *find(char *key) {
  int index = hash(key);
  struct listnode *current_node = table[index];

  while (current_node != NULL) {
    if (current_node->val->key == key) {
      break;
    } else {
      current_node = current_node->next;
    }
  }

  return current_node;
}

// if the slot is empty, it's the new head of a new list
// if the key is already in the table, overwrite the value
// otherwise, the k/v pair becomes the new head of this slot
void add(char *key, char *value) {
  struct listnode *new_node = create_list_node(key, value);
  int index = hash(key);

  if (table[index] == NULL) {
    table[index] = new_node;
  } else {
    struct listnode *current_head = table[index];
    struct listnode *search_node = current_head;

    while (search_node != NULL) {
      if (search_node->val->key == key) {
        search_node->val->value = value;
        return;
      } else {
        search_node = search_node->next;
      }
    }

    new_node->next = current_head;
    table[index] = new_node;
  }
}

int exists(char *key) {
  return find(key) != NULL;
}

char *get(char *key) {
  struct listnode *result = find(key);

  if (result != NULL) {
    return result->val->value;
  } else {
    printf("key %s not found\n", key);
    return NULL;
  }
}

void _remove(char *key) {
  struct listnode *result = find(key);

  if (result == NULL) {
    printf("error: key %s not found\n", key);
  } else {
    int index = hash(key);
    struct listnode *prev = table[index];

    // if it's the head, then the next element is the new head
    // otherwise, search for the element and splice it from the list
    if (prev == result) {
      table[index] = result->next;
      free(result);
    } else {
      while (prev->next != result) {
        prev = prev->next;
      }

      prev->next = result->next;
      free(result);
    }
  }
}

void print_hash_table() {
  printf("table:\n");

  for (int i = 0; i < TABLE_SIZE; i++) {
    if (table[i] == NULL) {
      printf("[%d]: empty\n", i);
    } else {
      struct listnode *current_node = table[i];

      printf("[%d]:", i);
      do {
        printf(" { key: %s, value: %s }", current_node->val->key, current_node->val->value);
        current_node = current_node->next;
      } while (current_node != NULL);
      printf("\n");
    }
  }

  printf("---\n");
}