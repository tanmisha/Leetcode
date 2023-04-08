class Solution {
    public int diagonalSum(int[][] mat) 
    {
     int c=0,i,j,a=mat.length;
        for(i=0;i<mat.length;i++)
        {
            for(j=0;j<mat[i].length;j++)
            {
                if(i==j||(i+j)==mat.length-1)
                    c+=mat[i][j];
            }
        }