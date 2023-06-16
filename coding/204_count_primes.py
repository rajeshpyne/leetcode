"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

"""
"""
Approach

1. iterate until the last digit of input from 1
2. check each number whether it is a prime number or not

"""
from math import sqrt

class Solution:

    def checkPrime(self, n:int ) -> bool:
        threshold = int(sqrt(n))
        # print(threshold)
        for i in range(2, threshold+1):
            # print(n , i)
            if n % i == 0:
                # print("Not Prime")
                return False
        # print(n)
        return True


    def countPrimes(self, n: int) -> int:
        if n >= 0 or n <= (5 * pow(10,6)):
            
            count = 0
            for i in range(2, n): 
                if self.checkPrime(i) == True:
                    count += 1

            return count


if __name__ == '__main__':
    s = Solution()
    # print(s.checkPrime(5))
    print(s.countPrimes(1500000))