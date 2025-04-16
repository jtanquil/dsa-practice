#ifndef HASHTABLE_H
#define HASHTABLE_H

void initialize(void);
int hash(char *);
void add(char *, char *);
int exists(char *);
char *get(char *);
void _remove(char *);
void print_hash_table(void);

#endif