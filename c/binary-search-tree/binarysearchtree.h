#ifndef BINARYSEARCHTREE_H
#define BINARYSEARCHTREE_H

void initialize(void);
void print_values(void);
void insert(int);
int get_node_count(void);
int is_in_tree(int);
int get_height(void);
int get_min(void);
int get_max(void);
void delete_value(int);
void delete_tree(void);
void print_levels(void);
int get_successor(int);
int get_predecessor(int);

#endif