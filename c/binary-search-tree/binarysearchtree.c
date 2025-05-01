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
int get_min();
int get_max();

// is_binary_search_tree:
// need node->left->key <= node->key, and node->right->key >= node->key
// and both child subtrees are BSTs
int is_binary_search_tree();

// delete_node:
// if the node has no children, unassign its parent's child pointer and free it
//
int delete_note(struct node *current_node);

// delete_value: find the value and delete the corresponding node
int delete_value(int key);