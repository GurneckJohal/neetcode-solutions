class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()

        self.bfs(image, sr, sc, color, image[sr][sc], visited)

        return image
    
    def bfs(self, image, sr, sc, color, og_color, visited):
        ROWS = len(image)
        COLS = len(image[0])

        if sr == ROWS or sc == COLS or sr < 0 or sc < 0 or image[sr][sc] != og_color or (sr, sc) in visited:
            return


        visited.add((sr, sc))

        self.bfs(image, sr-1,sc, color, og_color, visited)
        self.bfs(image, sr+1, sc, color, og_color, visited)
        self.bfs(image, sr, sc-1, color, og_color, visited)
        self.bfs(image, sr, sc+1, color, og_color, visited)

        image[sr][sc] = color

        return