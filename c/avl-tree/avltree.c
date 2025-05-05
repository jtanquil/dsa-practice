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

void print_node(struct node *current_node) {
  int parent_key = (current_node->parent == NULL) ? NULL : current_node->parent->key;
  int left_key = (current_node->left == NULL) ? NULL : current_node->left->key;
  int right_key = (current_node->right == NULL) ? NULL : current_node->right->key;
  printf("key: %d, height: %d, parent: %d, left: %d, right: %d\n", current_node->key, current_node->height, parent_key, left_key, right_key);
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