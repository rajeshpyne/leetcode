"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
"""

def majority_element(nums):
    len_list = len(nums)
    if len_list < 1 or len_list > 5 * 10000:
        return False
    dict = {}
    for j in nums:
        if j in dict:
            # val = dict.get(j)
            dict.update({j : dict.get(j)+1})
        else:
            dict[j] = 1
    # print(dict)
    threshold = int(len_list/3)
    # print(threshold)
    final = [i for i in dict if dict.get(i) > threshold]
    return final


assert majority_element(nums=[2,3,2]) == [2]
assert majority_element(nums=[1]) == [1]
assert majority_element(nums=[1,2]) == [1,2]
print("All test cases passed")
