def repeat_optimize(word, times):
    op_str = ""
    for i in range(int(times / 2)):
        op_str = op_str + word

    return op_str + op_str


d = repeat_optimize("test-", 10)
print(d)


Given a nested list of integers, returns the sum of all integers in the list weighted by their depth
For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
"""
def depth_sum(input_list: List[NestedInteger] ):
    pass
 
 
"""
This is the interface that represents nested lists.
You should not implement it, or speculate about its implementation.
"""
class NestedInteger:
    # @return True if this NestedInteger holds a single integer, rather than a nested list
    def is_integer():
        pass
    # @return the single integer that this NestedInteger holds, if it holds a single integer
    # Return None if this NestedInteger holds a nested list
    def get_integer():
        pass
    # @return the nested list that this NestedInteger holds, if it holds a nested list
    # Return None if this NestedInteger holds a single integer
    def get_list():
        pass


This question can be solved by Depth First Search.

Weight sum is level depth times sum. We will go throught the list, 
if the element is digit, we sum up. If element is list, 
we use dfs to get into new depth and go through the new list again. 
The depth is start from 1.

def depthSum(self, nestedList: List[NestedInteger]) -> int:      
        def DFS(nestedList, depth):
            temp_sum = 0
            for elem in nestedList:
                if elem.isInteger():
                    temp_sum += elem.getInteger() * depth
                else:
                    temp_sum += DFS(elem.getList(),depth+1)
            return temp_sum
        return DFS(nestedList,1)
BigO
We traversal all elements of nested list so total time complexity is O(n)

