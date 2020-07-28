from typing import List

def check(edges: List[int]) -> bool:
    misplaced_index = []
    for i in range(int(len(edges)/2)):
        if edges[2*i] == edges[2*i + 1]:
            continue
        else:
            return False

    return True


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        count = 0

        N = int(len(row)/2)
        n = int(len(row))
        edges = [0 for i in range(n)]

        # Edges
        for x in row:
            for j, y in enumerate(row):
                if x != y and ((x%2 == 0 and y%2 == 1 and y == x+1) or (x%2 == 1 and y%2 == 0 and x == y+1)):
                    edges[x] = int(j/2)
                    break

        if check(edges):
            return 0

        # High-impact swaps
        for i in range(int(len(edges) / 2)):
            for j in range(int(len(edges) / 2)):
                if i != j:
                    a = edges[2*i:2*i+2]
                    b = edges[2*j:2*j+2]
                    a.sort()
                    b.sort()
                    if a == b:
                        if edges[2 * j] != edges[2 * i]:
                            edges[2 * j], edges[2 * i] = edges[2 * i], edges[2 * j]
                        else:
                            edges[2 * j + 1], edges[2 * i] = edges[2 * i], edges[2 * j + 1]
                        count += 1
                        break

        if check(edges):
            return count

        # Low-impact swaps
        i = 0
        while i < int(len(edges) / 2):
            for j in range(int(len(edges) / 2)):
                if i != j:
                    a = edges[2*i:2*i+2]
                    b = edges[2*j:2*j+2]
                    if (a[0] == b[0] or a[0] == b[1]):
                        if edges[2 * j] != edges[2 * i]:
                            edges[2 * j], edges[2 * i] = edges[2 * i], edges[2 * j]
                        else:
                            edges[2 * j + 1], edges[2 * i] = edges[2 * i], edges[2 * j + 1]
                        count += 1
                        i = 0
                        break
            i += 1

        return count

s = Solution()
print(s.minSwapsCouples([0,2,4,6,7,1,3,5]))
