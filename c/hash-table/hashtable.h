#ifndef HASHTABLE_H
#define HASHTABLE_H

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

#endif