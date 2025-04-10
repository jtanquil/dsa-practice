#### Algorithmic Complexity of Fixed Circular Buffer Queue

`enqueue`: this is O(1) because it is possible to keep track of the current index to write to, and enqueueing an element is just reassigning the value at a pointer offset.

`dequeue`: this is O(1) for a similar reason; it is possible to keep track of the current index to read from, and dequeueing an element is just returning the value from a pointer offset and setting the value at that address to `NULL`.

`empty`: this is O(1) because it is possible to keep track of the buffer's size by updating a variable whenever an element is enqueued or dequeued.