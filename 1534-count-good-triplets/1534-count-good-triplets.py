class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0

        for j in range(1, n - 1):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) > b:
                    continue

                for i in range(j):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[i] - arr[k]) <= c:
                        count += 1

        return count