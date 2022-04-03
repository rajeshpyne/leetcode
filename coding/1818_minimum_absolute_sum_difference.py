"""
You are given two positive integer arrays nums1 and nums2, both of length n.

The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

|x| is defined as:

x if x >= 0, or
-x if x < 0.
 

Example 1:

Input: nums1 = [1,7,5], nums2 = [2,3,5]
Output: 3
Explanation: There are two possible optimal solutions:
- Replace the second element with the first: [1,7,5] => [1,1,5], or
- Replace the second element with the third: [1,7,5] => [1,5,5].
Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.
Example 2:

Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
Output: 0
Explanation: nums1 is equal to nums2 so no replacement is needed. This will result in an 
absolute sum difference of 0.
Example 3:

Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
Output: 20
Explanation: Replace the first element with the second: [1,10,4,4,2,7] => [10,10,4,4,2,7].
This yields an absolute sum difference of |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
 

Constraints:

n == nums1.length
n == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 105
"""

# Filename: 1818_minimum_absolute_sum_difference.py
# Description: https://leetcode.com/problems/minimum-absolute-sum-difference/
# Author: Rajesh Pyne
# Email:  rajesh.pyne@gmail.com

"""
Step 1: Check if the length of both the arrays are same or not. If true, proceed to step 2
Step 2: Calcuate the absolute difference between each elements of each position of the array.
Step 3: Take the highest absolute difference and position number, i of num2 list
        and find the mimimum difference between that num2[i] with all the elements in the num1 list.
Step 4: Replace the num1[j] with the minimum num1 list.

"""


def calculate_total(num1, num2):
    diff_list = [abs(num1[i] - num2[i]) for i in range(len(num1))]

    total = sum(diff_list)

    return diff_list, total


def min_abs_diff(num1, num2):
    if len(num1) != len(num2):
        return False

    diff_list, _ = calculate_total(num1, num2)

    if _ == 0:
        return 0

    max_diff = max(diff_list)
    max_index = diff_list.index(max_diff)

    # print(max_diff, max_index)

    # print(num1[max_index], num2[max_index])

    search_min_diff_list = [abs(num2[max_index] - num1[i]) for i in range(len(num1))]
    get_min_num1_index = search_min_diff_list.index(min(search_min_diff_list))
    # print(search_min_diff_list, get_min_num1_index)

    num1[max_index] = num1[get_min_num1_index]
    # print(num1)

    _, total = calculate_total(num1, num2)
    return total


# num1 = [1, 7, 5]
# num2 = [2, 3, 5]
# num1 = [2, 4, 6, 8, 10]
# num2 = [2, 4, 6, 8, 10]
num1 = [1, 10, 4, 4, 2, 7]
num2 = [9, 3, 5, 1, 7, 4]

abs_sum_diff = min_abs_diff(num1, num2)
print(abs_sum_diff)
