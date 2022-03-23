from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        visited = set()

        def fourD(coord):
            _matches = []
            r, c = coord
            if r>0:
                if (r-1, c) not in visited and image[r-1][c] == old_color:
                    _matches.append((r-1, c))
                else:
                    visited.add((r-1, c))
            if r<len(image)-1:
                if (r+1, c) not in visited and image[r+1][c] == old_color:
                    _matches.append((r+1, c))
                else:
                    visited.add((r+1, c))
            if c>0:
                if (r, c-1) not in visited and image[r][c-1] == old_color:
                    _matches.append((r, c-1))
                else:
                    visited.add((r, c-1))
            if c<len(image[0])-1:
                if (r, c+1) not in visited and image[r][c+1] == old_color:
                    _matches.append((r, c+1))
                else:
                    visited.add((r, c+1))
            return _matches

        stack = [(sr, sc)]
        matches = {(sr, sc)}
        while stack:
            elem = stack.pop()
            if elem in visited:
                continue
            visited.add(elem)
            _m = fourD(elem)
            stack.extend(_m)
            matches.update(_m)
        
        for (r, c) in matches:
            image[r][c] = newColor
        return image
            
            
print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
