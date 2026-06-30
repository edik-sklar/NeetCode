from collections import deque


def levelOrder(root):
    if not root:
        return []
    else:
        queue = deque([root])
        results = []
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)
    return results

