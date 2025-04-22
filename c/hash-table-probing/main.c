#include <stdio.h>
#include <stdlib.h>
#include "hashtable.h"

void main() {
  initialize();

  printf("testing: hash of %s is %d\n", "hi", hash("hi", 0));

  add("hi", "hello");
  add("hello", "what's up");

  printf("table['hi'] exists: %d, table['hello'] exists: %d\n", exists("hi"), exists("hello"));

  print_hash_table(0);

  _remove("hi");
  
  printf("table['hi'] exists: %d\n", exists("hi"));

  _remove("hi");

  add("oellh", "everynyan");
  add("llohe", "test");
  add("lelho", "hi");

  print_hash_table(0);

  _remove("hello");
  printf("removed 'hello'\n");

  printf("table['hello'] exists: %d\n", exists("hello"));
  printf("table['elloh'] exists: %d\n", exists("oellh"));
  printf("table['llohe'] exists: %d\n", exists("llohe"));

  print_hash_table(0);

  _remove("llohe");
  printf("removed 'llohe'\n");

  print_hash_table(0);

  printf("table['hello'] exists: %d\n", exists("hello"));
  printf("table['elloh'] exists: %d\n", exists("oellh"));
  printf("table['llohe'] exists: %d\n", exists("llohe"));

  _remove("oellh");

  print_hash_table(0);

  print_hash_table(0);
}