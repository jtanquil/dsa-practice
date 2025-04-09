#ifndef QUEUE_H
#define QUEUE_H

struct dlnode {
  int item;
  struct dlnode *next;
  struct dlnode *prev;
};

struct dlist {
  int size;
  struct dlnode *sentinel;
};

struct dlist *initialize(void);
void enqueue(struct dlist *, int);
int dequeue(struct dlist *);
int empty(struct dlist *);
int size(struct dlist *);

#endif