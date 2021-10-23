class mySolution {
    private int height,width;
    private int[][] dir = {{-1,0},{1,0},{0,-1},{0,1}};
    public int numIslands(char[][] grid) {
        height = grid.length;
        width = grid[0].length;
        int count = 0;
        for(int i = 0; i < height; ++i){
            for(int j = 0; j < width; ++j){
                if(grid[i][j] == '1'){
                    count+= drownNeighbours(grid,i,j);
                }
            }
        }
        return count;
       
    }
    private int drownNeighbours(char[][] grid, int i, int j){
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] == '0' ){                       
            return 0;          
        }
        grid[i][j]= '0';
        drownNeighbours(grid, i-1, j);     
        drownNeighbours(grid, i+1, j);
        drownNeighbours(grid, i, j-1);
        drownNeighbours(grid, i, j+1);
        return 1;
    }
    
    
}