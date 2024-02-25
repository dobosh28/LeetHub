class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        len1, len2 = len(word1), len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                result.append(word1[i])
            if i < len2:
                result.append(word2[i])
        return ''.join(result)
