class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.bfs(image, sr, sc, color, image[sr][sc])

        return image
    
    def bfs(self, image, sr, sc, color, og_color):
        ROWS = len(image)
        COLS = len(image[0])

        if sr == ROWS or sc == COLS or sr < 0 or sc < 0 or image[sr][sc] != og_color or image[sr][sc] == color:
            return

        image[sr][sc] = color

        self.bfs(image, sr-1,sc, color, og_color)
        self.bfs(image, sr+1, sc, color, og_color)
        self.bfs(image, sr, sc-1, color, og_color)
        self.bfs(image, sr, sc+1, color, og_color)

        return