"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""

# Filename: 29_divide_two_integers.py
# Description: https://leetcode.com/problems/divide-two-integers/
# Author: Rajesh Pyne
# Email:  rajesh.pyne@gmail.com

from helper_lib import BusinessService
import time


class Solution(BusinessService):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def calculate(self, *args, **kwargs):

        self.dividend = kwargs["dividend"]
        self.divisor = kwargs["divisor"]

        if self.dividend == 0:
            return 0
        elif self.divisor == 0:
            return False
        elif self.dividend == self.divisor:
            return 1
        divisor = -self.divisor if self.divisor < 0 else self.divisor
        n = 0
        count = 0
        temp_div = 0
        dividend = -self.dividend if self.dividend < 0 else self.dividend

        while temp_div < dividend:
            n = n + divisor
            count = count + 1

            temp_div = n
            # print(n, divisor, dividend)
        # return count
        op = -(count - 1) if self.dividend < 0 or self.divisor < 0 else count - 1
        return op
        # return int(self.dividend / self.divisor)


if __name__ == "__main__":
    obj = Solution()
    op = obj.calculate(dividend=0, divisor=-1)
    print(op)
