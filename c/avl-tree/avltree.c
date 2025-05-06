#include <stdio.h>
#include <stdlib.h>

struct node {
  int key;
  int height;
  struct node *left;
  struct node *right;
  struct node *parent;
};

struct avltree {
  struct node *root;
};

static struct avltree *tree;
static int tree_size = 0;

struct node *create_node(int key) {
  struct node *new_node = malloc(sizeof(struct node));
  new_node->key = key;
  new_node->height = 0;
  new_node->left = NULL;
  new_node->right = NULL;
  new_node->parent = NULL;

  return new_node;
}

void initialize() {
  tree = malloc(sizeof(struct avltree));
  tree->root == NULL;
}

int get_size() {
  return tree_size;
}

int get_height(struct node *current_node) {
  // if one side of a node has no subtree its contribution to the height of the node is 0,
  // so the height of the empty subtree itself is 0 - 1 = -1
  int left_height = (current_node->left == NULL) ? -1 : current_node->left->height;
  int right_height = (current_node->right == NULL) ? -1 : current_node->right->height;

  return (left_height > right_height) ? left_height + 1 : right_height + 1;
}

int get_height_skew(struct node *current_node) {
  int left_height = (current_node->left == NULL) ? -1 : current_node->left->height;
  int right_height = (current_node->right == NULL) ? -1 : current_node->right->height;

  return right_height - left_height;
}

void print_node(struct node *current_node) {
  int parent_key = (current_node->parent == NULL) ? -1 : current_node->parent->key;
  int left_key = (current_node->left == NULL) ? -1 : current_node->left->key;
  int right_key = (current_node->right == NULL) ? -1 : current_node->right->key;
  printf("key: %d, height: %d, skew: %d, parent: %d, left: %d, right: %d\n", current_node->key, current_node->height, get_height_skew(current_node), parent_key, left_key, right_key);
}

void print_subtree(struct node *current_node) {
  if (current_node != NULL) {
    print_subtree(current_node->left);
    print_node(current_node);
    print_subtree(current_node->right);
  }
}

void print_tree() {
  if (tree->root == NULL) {
    printf("tree is empty\n");
  }
  printf("printing in traversal order:\n");
  print_subtree(tree->root);
}

void print_levels() {
  struct node *node_queue[tree_size];
  int queue_size = 0;
  int read_index = 0;
  int write_index = 0;

  if (tree->root == NULL) {
    printf("error: tree is empty\n");
  } else {
    printf("printing by level:\n");
    node_queue[write_index++] = tree->root;
    queue_size++;

    while (queue_size > 0) {
      struct node *current_node = node_queue[read_index++];
      queue_size--;

      print_node(current_node);

      if (current_node->left != NULL) {
        node_queue[write_index++] = current_node->left;
        queue_size++;
      }

      if (current_node->right != NULL) {
        node_queue[write_index++] = current_node->right;
        queue_size++;
      }
    }
  }
}

// rotate, then update height of rotated current_node and rotated child
// assumes current_node->left exists
void right_rotate(struct node *current_node) {
  struct node *current_ancestor = current_node->parent;
  struct node *left_child = current_node->left;

  if (current_ancestor != NULL && current_ancestor->left == current_node) {
    current_ancestor->left = left_child;
  } else if (current_ancestor != NULL && current_ancestor->right == current_node) {
    current_ancestor->right = left_child;
  } else { // otherwise, the current node is the current root, and the rotated child is the new root
    tree->root = left_child;
    left_child->parent = NULL;
  }

  struct node *left_right_subtree = left_child->right;
  left_child->right = current_node;
  current_node->parent = left_child;
  current_node->left = left_right_subtree;

  if (left_right_subtree != NULL) {
    left_right_subtree->parent = current_node;
  }

  current_node->height = get_height(current_node);
  left_child->height = get_height(left_child);

  print_node(current_node);
  print_node(left_child);
  if (left_right_subtree != NULL) {
    print_node(left_right_subtree);
  }
}

