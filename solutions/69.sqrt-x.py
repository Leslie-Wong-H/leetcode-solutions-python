#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (31.02%)
# Total Accepted:    350K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        # sqrt_dictionary = {81:9, 64:8, 49:7, 36:6, 25:5, 16:4, 9:3, 4:2, 1:1}
        # x_str = str(x)
        # x_length = len(x_str)
        # x_list = list(x_str)
        # remain = 0
        # if x_length % 2 == 1:
        #     if int(x_list[0]) == 9:
        #         quotient = sqrt_dictionary[9]
        #         quo_str = '3'
        #         remain = '0'
        #     elif int(x_list[0]) < 9 and int(x_list[0]) >= 4:
        #         quotient = sqrt_dictionary[4]
        #         quo_str = '2'
        #         remain = str(int(x_list[0]) - 4)
        #     elif int(x_list[0]) <4 and int(x_list[0]) >= 1:
        #         quotient = sqrt_dictionary[1]
        #         quo_str = '1'
        #         remain = str(int(x_list[0]) - 1)
        #     else:
        #         return 0
        #     x_list.pop(0)
        #     x_length -= 1
        # else:
        #     temp_list = [x_list[0],x_list[1]]
        #     temp = int("".join(temp_list))
        #     if temp >= 81 and temp <= 99:
        #         quotient = sqrt_dictionary[81]
        #         quo_str = '9'
        #         remain = str(temp - 81)
        #     elif temp < 81 and temp >= 64:
        #         quotient = sqrt_dictionary[64]
        #         quo_str = '8'
        #         remain = str(temp - 64)
        #     elif temp < 64 and temp >= 49:
        #         quotient = sqrt_dictionary[49]
        #         quo_str = '7'
        #         remain = str(temp - 49)
        #     elif temp < 49 and temp >= 36:
        #         quotient = sqrt_dictionary[36]
        #         quo_str = '6'
        #         remain = str(temp - 36)
        #     elif temp < 36 and temp >= 25:
        #         quotient = sqrt_dictionary[25]
        #         quo_str = '5'
        #         remain = str(temp - 25)
        #     elif temp < 25 and temp >= 16:
        #         quotient = sqrt_dictionary[16]
        #         quo_str = '4'
        #         remain = str(temp -16)
        #     elif temp < 16 and temp >= 10:
        #         quotient = sqrt_dictionary[9]
        #         quo_str = '3'
        #         remain = str(temp - 9)
        #     x_list.pop(0)
        #     x_list.pop(0)
        #     x_length -= 2

        # for index in range(0, x_length, 2):
        #     new_temp_list = [remain, x_list[index], x_list[index + 1]]
        #     dividend = int("".join(new_temp_list))
        #     divider = quotient * 20
        #     # test_number = dividend / divider
        #     # print(test_number)
        #     number = int(dividend / divider)
        #     if number >= 10:
        #         number = 9                
        #     # print(number)
        #     compariment = number * (divider + number)
        #     while compariment > dividend:
        #         number = number - 1
        #         if number < 0:
        #             number = 0
        #         compariment = number * (divider + number)
        #         temp_quotient = number
        #         # print(temp_quotient)
        #         # print(True)
            
        #     temp_quotient = number

        #     remain = str(dividend - compariment)
        #     quo_str_list = list(quo_str)
        #     quo_str_list.append(str(temp_quotient))
        #     quo_str = "".join(quo_str_list)
        #     quotient = int(quo_str)
        
        # return quotient
        if x == 0:
            return 0
        left = 1
        right = 2 * x
        while True:
            mid = left + (right - left) // 2
            if x < mid * mid:
                right = mid - 1

            else:
                if x < (mid + 1) * (mid + 1):
                    return mid
                left = mid + 1
        
    
        

