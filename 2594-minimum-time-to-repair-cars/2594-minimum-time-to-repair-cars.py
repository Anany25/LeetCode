class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks) * cars * cars
        mini = right

        while left <= right:
            time = (left + right)//2
            repaired = 0

            for rank in ranks:
                repaired +=  int((time / rank) ** 0.5)

            if repaired >= cars:
                mini = min(mini, time)
                right = time -1
            else:
                left = time + 1

        return mini



