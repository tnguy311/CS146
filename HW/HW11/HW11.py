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

# The solution uses a recursive approach to traverse connected pixels starting from the given pixel.
# It defines function dfs, and visits neighboring pixels recursively and changes their color if they match the starting pixel's color.
# The function keeps track of visited pixels to avoid infinite recursion and stops when all connected pixels of the same color are visited.
# If the starting pixel's color is different from the specified color, the function initiates the flood fill operation.
# The function returns the updated image after the flood fill operation.
