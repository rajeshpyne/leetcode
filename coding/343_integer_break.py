"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
"""
# Filename: 343_integer_break.py
# Description: https://leetcode.com/problems/integer-break/
# Author: Rajesh Pyne
# Email:  rajesh.pyne@gmail.com

"""Approach
Divide the number into lowest possible prime numbers.

8 = 3 * 2 * 3
9 = 3 * 2 * 2 * 2
10 = 3 * 2 * 2 * 3
25 = 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 2
"""
def integerBreak(n: int) -> int:
    if n < 2 or n > 58:
        return False
    
    if n > 4:
        if n % 2 == 0:
            factor = (n // 3) - 1
            # print(factor)
            # mul_fact = (3 ** factor)
            return (n-(factor * 3)) * (3 ** factor)
        else:
            factor = n // 3
            # print(factor)
            # mul = 3 ** factor * 2
            return (n - ) * (3 ** factor)
            # return mul
    elif n == 2:
        factor = n // 2
        return factor
    elif n == 3:
        return (n // 2) * 2
    else:
        return n

print(integerBreak(6))

