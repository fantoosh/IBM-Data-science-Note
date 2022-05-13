# py3
# Write a function that finds the XOR on contiguous subarrays of an array

# XOR has some useful properties that i can exploit to solve ths in O(n) time.
# 1. Xor is associative and commutative
# 2. For  any n: n XOR n == 0
# 3. For any n: n XOR 0 == n

def xor_em(lst):
    n = len(lst)
    output = 0
    for i, element in enumerate(lst):
        count = (i + 1) * (n - i)
        if count % 2:
            output ^= element
    return output

# there are n - i to the right (also including itself) and
# i + 1 elements to the left of the current element (including itself)
# we can get the number of sub arrays to the left and right of the subarry by multipying the two
# finally we precede by reducing the problem to looking for pairs (i + 1) and (n - i) whose product is odd.

print(xor_em([3, 5, 1]))
print(5 ^ 5)
