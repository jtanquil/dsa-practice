#include <stdio.h>
#include <stdlib.h>

struct node {
  int key;
  struct node *left;
  struct node *right;
  struct node *parent;
};

struct tree {
  struct node *root;
};

static struct tree *new_tree;

struct node *create_node(int key) {
  struct node *new_node = malloc(sizeof(struct node));
  new_node->key = key;
  new_node->left = NULL;
  new_node->right = NULL;
  new_node->parent = NULL;

  return new_node;
}

void print_node(struct node *node) {
  printf("%d\n", node->key);
}

void *initialize() {
  new_tree = malloc(sizeof(struct tree));
  new_tree->root = NULL;
}

// print the values of the tree, from min to max
// implies in-order traversal of the tree
void print_subtree(struct node *current_node) {
  if (current_node->left != NULL) {
    print_subtree(current_node->left);
  }

  print_node(current_node);

  if (current_node->right != NULL) {
    print_subtree(current_node->right);
  }
}

void print_values() {
  if (new_tree->root == NULL) {
    printf("tree is empty\n");
  } else {
    print_subtree(new_tree->root);
  }  
}

// insert key into the bst:
// compare w/parent value, go left or right from there
// if that direction has no child, insert there
// otherwise, recursively insert into that child
void insert_subtree(int key, struct node *current_node) {
  if (key <= current_node->key) {
    if (current_node->left == NULL) {
      struct node *new_node = create_node(key);
      new_node->parent = current_node;
      current_node->left = new_node;
    } else {
      insert_subtree(key, current_node->left);
    }
  } else if (key > current_node->key) {
    if (current_node->right == NULL) {
      struct node *new_node = create_node(key);
      new_node->parent = current_node;
      current_node->right = new_node;
    } else {
      insert_subtree(key, current_node->right);
    }
  }
}

void insert(int key) {
  if (new_tree->root == NULL) {
    new_tree->root = create_node(key);
  } else {
    insert_subtree(key, new_tree->root);
  }
}

// get node count:
// starting at the parent, recursively count the nodes of each child subtree
// and add to the total
// honestly probably easier to just keep a tally but tree traversal practice
int get_subtree_count(struct node *current_node) {
  if (current_node == NULL) {
    return 0;
  } else {
    return 1 + get_subtree_count(current_node->left) + get_subtree_count(current_node->right);
  }
}

int get_node_count() {
  return get_subtree_count(new_tree->root);
}

// bfs traversal
void print_levels() {
  int node_count = get_node_count();
  struct node *nodes[node_count];
  int read_index = 0;
  int write_index = 0;
  int size = 0;

  if (new_tree->root == NULL) {
    printf("error: tree is empty\n");
  } else {
    nodes[write_index++] = new_tree->root;
    size++;

    while (size > 0) {
      struct node *current_node = nodes[read_index++];
      size--;

      print_node(current_node);

      if (current_node->left != NULL) {
        nodes[write_index++] = current_node->left;
        size++;
      }

      if (current_node->right != NULL) {
        nodes[write_index++] = current_node->right;
        size++;
      }
    }
  }
}


// is_in_subtree:
// starting at the root,
// compare node->key to key, if they're equal return 1, else check the correct side
// if that side has no more children, key isn't in the tree
int is_in_subtree(int key, struct node *current_node) {
  if (current_node == NULL) {
    return 0;
  } else {
    if (current_node->key == key) {
      return 1;
    } else if (current_node->key > key) {
      return is_in_subtree(key, current_node->left);
    } else if (current_node->key < key) {
      return is_in_subtree(key, current_node->right);
    }
  }
}

int is_in_tree(int key) {
  if (new_tree->root == NULL) {
    return 0;
  } else {
    return is_in_subtree(key, new_tree->root);
  }
}

// max_height:
// compute the height of new_tree->root
// in general, the height of a node is recursively calculated:
// height(node) = 1 + max(height(node->left), height(node->right)), height(NULL) = 0
int get_height_of_subtree(struct node *current_node) {
  if (current_node == NULL) {
    return 0;
  } else {
    int left_height = get_height_of_subtree(current_node->left);
    int right_height = get_height_of_subtree(current_node->right);
    return 1 + ((left_height > right_height) ? left_height : right_height);
  }
}

int get_height() {
  if (new_tree->root == NULL) {
    return 0;
  } else {
    return get_height_of_subtree(new_tree->root);
  }
}

// get_min and get_max:
// starting from the root, go left/right until there are no children left
// once there are no children left, that's the min/max
int get_min_in_subtree(struct node *current_node) {
  if (current_node->left == NULL) {
    return current_node->key;
  } else {
    return get_min_in_subtree(current_node->left);
  }
}

