---
Date: 2023-01-16
Author: AkaCoder404
File Hiearchy: Problems | Easy 
---
# 66-PlusOne

tags: #Easy, #array

## Question

Add one to an integer number stored in array format. 

### Example
```cpp
```

## Thought Process

The key point is to keep track of carry. So we traverse the array from end to beginning, start by adding one to the end. 

If that value results in 10, replace that digit whose sum is equal to 10 with a 0, then the carry value of 1 propagates forward. 

If the carry is still zero after traversing all the numbers, just insert a 1 at the beggining.

## Solution


### Results

### Edge Cases
```
[9] -> [1,0] instead of [10]
[9, 9] -> [1, 0, 0]
```

