#### Time Complexity of Dynamic Array Implementation

`push`/`pop`: in each case, the call to `insert` or `delete` uses a pointer offset to access the last element of the array, and no shifting of the rest of the array elements is necessary in either case. In both cases it is possible that the array is automatically resized, an operation whose cost is in `O(n)`, but this cost can be amortized across the previous `n` operations (that take constant time); therefore, the amortized time complexity of `push` and `pop` is `O(1)`.

`at`/`update`: both of these also use a pointer offset to access the given `index`, and reassigning the element is also a constant time operation, so these are both `O(1)`

`insert`/`delete`: in general, these operations are `O(n)` because while accessing the element via pointer offset is constant, and the cost of potential array resizing can be amortized like above, it is also necessary to shift the rest of the array to the right (when inserting an element) or to the left (when removing an element); in the worst case, where the element is at the front of the array, this shifting would take `O(n)` time, so this entire operation is in `O(n)`.