int get_min() {
  if (new_tree->root == NULL) {
    return NULL;
  } else {
    return get_min_in_subtree(new_tree->root);
  }
}

int get_max_in_subtree(struct node *current_node) {
  if (current_node->right == NULL) {
    return current_node->key;
  } else {
    return get_max_in_subtree(current_node->right);
  }
}

int get_max() {
  if (new_tree->root == NULL) {
    return NULL;
  } else {
    return get_max_in_subtree(new_tree->root);
  }
}

// is_binary_search_tree:
// need node->left->key <= node->key, and node->right->key >= node->key
// and both child subtrees are BSTs
int is_binary_search_tree();

// delete_node:
// if the node has no children, unassign its parent's child pointer and free it
// otherwise:
// if the node has a left child, find its predecessor, swap the values, then delete the predecessor
// if the node has a right child, find its successor, swap the values, then delete the successor
struct node *get_successor_node(struct node *current_node) {
  if (current_node->right == NULL) {
    return NULL;
  } else {
    current_node = current_node->right;

    while (current_node->left != NULL) {
      current_node = current_node->left;
    }

    return current_node;
  }
}

struct node *get_predecessor_node(struct node *current_node) {
  if (current_node->left == NULL) {
    return NULL;
  } else {
    current_node = current_node->left;

    while (current_node->right != NULL) {
      current_node = current_node->right;
    }

    return current_node;
  }
}

int delete_node(struct node *current_node) {
  if (current_node->left == NULL && current_node->right == NULL) {
    struct node *parent = current_node->parent;

    if (parent != NULL) {
      if (current_node == parent->left) {
        parent->left = NULL;
      } else if (current_node == parent->right) {
        parent->right = NULL;
      }
    }

    if (current_node == new_tree->root) {
      new_tree->root = current_node->parent;
    }

    free(current_node);
  } else {
    if (current_node->left != NULL) {
      struct node *predecessor = get_predecessor_node(current_node);
      current_node->key = predecessor->key;

      delete_node(predecessor);
    } else if (current_node->right != NULL) {
      struct node *successor = get_successor_node(current_node);
      current_node->key = successor->key;

      delete_node(successor);
    }
  }
}

void delete_tree() {
  while (new_tree->root != NULL) {
    delete_node(new_tree->root);
  }
}

struct node *find_node_in_subtree(int key, struct node *current_node) {
  if (current_node == NULL) {
    return NULL;
  } else if (current_node->key == key) {
    return current_node;
  } else if (current_node->key < key) {
    return find_node_in_subtree(key, current_node->right);
  } else if (current_node->key > key) {
    return find_node_in_subtree(key, current_node->left);
  }
}

struct node *find_node(int key) {
  if (new_tree->root == NULL) {
    return NULL;
  } else {
    return find_node_in_subtree(key, new_tree->root);
  }
}

// delete_value: find the value and delete the corresponding node
void delete_value(int key) {
  if (!is_in_tree(key)) {
    printf("key not found\n");
  } else {
    delete_node(find_node(key));
  }
}

// get_successor, get_predecessor: get next-highest/next-lowest value in the tree after key, -1 if none
// get_successor: two cases:
// 1) key < root: then root is a candidate, compare root to the successor from left subtree
// 2) key >= root: then -1 is a candidate, compare to the successor from right subtree
// general recursive case:
// passing a previous successor candidate + key,
// 0) if current is null, then return candidate
// 1) if current <= key, then go right; if current > key, then update the candidate and go left
int get_successor_in_subtree(int key, int candidate, struct node *current_node) {
  if (current_node == NULL) {
    return candidate;
  } else {
    if (current_node->key > key) {
      return get_successor_in_subtree(key, current_node->key, current_node->left);
    } else if (current_node->key <= key) {
      return get_successor_in_subtree(key, candidate, current_node->right);
    }
  }
}

int get_successor(int key) {
  if (new_tree->root == NULL) {
    return -1;
  } else {
    return get_successor_in_subtree(key, -1, new_tree->root);
  }
}

// get_predecessor: two cases:
// passing a previous predecessor candidate + key,
// if current <= key, update the candidate and go right
// if current > key, then go left
int get_predecessor_in_subtree(int key, int candidate, struct node *current_node) {
  if (current_node == NULL) {
    return candidate;
  } else {
    if (current_node->key <= key) {
      return get_predecessor_in_subtree(key, current_node->key, current_node->right);
    } else if (current_node->key > key) {
      return get_predecessor_in_subtree(key, candidate, current_node->left);
    }
  }
}

int get_predecessor(int key) {
  if (new_tree->root == NULL) {
    return -1;
  } else {
    return get_predecessor_in_subtree(key, -1, new_tree->root);
  }
}