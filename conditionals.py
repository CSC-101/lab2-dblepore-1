def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # never executed
    else:
        return m

first = smallest(3, 2)       # first = 2
second = smallest(2, 2)      # second = 2, this is reasonable, because 2 is not < 2,
print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # this will be evaluated when a is the largest of the three numbers
    elif b > c:
        return b + c             # this will be evaluated when b is the largest number
    else:
        return 2 * c             # this will be evaluated when c is the largest number


answer1 = function2(3, 2, 1)     # answer1 = 3 - 2 = 1
answer2 = function2(2, 3, 1)     # answer2 = 3 + 1 = 4
answer3 = function2(2, 1, 3)     # answer3 = 2 * 3 = 6
print()