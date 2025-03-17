import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks) * cars * cars

        def can_repaire(time: int):
            total = 0
            for rank in ranks:
                total += math.isqrt(time//rank)  
                if total >= cars: 
                    return True
            return total >= cars

        while left <= right:
            time = (left + right)//2
            if can_repaire(time):
                right = time - 1
            else:
                left = time + 1

        return left



