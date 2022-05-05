"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false
 
Constraints:

1 <= n <= 231 - 1
"""
"""
Approach : 
    1. split a number by remainder division method
    2. square the number and add to the existing squared numbers
    3. continue the process till the result is 1 
"""

class Solution:
    def getSquareNum(self, x:int) -> int:
        sq_num = 0
        while x > 0:
            sq_num += pow(x%10,2)
            x //=10
        return sq_num

    def isHappy(self, n: int) -> bool:
        if n <= 1 and n >= 2^31-1:
            return False
        
        op = 0
        happy_op_list = []

        while op != 1:
            op = self.getSquareNum(n)

            if op in happy_op_list:
                return False
            happy_op_list.append(op)
            
            if op == 1:
                return True
            n = op
           



if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(2))