// assumes current_node->right exists
void left_rotate(struct node *current_node) {
  struct node *current_ancestor = current_node->parent;
  struct node *right_child = current_node->right;

  if (current_ancestor != NULL && current_ancestor->left == current_node) {
    current_ancestor->left = right_child;
  } else if (current_ancestor != NULL && current_ancestor->right == current_node) {
    current_ancestor->right = right_child;
  } else { // otherwise, the current node is the current root, and the rotated child is the new root
    tree->root = right_child;
    right_child->parent = NULL;
  }

  struct node *right_left_subtree = right_child->left;
  right_child->left = current_node;
  current_node->parent = right_child;
  current_node->right = right_left_subtree;

  if (right_left_subtree != NULL) {
    right_left_subtree->parent = current_node;
  }

  current_node->height = get_height(current_node);
  right_child->height = get_height(right_child);

  print_node(current_node);
  print_node(right_child);
  if (right_left_subtree != NULL) {
    print_node(right_left_subtree);
  }
}

void rebalance(struct node *current_node) {
  if (get_height_skew(current_node) < -1) {
    struct node *left_child = current_node->left;

    if (get_height_skew(left_child) == 1) {
      left_rotate(left_child);
    }

    right_rotate(current_node);
  } else if (get_height_skew(current_node) > 1) {
    struct node *right_child = current_node->right;

    if (get_height_skew(right_child) == -1) {
      right_rotate(right_child);
    }
      
    left_rotate(current_node);
  }
}

// recursively insert element into current_node's subtree
// then update the height of the inserted node's ancestors
void insert_into_subtree(int key, struct node *current_node) {
  if (current_node->key > key) {
    if (current_node->left == NULL) {
      struct node *new_node = create_node(key);
      new_node->parent = current_node;
      current_node->left = new_node;

      if (current_node->right == NULL) {
        current_node->height = 1;
      }

      if (get_height_skew(current_node) < -1 || get_height_skew(current_node) > 1) {
        rebalance(current_node);
      }

      tree_size++;
    } else {
      insert_into_subtree(key, current_node->left);
      
      if (get_height_skew(current_node) < -1 || get_height_skew(current_node) > 1) {
        rebalance(current_node);
      }

      current_node->height = get_height(current_node);
    }
  } else if (current_node->key <= key) {
    if (current_node->right == NULL) {
      struct node *new_node = create_node(key);
      new_node->parent = current_node;
      current_node->right = new_node;

      if (current_node->left == NULL) {
        current_node->height = 1;
      }

      if (get_height_skew(current_node) < -1 || get_height_skew(current_node) > 1) {
        rebalance(current_node);
      }

      tree_size++;
    } else {
      insert_into_subtree(key, current_node->right);

      if (get_height_skew(current_node) < -1 || get_height_skew(current_node) > 1) {
        rebalance(current_node);
      }

      current_node->height = get_height(current_node);
    }
  }
}

void insert(int key) {
  if (tree->root == NULL) {
    tree->root = create_node(key);
    tree_size++;
  } else {
    insert_into_subtree(key, tree->root);
  }
}

// recursively search the tree for key
struct node *find_in_subtree(int key, struct node *current_node) {
  if (current_node == NULL) {
    return NULL;
  } else if (current_node->key == key) {
    return current_node;
  } else if (current_node->key > key) {
    return find_in_subtree(key, current_node->left);
  } else if (current_node->key < key) {
    return find_in_subtree(key, current_node->right);
  }
}

struct node *find(int key) {
  if (tree->root == NULL) {
    printf("error: tree is empty\n");
    return NULL;
  } else {
    return find_in_subtree(key, tree->root);
  }
}

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

// deletes node w/corresponding key from the tree; assuming key is in the tree, 3 cases:
// 1. node has no children. then set node->parent->(left/right) = NULL, deallocate node,
//    update height of ancestors
// 2. node has a left child. then set node->key = predecessor->key, delete predecessor 
//    (update predecessor's ancestors)
// 3. node has a right child. then set node->key = successor->key, delete successor 
//    (update successor's ancestors)
void delete_node(struct node *current_node) {
  if (current_node == NULL) {
    printf("node could not be found\n");
  } else {
    if (current_node->left == NULL && current_node->right == NULL) {
      struct node *current_ancestor = current_node->parent;

      if (current_ancestor != NULL && current_ancestor->left == current_node) {
        current_ancestor->left = NULL;
      } else if (current_ancestor != NULL && current_ancestor->right == current_node) {
        current_ancestor->right = NULL;
      }

      free(current_node);
      tree_size--;

      while (current_ancestor != NULL) {
        current_ancestor->height = get_height(current_ancestor);
        current_ancestor = current_ancestor->parent;
      }
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
}

void delete_value(int key) {
  if (tree->root == NULL) {
    printf("error: tree is empty\n");
  } else {
    delete_node(find(key));
  }
}