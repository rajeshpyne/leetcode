"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], 
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""


def reverse(x):
    flag = True if x < 0 else False

    temp = abs(x)
    f = 0
    while temp > 0:
        f = f * 10 + temp % 10
        temp //= 10

    # Constraints
    if f >= 2 ** 31 - 1 or f <= -(2 ** 31):
        return 0

    return -f if flag else f


x = reverse(123)
assert x == 321, "Output not matching"
x = reverse(-123)
assert x == -321, "Output not matching"
x = reverse(120)
assert x == 21, "Output not matching"
x = reverse(2147483648)
assert x == 0, "Output not matching"
x = reverse(-2147483648)
assert x == 0, "Output not matching"
x = reverse(1534236469)
assert x == 0, "Output not matching"

print("All test cases passed")
