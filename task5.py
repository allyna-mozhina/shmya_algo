from collections import deque

def bfs(tree, root):
    ans = []
    q = deque()
    visited = [0] * len(tree)

    visited[root - 1] = 1
    q.append(root)

    while len(q) != 0:
        curr = q.popleft()
        ans.append(curr)

        for child in tree[curr]:
            if child is not None and visited[child - 1] != 1:
                q.append(child)

    return ans 


tree = {
    1: [2, 7],
    2: [3, 4],
    3: [None, None],
    4: [5, None],
    5: [None, None],
    6: [None, None],
    7: [None, 9],
    8: [None, None],
    9: [None, None]
}
root = 1

print(bfs(tree, root))