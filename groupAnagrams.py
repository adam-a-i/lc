"""
49. Group Anagrams
Solved
Medium
Topics
premium lock icon
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {} # this hash table will be used to keep track of the words and map them to their respective anagrams, the key will be the sorted anagram and the value will be an array with the original words

        for word in strs: 
            key = "".join(sorted(word)) # this returns a string of the sorted word, we have to use "".join becuase sorted returns the sorted array of individual chars like ['a', .......
            if key not in hash: # if this anagram isnt already in the hashtable we add it
                hash[key] = []
            hash[key].append(word)# add the original word to the respective anagram(key) in the array of other original words
        
        newarr = []

        for anagram in hash: # group the original words from the anagrams(key) into an array 
            newarr.append(hash[anagram]) 
        return newarr
        
