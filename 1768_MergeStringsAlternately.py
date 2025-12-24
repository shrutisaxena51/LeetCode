class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len_w1=len(word1)
        len_w2=len(word2)
        i=0
        j=0
        merged=""
        while (i <len_w1 and j<len_w2):
        
            merged += word1[i]+ word2[j]
            i +=1
            j +=1
        
        if (i< len_w1):merged +=word1[i:]
        if (j< len_w2):merged +=word2[j:]
        return merged
        
