#ifndef QUEUE_H
#define QUEUE_H

struct cbuffer {
  int *buffer;
  int capacity;
  int size;
  int read_index;
  int write_index;
  int overwrite;
};

struct cbuffer *initialize(int, int);
int empty(struct cbuffer *);
int full(struct cbuffer *);
int size(struct cbuffer *);
int capacity(struct cbuffer *);
void enqueue(struct cbuffer *, int);
int dequeue(struct cbuffer *);

#endif