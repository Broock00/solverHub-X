class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        i = 0
        j = i+1
        while i < n and j < n:
            if arr[i] > arr[j]:
                return 0
            else:
                i += 1
                j += 1
        return 1
