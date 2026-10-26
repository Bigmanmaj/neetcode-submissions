class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            largest = self.find_largest(stones)
            stones.pop(largest[1])
            second_largest = self.find_largest(stones)
            stones.pop(second_largest[1])

            smashed_stone = largest[0] - second_largest[0]
            stones.append(smashed_stone)

        if stones:
            return stones[0]
        else:
            return 0

    def find_largest(self, stones):
        largest = -1
        pos = -1
        for i in range(len(stones)):
            if stones[i] > largest:
                largest = stones[i]
                pos = i
        return [largest, pos]
