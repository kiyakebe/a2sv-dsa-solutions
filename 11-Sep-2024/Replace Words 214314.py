# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def inser(self, word):
        curr = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word):
        replacement = ['']
        curr = self.root
        for ch in word:
            if not curr:
                break
            idx = ord(ch) - 97
            if curr.children[idx]:
                replacement.append(ch)

                if curr.children[idx].is_end:
                    return ''.join(replacement)
            curr = curr.children[idx]

        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.inser(word)
        
        sent = sentence.split()

        for i in range(len(sent)):
            sent[i] = self.search(sent[i])
        
        return " ".join(sent)