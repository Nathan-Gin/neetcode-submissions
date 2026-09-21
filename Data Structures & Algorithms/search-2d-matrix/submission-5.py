class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False

        
        if len(matrix) > 1:
            for r in range(len(matrix)-1):
                if matrix[r][0] == target:
                    return True
                elif matrix[r][0] < target < matrix[r+1][0]:
                    result = self.binarySearch(matrix[r], target)
            if matrix[-1][0] == target:
                return True
            if matrix[-1][0] < target <= matrix[-1][-1]:
                result = self.binarySearch(matrix[-1], target)
        else:
            result = self.binarySearch(matrix[0], target)
            

        return result


    def binarySearch(self, arr, target):
        
        low = 0
        high = len(arr)-1

        while low <= high:
            mid = low + ((high-low) // 2)
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid-1
        return False