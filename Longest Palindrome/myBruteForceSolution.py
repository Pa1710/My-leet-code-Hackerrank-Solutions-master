class Solution:

    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""
        lowerLimit = len(s)
        upperLimit = 0
        i = 0
        j = len(s)
        while(i <= lowerLimit):
            if j < upperLimit:
                i += 1
                j = len(s)
            temp = s[i:j]
            test = Solution.isPalindrome(temp)
            if test == True:
                if len(longestPalindrome) < len(temp):
                    longestPalindrome = temp
                    lowerLimit = len(s)
                    upperLimit = 0
                    lowerLimit -= len(temp)
                    upperLimit += len(temp)
            j -= 1
            # print(j)

        return longestPalindrome

    def isPalindrome(temp: str):
        return temp == temp[::-1]
