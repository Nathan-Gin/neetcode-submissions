class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return 0

        start = 0
        current_max = 1
        #char : index
        seen = {}
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                start = seen[s[i]] + 1
            seen[s[i]] = i
            if i - start + 1> current_max:
                current_max = i - start + 1

        return current_max