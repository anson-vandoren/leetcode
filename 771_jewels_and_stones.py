def numJewelsInStones(self, J: str, S: str) -> int:
    return sum([stone in J for stone in list(S)])
