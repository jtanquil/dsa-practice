#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 101

struct node {
  char *key;
  char *value;
};

static struct node *slots[TABLE_SIZE];

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

int get_index(char *key) {
  int index = hash(key, TABLE_SIZE);
  int iterations = 0;
  struct node *current_node = slots[index];

  // probing operation: if the key is there or the space is empty, return the index
  // otherwise, check the next index (mod the table size) and repeat
  // break the loop after iterating through the entire table to prevent an infinite loop on a full table  
  while (current_node != NULL) {
    if (current_node->key == key || iterations == TABLE_SIZE) {
      break; 
    } else {
      index = (index + 1) % TABLE_SIZE;
      iterations++;
      current_node = slots[index];
    }
  }

  if (iterations == TABLE_SIZE) {
    return -1; // table is full and the entry isn't there
  } else {
    return index;
  }
}

void add(char *key, char *value) {
  int index = get_index(key);

  if (index < 0) {
    printf("error: hash table is full\n");
  } else {
    // overwrite the existing value, or insert the node
    if (slots[index] == NULL) {
      struct node *new_node = create_node(key, value);
      slots[index] = new_node;
    } else {
      slots[index]->value = value;
    }
  }
}

int exists(char *key) {
  if (slots[get_index(key)] == NULL) {
    return 0;
  } else {
    return 1;
  }
}

char *get(char *key) {
  if (exists(key)) {
    return slots[get_index(key)]->value;
  } else {
    return NULL;
  }
}

int _remove(char *key) {
  int index = get_index(key);

  if (index < 0) {
    printf("error: key is not in the table\n");
  } else {
    if (slots[index] == NULL) {
      printf("error: key is not in the table\n");
      return NULL;
    } else {
      struct node *old_node = slots[index];
      slots[index] = NULL;
      free(old_node);
      return 1;
    }
  }
};