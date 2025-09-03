"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

# the main loogic behind this is a sliding window on which you have a hash table whihc oyu will keep coparing to achanging hash table that rpeesents the curent window
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        hash = Counter(p) 
        window = Counter(s[0:len(p)]) #first window
        res = []

        for i in range(len(s) - len(p)): # goes through all windows except the last
            if window == hash: # if window and hash equal add the initial(i) index
                res.append(i)
            window[s[i]] -= 1# shorter window from the left(we remove the value of counting for that ch)
            if window[s[i]] == 0:# if its 0 js remove key for purpose of getting equality to work properly
                del window[s[i]]
            window[s[i + len(p)]] += 1 # expand window by counting the next ch in the window
        if hash == window: #tests the last window
            res.append(len(s)-len(p))
        return res    
