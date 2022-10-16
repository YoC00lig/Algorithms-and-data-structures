class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.max = 0

class Solution:
    def _build(self, left, right):
        root = SegmentTreeNode(self.coords[left], self.coords[right])
        if left == right: return root
        mid = (left + right) // 2
        root.left = self._build(left, mid)
        root.right = self._build(mid + 1, right)
        return root

    def _update(self, root, lower, upper, val):
        if root is not None and lower <= root.high and root.low <= upper:  # intersect
            root.max = val
            self._update(root.left, lower, upper, val)
            self._update(root.right, lower, upper, val)

    def _query(self, root, lower, upper):
        if lower <= root.low and root.high <= upper: return root.max
        if upper < root.low or root.high < lower or lower > upper: return 0
        return max(self._query(root.left, lower, upper), self._query(root.right, lower, upper))

    def fallingSquares(self, positions):
        brick_size = 1
        coords = set()
        for left, right in positions:
            coords.add(left)
            coords.add(right)
        self.coords = sorted(list(coords))
        root = self._build(0, len(self.coords) - 1)

        res = []
        for left, right in positions:
            h = self._query(root, left, right) + brick_size
            res.append(max(res[-1], h)) if res else res.append(h)
            self._update(root, left, right, h)
        print(res)
        return max(res)

positions =  [(7, 9), (5, 8), (0, 3), (5, 7), (2, 8), (4, 9)]
x = Solution()
a = x.fallingSquares(positions)
print(a)

def FallingBrick(bricks):
    x = Solution()
    a = x.fallingSquares(bricks)
    return a

