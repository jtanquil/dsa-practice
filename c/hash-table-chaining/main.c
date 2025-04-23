#include <stdio.h>
#include "hashtable.h"

void main() {
  printf("hash of 'hi' is: %d\n", hash("hi"));

  add("hello", "hi");
  add("hfllo", "test");
  add("hey", "what's up");
  add("hye", "hello");
  add("olleh", "ih");
  add("loelh", "hey");
  add("what is up", "guys");
  add("hi there", "everynyan");
  add("test", "test2");
  add("tset", "test3");
  add("ttes", "test4");
  add("sett", "test5");

  print_hash_table();

  _remove("what is up");
  _remove("idk");
  _remove("sett");
  _remove("olleh");
  _remove("test");

  print_hash_table();
}