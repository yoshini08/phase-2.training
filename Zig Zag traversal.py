class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        res = []
        level = 0
        
        while queue:
            n = len(queue)
            sub = []
            for i in range(n):
                curr = queue.pop(0)
                sub.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level % 2 != 0:
                sub.reverse()
            res.append(sub)
            level += 1
        
        return res
