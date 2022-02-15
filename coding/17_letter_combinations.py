"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

# Filename: 17_letter_combinations.py
# Description: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Author: Rajesh Pyne
# Email:  rajesh.pyne@gmail.com

from ntpath import join

from black import out
from helper_lib import BusinessService
import time
from itertools import product


class LetterCombination(BusinessService):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.input = kwargs["digits"]

    def calculate(self, *args, **kwargs):
        self.input = kwargs["digits"]
        phone_dictionary = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        dig_list = [
            phone_dictionary.get(int(i))
            for i in self.input
            if int(i) > 1 and int(i) < 10
        ]

        # doing a cartesian product of the lists
        cartesian_prod = list(product(*dig_list))
        join_list = ["".join(a) for a in cartesian_prod]
        return join_list


if __name__ == "__main__":
    combine = LetterCombination()
    output = combine.calculate(digits="1")
    print(output)

    start_time = time.time()

    # print(
    #     "compute result =",
    #     combine.calculate(digits="2345"),
    #     ", time taken - ",
    #     (time.time() - start_time),
    #     " seconds",
    # )

    # Test Cases
    assert combine.calculate(digits="23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert combine.calculate(digits="") == [""]
    # assert combine.calculate(digits="1") == []

    print("all test case passed")
