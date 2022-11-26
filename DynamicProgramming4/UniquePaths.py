#TimeComplexity: O(m*n)
#SpaceComplexity: O(1)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prevrow = [1] *n # creating the previous row with 1 as array with length of n

        if m == 1: # if m is equal to 1 then return 1
            return 1

        for i in range(m-1):
            currRow = [1]*n # creating the current row with value 1 with length of n
            for j in range(n-2,-1,-1):
                currRow[j] = currRow[j+1] + prevrow[j] # run until the loop by currRow  with currRow and prevRow

            prevrow = currRow # assigning the current row to prev row

        return currRow[0] # return the 0th value of current row 
