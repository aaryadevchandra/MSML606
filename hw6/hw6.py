import copy
from collections import deque

# BFS solution
def num_islands_bfs(grid):
    if not grid:
        return 0
    
    r = len(grid)
    c = len(grid[0])
    count = 0
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                count += 1
                
                q = deque()
                q.append((i, j))
                grid[i][j] = '0'
                
                while q:
                    x, y = q.popleft()
                    
                    # check 4 dirs
                    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
                    for dx, dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        
                        if nx >= 0 and nx < r and ny >= 0 and ny < c:
                            if grid[nx][ny] == '1':
                                q.append((nx, ny))
                                grid[nx][ny] = '0'  # remove land so we dont count again
    
    return count



# DFS recursive
def num_islands_dfs_rec(grid):
    if not grid:
        return 0
    
    r = len(grid)
    c = len(grid[0])
    
    def dfs(i, j):
        # if out of bound or water then stop
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'  # mark visited
        
        # go all 4 sides (maybe order does not matter)
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    
    count = 0
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    
    return count



# DFS iterative (stack)
def num_islands_dfs_stack(grid):
    if not grid:
        return 0
    
    r = len(grid)
    c = len(grid[0])
    count = 0
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                count += 1
                
                st = []
                st.append((i, j))
                grid[i][j] = '0'
                
                while st:
                    x, y = st.pop()
                    
                    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
                    for dx, dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        
                        if nx >= 0 and nx < r and ny >= 0 and ny < c:
                            if grid[nx][ny] == '1':
                                st.append((nx, ny))
                                grid[nx][ny] = '0'
    
    return count



if __name__ == "__main__":
    
    grid1 = [
        ['1','1','0','0'],
        ['1','0','0','1'],
        ['0','0','1','1']
    ]
    
    
    print(num_islands_bfs(copy.deepcopy(grid1)))
    print(num_islands_dfs_rec(copy.deepcopy(grid1)))
    print(num_islands_dfs_stack(copy.deepcopy(grid1)))
    
    # edge cases
    print(num_islands_bfs([]))  # empty
    print(num_islands_bfs([['0']]))  # all water
    print(num_islands_bfs([['1']]))  # single land