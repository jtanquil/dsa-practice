#include <stdio.h>
#include "hashtable.h"

void main() {
  initialize();

  printf("testing: hash of %s is %d\n", "hi", hash("hi", 101));

  add("hi", "hello");
  add("hello", "what's up");

  printf("table['hi'] exists: %d, table['hello'] exists: %d\n", exists("hi"), exists("hello"));

  _remove("hi");
  
  printf("table['hi'] exists: %d\n", exists("hi"));

  _remove("hi");

  add("oellh", "everynyan");
  add("llohe", "test");

  printf("table['hello']: %s\n", get("hello"));
  printf("table['oellh']: %s\n", get("oellh"));
  printf("table['llohe']: %s\n", get("llohe"));

  _remove("hello");
  printf("removed 'hello'\n");

  printf("table['hello'] exists: %d\n", exists("hello"));
  printf("table['elloh'] exists: %d\n", exists("oellh"));
  printf("table['llohe'] exists: %d\n", exists("llohe"));

  _remove("llohe");
  printf("removed 'llohe'\n");

  printf("table['hello'] exists: %d\n", exists("hello"));
  printf("table['elloh'] exists: %d\n", exists("oellh"));
  printf("table['llohe'] exists: %d\n", exists("llohe"));
}