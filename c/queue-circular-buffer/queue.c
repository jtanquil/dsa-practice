// fixed-size circular buffer implementation
#include <stdio.h>
#include <stdlib.h>

// enqueue onto the write_index
// dequeue from the read_index (these are the oldest elements)
// overwrite specifies the behavior if the buffer is full
struct cbuffer {
  int *buffer;
  int capacity;
  int size;
  int read_index;
  int write_index;
  int overwrite;
};

struct cbuffer *initialize(int capacity, int overwrite) {
  struct cbuffer *buf = malloc(sizeof(struct cbuffer));
  buf->buffer = malloc(capacity * sizeof(int));
  buf->capacity = capacity;
  buf->size = 0;
  buf->read_index = 0;
  buf->write_index = 0;
  buf->overwrite = overwrite;

  // fill empty buffer elements with NULL
  for (int i = 0; i < capacity; i++) {
    *(buf->buffer + i) = NULL;
  }

  return buf;
}

int empty(struct cbuffer *buf) {
  return buf->size == 0;
}

int full(struct cbuffer *buf) {
  return buf->size == buf->capacity;
}

int capacity(struct cbuffer *buf) {
  return buf->capacity;
}

int size(struct cbuffer *buf) {
  return buf->size;
}

// enqueue onto the write_index, increment it (mod capacity)
// if overwrite is enabled, then overwrite old entries when the buffer is full
// otherwise, don't write if the buffer is full
void enqueue(struct cbuffer *buf, int item) {
  // in general, overflow condition is when write_index == read_index after ++/mod
  // UNLESS the buffer is empty; in this case just enqueue and increment
  if (empty(buf)) {
    *(buf->buffer + buf->write_index) = item;
    (buf->write_index)++;
    (buf->size)++;

  } else {
    if (buf->write_index != buf->read_index) {
      *(buf->buffer + buf->write_index) = item;
      buf->write_index = (buf->write_index + 1) % buf->capacity;
      (buf->size)++;

    } else {
      if (!buf->overwrite) {
        printf("buffer is full, cannot enqueue %d\n", item);
      } else {
        // if the element at read_index is overwritten, the new oldest element
        // will be the adjacent element, so increment read_index (mod capacity)
        // size remains the same since an element was overwritten
        int old_value = *(buf->buffer + buf->write_index);
        *(buf->buffer + buf->write_index) = item;
        buf->write_index = (buf->write_index + 1) % buf->capacity;
        buf->read_index = (buf->read_index + 1) % buf->capacity;
      }
    }
  }
}

// dequeue from read_index, and increment it (mod capacity)
int dequeue(struct cbuffer *buf) {
  if (empty(buf)) {
    printf("error: buffer is empty\n");
    return NULL;
  } else {
    int item = *(buf->buffer + buf->read_index);
    *(buf->buffer + buf->read_index) = NULL;
    buf->read_index = (buf->read_index + 1) % buf->capacity;

    (buf->size)--;
    return item;
  }
}

void print_buf(struct cbuffer *buf) {
  for (int i = 0; i < buf->capacity; i++) {
    printf("%d ", *(buf->buffer + i));
  }

  printf("\n");
}