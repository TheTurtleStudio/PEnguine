class Math():
    @classmethod
    def SquaredDistance(self, pos1, pos2):
        return ((pos1[0]-pos2[0])**2) + ((pos1[1]-pos2[1])**2)
    @classmethod
    def Distance(self, pos1, pos2):
        return self.SquaredDistance(pos1, pos2)**0.5
    class QuickSort():
        class Regular():
            @classmethod
            def _partition(arr, low, high):
                i = (low-1)
                pivot = arr[high]
                for j in range(low, high):
                    if arr[j] <= pivot:
                        i = i+1
                        arr[i], arr[j] = arr[j], arr[i]
         
                arr[i+1], arr[high] = arr[high], arr[i+1]
                return (i+1)
            @classmethod
            def QuickSort(self, arr, low, high):
                if len(arr) == 1:
                    return arr
                if low < high:
                    pi = self._partition(arr, low, high)
                    self.QuickSort(arr, low, pi-1)
                    self.QuickSort(arr, pi+1, high)
        class LinkedObject(): #Same as the above quicksort class. This one just attaches another list and sorts alongside the first. Used in render function to determine render priority more efficiently.
            @classmethod
            def _partition(self, arr, linkedObjArr, low, high):
                i = (low-1)
                pivot = arr[high]
                for j in range(low, high):
                    if arr[j] <= pivot:
                        i = i+1
                        arr[i], arr[j] = arr[j], arr[i]
                        linkedObjArr[i], linkedObjArr[j] = linkedObjArr[j], linkedObjArr[i]
             
                arr[i+1], arr[high] = arr[high], arr[i+1]
                linkedObjArr[i+1], linkedObjArr[high] = linkedObjArr[high], linkedObjArr[i+1]
                return (i+1)
            @classmethod
            def QuickSort(self, arr, linkedObjArr, low, high):
                if len(arr) == 1:
                    return (arr, linkedObjArr)
                if low < high:
                    pi = self._partition(arr, linkedObjArr, low, high)
                    self.QuickSort(arr, linkedObjArr, low, pi-1)
                    self.QuickSort(arr, linkedObjArr, pi+1, high)
