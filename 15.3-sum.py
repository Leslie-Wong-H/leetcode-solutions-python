#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Create dictionary to count the time apeared of each element
        temp_dict = {}
        for num in nums:
            temp_dict[num] = temp_dict.get(num, 0) + 1

        # Seperate negative elements and positive elements
        negative = sorted(filter(lambda key: key < 0, temp_dict))
        positive = sorted(filter(lambda key: key > 0, temp_dict))

        # Check whether more than 3 zeros exist
        if 0 in temp_dict and temp_dict[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []
        
        # Cut into two situation, two same and all unique, e.g. [-1,-1,2], [-1, 0, 1]
        for i in negative:
            for j in positive:
                diff = -i - j
                if diff in temp_dict:
                    # two same
                    if diff in (i, j) and temp_dict[diff] > 1:
                        res.append([i, diff, j])
                    # all unique, and to prevent duplicate, use big endian
                    elif i < diff and diff< j:
                        res.append([i, diff, j])

        # To fit the permutation requirement of leetcode test program
        return sorted(res, key=lambda x: (x[0], x[1], x[2]))
        


        
        

