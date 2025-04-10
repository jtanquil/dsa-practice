#### Algorithmic Complexity of a Doubly Linked List Queue

`enqueue`: enqueueing into the queue is just pushing to the back of a doubly linked list, which is O(1).

`dequeue`: dequeueing from the queue is just popping from the front of a doubly linked list, which is also O(1). 

`empty`: this is O(1) since it is possible to keep track of the size of the list by updating a counter whenever an element is enqueued or dequeued.