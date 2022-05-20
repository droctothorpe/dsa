# The ultimate python coding interview bootcamp notes

[Link](http://www.udemy.com/course/data-structures-algorithms-python) to course.

## Hash tables

Methods or handling collisions:
- Separate chaining
  - Put collisions at the same index / address.
  - Can be lists or linked lists.
- Linear probing (a type of open addressing)
  - Put collisions in the next available index / address.

You should always have a prime number of indexes / addresses because that
increases the randomness of how key values are distributed through the hash
table.
