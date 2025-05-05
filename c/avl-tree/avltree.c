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

int get_size() {
  return tree_size;
}

int get_height_skew(struct node *current_node) {
  int left_height = (current_node->left == NULL) ? 0 : current_node->left->height;
  int right_height = (current_node->right == NULL) ? 0 : current_node->right->height;

  return right_height - left_height;
}

void print_node(struct node *current_node) {
  int parent_key = (current_node->parent == NULL) ? NULL : current_node->parent->key;
  int left_key = (current_node->left == NULL) ? NULL : current_node->left->key;
  int right_key = (current_node->right == NULL) ? NULL : current_node->right->key;
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

void initialize() {
  tree = malloc(sizeof(struct avltree));
  tree->root == NULL;
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

      tree_size++;
    } else {
      insert_into_subtree(key, current_node->left);
      int left_height = current_node->left->height;
      int right_height = (current_node->right == NULL) ? 0 : current_node->right->height;
      current_node->height = (left_height > right_height) ? left_height + 1 : right_height + 1;
    }
  } else if (current_node->key <= key) {
    if (current_node->right == NULL) {
      struct node *new_node = create_node(key);
      new_node->parent = current_node;
      current_node->right = new_node;

      if (current_node->left == NULL) {
        current_node->height = 1;
      }

      tree_size++;
    } else {
      insert_into_subtree(key, current_node->right);
      int left_height = (current_node->left == NULL) ? 0 : current_node->left->height;
      int right_height = current_node->right->height;
      current_node->height = (left_height > right_height) ? left_height + 1 : right_height + 1;
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
        // if one side of a node has no subtree its contribution to the height of the node is 0,
        // so the height of the empty subtree itself is 0 - 1 = -1
        int left_height = (current_ancestor->left == NULL) ? -1 : current_ancestor->left->height;
        int right_height = (current_ancestor->right == NULL) ? -1 : current_ancestor->right->height;

        current_ancestor->height = (left_height > right_height) ? left_height + 1 : right_height + 1;
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