import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks) * cars * cars


        while left <= right:
            time = (left + right)//2
            repaired = 0

            for rank in ranks:
                repaired +=  int((time / rank) ** 0.5)

            if repaired >= cars:
                right = time - 1
            else:
                left = time + 1

        return left



