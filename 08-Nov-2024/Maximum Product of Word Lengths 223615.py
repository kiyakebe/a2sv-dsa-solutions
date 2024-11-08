# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        max_product = 0
        str_mask = defaultdict(int)

        # creating mask for each word
        for i in range(len(words)):
            mask = 0
            for k in words[i]:
                index = ord(k)-97
                mask |= (1 << index)

            for word in str_mask:
                if mask&str_mask[word] == 0:
                    max_product = max(max_product, len(words[i])*len(word))

            str_mask[words[i]] = mask

        return max_product