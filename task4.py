def dfs(tree, root):
    ans = []
    s = []
    visited = [0] * len(tree)

    visited[root - 1] = 1
    s.append(root)

    while len(s) > 0:
        curr = s.pop()
        ans.append(curr)

        for child in tree[curr]:
            if child is not None and visited[child - 1] != 1:
                s.append(child)
    
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

print(dfs(tree, root))