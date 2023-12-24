class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        sorted_words = sorted(words, key=lambda word: [order.index(char) for char in word])

        for i in range(len(words)):
            if sorted_words[i] != words[i]:
                return False
                break
        else:
            return True
