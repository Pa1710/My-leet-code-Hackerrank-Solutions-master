class Solution:

    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxLen = 1

        # print(n)
        for i in range(1, len(s)):
            # print(i)
            lowerLimit = i-1
            upperLimit = i
            while lowerLimit >= 0 and upperLimit < len(s) and s[lowerLimit] == s[upperLimit]:
                #print("in even while")
                if upperLimit - lowerLimit + 1 > maxLen:
                    maxLen = upperLimit - lowerLimit + 1
                    start = lowerLimit
                upperLimit += 1
                lowerLimit -= 1
            lowerLimit = i-1
            upperLimit = i+1
            while lowerLimit >= 0 and upperLimit < len(s) and s[lowerLimit] == s[upperLimit]:
                #print("in odd while")
                if upperLimit - lowerLimit + 1 > maxLen:
                    maxLen = upperLimit - lowerLimit + 1
                    start = lowerLimit
                upperLimit += 1
                lowerLimit -= 1

        return s[start:start + maxLen]
