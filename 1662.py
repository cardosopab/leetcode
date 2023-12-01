from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    w1 = w2 = 0
    c1 = c2 = 0

    while w1 < len(word1) or w2 < len(word2):
        if w1 == len(word1) or w2 == len(word2):
            return False
            
        if word1[w1][c1] != word2[w2][c2]:
            return False

        c1 += 1
        c2 += 1

        if c1 == len(word1[w1]):
            w1 += 1
            c1 = 0

        if c2 == len(word2[w2]):
            w2 += 1
            c2 = 0

    return True


print(arrayStringsAreEqual(["a", "bc"], ["ab", "c"]))  # True

print(arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))  # False

print(arrayStringsAreEqual(["abc", "d", "efg"], ["abcdefg"]))  # True
