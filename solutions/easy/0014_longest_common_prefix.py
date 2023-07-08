# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs.pop(0)

        for string in strs:
            prefix = self.common_prefix(prefix, string)

        return prefix

    def common_prefix(self, str1, str2) -> str:
        pos1 = 0
        pos2 = 0

        prefix = ''

        while pos1 < len(str1) and pos2 < len(str2):
            if str1[pos1] == str2[pos1]:
                prefix = prefix + str1[pos1]
            else:
                break

            pos1 += 1
            pos2 += 1

        return prefix
