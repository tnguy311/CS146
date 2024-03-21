public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
    int color = image[sr][sc];
    if (color != newColor) {
        dfs(image, sr, sc, color, newColor);
    }
    return image;
}

private void dfs(int[][] image, int sr, int sc, int color, int newColor) {
    if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length || image[sr][sc] != color) {
        return;
    }
    image[sr][sc] = newColor;
    dfs(image, sr + 1, sc, color, newColor);
    dfs(image, sr - 1, sc, color, newColor);
    dfs(image, sr, sc + 1, color, newColor);
    dfs(image, sr, sc - 1, color, newColor);
}

// The solution uses a recursive approach Depth-First Search (DFS) to traverse the connected pixels starting from the given pixel.
// It defines a method called dfs that recursively visits neighboring pixels and updates their color if they match the starting pixel's color.
// The process continues until all connected pixels of the same color are visited.
// If the starting pixel's color is different from the specified color, the floodFill method initiates the DFS to perform the flood fill operation.
// The modified image is returned after the flood fill operation.
