def floodFill(self, image, sr, sc, color):
    def dfs(image, sr, sc, color, newColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color:
            return
        image[sr][sc] = newColor
        dfs(image, sr + 1, sc, color, newColor)
        dfs(image, sr - 1, sc, color, newColor)
        dfs(image, sr, sc + 1, color, newColor)
        dfs(image, sr, sc - 1, color, newColor)
    
    if image[sr][sc] != color:
        dfs(image, sr, sc, image[sr][sc], color)
    return image

# The Python solution utilizes a recursive Depth-First Search (DFS) approach to traverse the image pixels connected to the starting pixel.
# It defines a helper function dfs that recursively visits neighboring pixels, updating their color if they match the starting pixel's color.
# The process continues until all connected pixels of the same color are visited.
# If the starting pixel's color is different from the specified color, the function invokes the DFS to perform the flood fill.
# Finally, it returns the modified image after the flood fill operation.
