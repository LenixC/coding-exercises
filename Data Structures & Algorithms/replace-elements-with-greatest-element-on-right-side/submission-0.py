class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr):
            j = i+1
            max_right = -1
            while j < len(arr):
                if arr[j] > max_right:
                    max_right = arr[j]
                j += 1
            arr[i] = max_right
            i += 1
        
        print(arr)
        return arr
