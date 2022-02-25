# """
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# """


# egg = add

# foo != bar

# s = "dad" t = "egg"

# Approach :

# Check 1:
#     take two strings together,
#     split each string.
#     get the distinct characters

#     if check1 is passed, then then check 2

# Check 2:
#     d1 = {1: 'd', 2: 'a', 3: 'd'}
#     d2 = {1: 'e', 2: 'g', 3: 'g'}

#     {'e' : 'a', 'g' : 'd', 'g': 'd'} True

#     {'d' : 'e', 'a' : 'g', 'd' : 'g'} False

# def solution(str1, str2):

#     s1 = set(str1.split())
#     s2 = set(str2.split())

#     if len(s1) == len(s2):
#         d1 = s1.dict()
#         d2 = s2.dict()
#         # d3 = {d1.value : d2.value}
#         processed = []
#         for k1,v1 in d1.items():
#             if v1 not in processed or d3.get(v1) == d2.get(k1):
#                 d3 = {v1 : d2.get(k1)}
#                 processed = processed.append(v1)
#             else:
#                 return False
#     else:
#         return False


def isomorph(a, b):
    print(a, b)
    print([a.index(x) for x in a])
    print([b.index(y) for y in b])
    return [a.index(x) for x in a] == [b.index(y) for y in b]


a = isomorph("egg", "dad")
print(a)
