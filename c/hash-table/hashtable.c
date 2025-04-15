#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 13
#define SEARCH_MODE 0
#define INSERT_MODE 1

struct node {
  char *key;
  char *value;
};

static struct node *slots[TABLE_SIZE];
static struct node deleted = { NULL, NULL }; // represents a deleted node

void initialize() {
  for(int i = 0; i < TABLE_SIZE; i++) {
    slots[i] = NULL;
  }
}

struct node *create_node(char *key, char *value) {
  struct node *new_node = malloc(sizeof(struct node));
  new_node->key = key;
  new_node->value = value;

  return new_node;
}

// naive hash function for now
int hash(char *key, int size) {
  int i = 0;

  for (; *key != '\0'; key++) {
    i += *key;
  }

  return i % size;
}

// if inserting, probing will finish at a deleted node (to insert)
// if searching (for get or _remove), probing will skip deleted nodes
int is_not_target_node(struct node *current_node, int insert_mode) {
  if (insert_mode) {
    return (current_node != NULL && current_node != &deleted);
  } else {
    return current_node != NULL;
  }
}

int get_index(char *key, int insert_mode) {
  int index = hash(key, TABLE_SIZE);
  int iterations = 0;
  struct node *current_node = slots[index];

  // probing operation: if the node's key doesn't match, move to the next node
  // keep going until the key is found, or an empty node is found
  // insert_mode flag used to determine whether deleted nodes are skipped
  while (is_not_target_node(current_node, insert_mode)) {
    if (current_node->key == key || iterations == TABLE_SIZE) {
      break; 
    } else {
      index = (index + 1) % TABLE_SIZE;
      iterations++;
      current_node = slots[index];
    }
  }

  // break the loop after iterating through the entire table to prevent an infinite loop
  // on a full table  
  if (iterations == TABLE_SIZE) {
    return -1; // table is full and the entry isn't there
  } else {
    return index;
  }
}

void add(char *key, char *value) {
  int index = get_index(key, INSERT_MODE);

  if (index < 0) {
    printf("error: hash table is full\n");
  } else {
    // overwrite the existing value, or insert the node
    if (slots[index] == NULL || slots[index] == &deleted) {
      struct node *new_node = create_node(key, value);
      slots[index] = new_node;
    } else {
      slots[index]->value = value;
    }
  }
}

int exists(char *key) {
  if (slots[get_index(key, SEARCH_MODE)] == NULL) {
    return 0;
  } else {
    return 1;
  }
}

char *get(char *key) {
  if (exists(key)) {
    return slots[get_index(key, SEARCH_MODE)]->value;
  } else {
    return NULL;
  }
}

int _remove(char *key) {
  int index = get_index(key, SEARCH_MODE);

  if (index < 0) {
    printf("error: key '%s' is not in the table\n", key);
  } else {
    if (slots[index] == NULL) {
      printf("error: key '%s' is not in the table\n", key);
      return -1;
    } else {
      struct node *old_node = slots[index];
      slots[index] = &deleted;
      free(old_node);
      return 1;
    }
  }
};

void print_hash_table(int only_exists) {
  printf("table:\n");

  for (int i = 0; i < TABLE_SIZE; i++) {
    struct node *current_node = slots[i];

    if (current_node == NULL && !only_exists) {
      printf("[%d]: empty\n", i);
    } else if (current_node == &deleted && !only_exists) {
      printf("[%d]: deleted\n", i);
    } else if (current_node != NULL && current_node != &deleted) {
      printf("[%d]: { key: %s, value: %s }\n", i, current_node->key, current_node->value);
    }
  }
  
  printf("---\n");
}