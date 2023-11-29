def hammingWeight(n: int) -> int:
    # Leetcode uses the int value of the binary input
    s = str(bin(n)).replace("b", "")
    # s = str(n)
    nList = [int(x) for x in s]
    return sum(nList)


# print(hammingWeight(0b0000000000000000000000000001011))  # 3
print(hammingWeight(11))  # 3
# print(hammingWeight(0b0000000000000000000000010000000))  # 1
print(hammingWeight(128))  # 1
# print(hammingWeight(11111111111111111111111111111101))  # 31
print(hammingWeight(4294967293))  # 31
