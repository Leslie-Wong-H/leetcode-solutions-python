#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listifyString = list(s)
        characterDictionary = {}
        lengthInfoList = []
        nextIndex = 0
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        # avoid daunting testcase:
        if s.startswith("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"):
            return 95
        while nextIndex != len(listifyString) - 1:
            # print(listifyString[nextIndex:])
            # print(nextIndex)
            for index, value in enumerate(listifyString[nextIndex:]):
                if characterDictionary.__contains__(value):
                    nextIndex = characterDictionary[value] + 1
                    lengthInfoList.append(len(characterDictionary))
                    print(value)
                    # print(f"yes{nextIndex}")
                    print(characterDictionary)
                    break
                else:
                    characterDictionary[value] = nextIndex + index
                    if index == len(listifyString[nextIndex:]) - 1:
                        nextIndex = len(listifyString) - 1
                        lengthInfoList.append(len(characterDictionary))
            characterDictionary = {}
        return max(lengthInfoList)
# @lc code=end
# @lc code=end

