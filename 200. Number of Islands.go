// Your runtime beats 92.23 % of golang submissions.
// Your memory usage beats 100.00 % of golang submissions.
func numIslands(grid [][]byte) int {
    count := 0 
    for i := 0; i < len(grid); i++{
        for j := 0; j < len(grid[0]); j++{
            if (grid[i][j] == '1'){
                count++
                elim(i,j,grid)
            }
        }
    }
    return count
}
func elim(i int, j int, grid [][]byte){
    grid[i][j] = '0'
    if (i - 1 >= 0 && grid[i-1][j] == '1'){ 
        elim(i - 1, j, grid)
    }
    if (j - 1 >= 0 && grid[i][j-1] == '1'){
        elim(i, j - 1, grid)
    }  
    if (i + 1 < len(grid) && grid[i+1][j] == '1'){
        elim(i + 1,j, grid)
    }   
    if (j + 1 < len(grid[0]) && grid[i][j+1] == '1'){
        elim(i,j + 1, grid)
    }
}
