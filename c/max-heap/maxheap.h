#ifndef MAXHEAP_H
#define MAXHEAP_H

void initialize(void);
void print_heap(void);
int get_size(void);
int is_empty(void);
void insert(int);
int extract_max(void);
int _remove(int);

#endif