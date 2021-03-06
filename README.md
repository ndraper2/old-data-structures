# data-structures
Contains a number of classic data structures, implemented in python.
This file contains:
Singly linked list
    Data structure utilizing nodes
    References for list:
    http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python for the attempt at using unicode strings.
Stack
    Data structure utilizing nodes with a "First In, Last Out" 
    organization.
    contains two constructors, one for the data node, and one
    for the stack itself. 
    The stack contains a reference to the first data node, and that
    is all. 
    A node contains a data value, along with a reference to the next
    node.
Queue 
    Data structure that push values into the back of list, then spits
    them out of the front, in the order they were pushed.
    Enqueue adds nodes to the back of the list
    dequeue pops nodes off the top of the list
    size checks the length of the queue
Doubly-Linked Lists
    Same deal as a Linked list, except the nodes carry values for the nodes
    ahead and behind them in the list. Also has methods for adding/removing
    from both ends of the list.
    Doubly linked lists take up a bit more space in memory, but allow
    for more flexibilty than a singly-linked list. I guess it's a matter
    of space over speed: singly-linked lists take less space, but more
    time to perform operations, and the flip is true for doubly-linked 
    lists.
Binary Heap
    A binary heap where each value in the list has two children that are guaranteed to be less than the node.
    Resources: http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
Graph
    A graph of nodes where each node can be connected to any other node.
    Note - node values must be immutable.
    Graph traversal resource: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
Collaborations: Robert Haskell & Nick Draper (coders)
References: Google, Google, Google, and also Wikipedia

[![Build Status](https://travis-ci.org/robertwhaskell/data-structures.svg?branch=weighted-graph)](https://travis-ci.org/robertwhaskell/data-structures)
    