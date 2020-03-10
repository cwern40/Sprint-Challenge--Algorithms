#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n^3) The runtime of the while loop doesn't increase by the same integer each time n is increased. It increases by n^3 times.

b)
O(n logn). there is a loop within a loop and each loop increases by n which means that each loop has a runtime of O(n). O(n) * O(n) = O(n^2)

c)
O(n). A recursive function that recurses once each call and by n-1.

## Exercise II

My algorithm would have a variable called max_drop. This will hold the value for the highest floor that would not break an egg. I would set this value to the number of stories in the building. If the eggs were dropped at random floors and assuming the list was unorganized then I would loop through each case and if an egg was broken and that floor - 1 is less then the current value of max_drop then I would set max_drop to that value. I would then return max_drop + 1.
