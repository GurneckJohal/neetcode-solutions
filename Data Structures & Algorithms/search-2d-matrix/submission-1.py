class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_low = 0
        row_high = len(matrix) - 1

        while(row_low <= row_high):
            row = (row_high + row_low) // 2
            if target < matrix[row][0]:
                row_high = row - 1
            elif target > matrix[row][len(matrix[row]) - 1]:
                row_low = row + 1
            else:
                l = 0
                r = len(matrix[row]) - 1
                while l <= r:
                    mid = (r + l) // 2
                    if target < matrix[row][mid]:
                        r = mid - 1
                    elif target > matrix[row][mid]:
                        l = mid + 1
                    else:
                        return True
                return False
        return False

                