"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 



"""



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
      # we'll use a sliding window mechanism here
      
        longest = 0
        myset = set() #doesnt allow duplicates, good for keeping track of them
        l = 0 # left pointer

        for r in range(len(s)): 
            while s[r] in myset:# if a duplicate is found get the length of this current set and check if its the longest substring so far
                longest = max(longest, len(myset))
                myset.remove(s[l]) # this keeps doing the while loop and shrining the window from the left side until the duplicate has finally been deleted 
                l+=1 
            myset.add(s[r]) #expanding the window from the right
            r+=1
        longest = max(longest, len(myset)) # final length check
        return longest
        
