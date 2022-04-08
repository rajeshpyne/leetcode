"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or 
convert the inputs to integer directly. 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

# Filename: 43_multiply_strings.py
# Description: https://leetcode.com/problems/multiply-strings/
# Author: Rajesh Pyne
# Email:  rajesh.pyne@gmail.com

def formulate_num(n1_list):
    res1=0
    for i, d in enumerate(n1_list[::-1]):
        # print(i,d)
        dig = 0 if d is None else d
        res1 += (dig * 10**i)
    return res1

def multiply(num1: str, num2: str) -> str:
    # print(ord("1"), ord("9"))
    num_dict = {
        ord("1"):1,
        ord("2"):2,
        ord("3"):3,
        ord("4"):4,
        ord("5"):5,
        ord("6"):6,
        ord("7"):7,
        ord("8"):8,
        ord("9"):9
    }
    # print(num_dict)
    if num1 == "0" or num2 == "0":
        return "0"

    if len(num1) > 200 or len(num2) > 200:
        return False

    n1_list = [num_dict.get(ord(i)) for i in num1]
    # print(n1_list)
    # res1 = sum(d * 10**i for i, d in enumerate(n1_list[::-1]))
    # print(res1)
    res1 = formulate_num(n1_list)
    
    n2_list = [num_dict.get(ord(j)) for j in num2]
    # print(n2_list)
    # res2 = sum(d * 10**i for i, d in enumerate(n2_list[::-1]))
    # print(res2)
    res2 = formulate_num(n2_list)

    return str(res1 * res2)

assert multiply("42","3") == "126"
assert multiply("4","5") == "20"
assert multiply("123","456") == "56088"
assert multiply("408","5") == "2040"
print("All Test cases passed")