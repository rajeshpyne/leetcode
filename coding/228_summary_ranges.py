"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""

# Filename: 228_summary_ranges.py
# Description: https://leetcode.com/problems/summary-ranges/
# Author: Rajesh Pyne
# Email:  rajesh.pyne@gmail.com

"""
Prerequisite: if length of the list is > 20, then return False

Step 1: Find out the difference between each element of the list
"""
from typing import final


def summaryRanges(nums):
    # if len(nums)>20:
    #     return False
    
    # nums.sort()
    
    # final_list = (list(set(nums)))
    # print(final_list)
    # diff_list = [final_list[i+1]-final_list[i] for i in range(len(final_list)-1)]
    # print(diff_list)

    # l = [final_list[j] for j in range(len(diff_list)) if diff_list[j] == 1]
    # print(l)

    ranges = []
    print(nums[-1][-1]+1)
    for n in nums:
        
        if not ranges or n > ranges[-1][-1] + 1:
            ranges += [],            
        ranges[-1][1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]


num_list = [0,1,2,4,5,7]
p =summaryRanges(num_list)
print(p)
