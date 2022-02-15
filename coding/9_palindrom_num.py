"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

"""
# Filename: 9_palindrom_num.py
# Description: https://leetcode.com/problems/palindrome-number/
# Author: Rajesh Pyne
# Email:  rajesh.pyne@gmail.com

from helper_lib import BusinessService
import time


class Palindrom(BusinessService):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def calculate(self, *args, **kwargs):
        # return super().calculate(*args, **kwargs)
        num = kwargs["input"]
        new_num = 0
        while num > 0:
            r = num % 10
            new_num = new_num * 10 + r
            num //= 10
        if new_num == kwargs["input"]:
            return True
        else:
            return False


if __name__ == "__main__":
    input = 989
    a = Palindrom()
    # a.calculate()

    start_time = time.time()

    print(
        "compute result =",
        a.calculate(input=input),
        ", time taken - ",
        (time.time() - start_time),
        " seconds",
    )

    # Test Cases
    assert a.calculate(input=121) == True
    assert a.calculate(input=1221) == False

    print("all test case passed")
