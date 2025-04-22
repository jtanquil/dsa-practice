#ifndef HASHTABLE_H
#define HASHTABLE_H

#define TABLE_SIZE 13

struct node {
  char *key;
  char *value;
};

void initialize(void);
int hash(char *, int);
void add(char *, char *);
int exists(char *);
char *get(char *);
int _remove(char *);
void print_hash_table(int);

#endif