# Trick with using Stack is
* Using same kind of fact that each element can share the same "answer". Hence, improve the time complexity
  * This process of storing elements and then walking back through them matches the behavior of a stack
  * So,  we can "delay" finding the answer for number of iterations, and upon finding a "answer", we can move backward to answer for
    all iterations at the same time

```
Monotonic stacks are a good option when a problem involves comparing the size of numeric elements, with their order being relevant.
```