class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        r = len(matrix)
        c = len(matrix[0])

        result = []

        top = 0
        bottom = r - 1

        left = 0
        right = c - 1


        while top <= bottom and left <= right:

            # from left to right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            
            top += 1

            # from top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])

            right -= 1

            # from right to left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                
                bottom -= 1

            # from bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])

                left += 1

        return result
     
                

        