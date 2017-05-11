# python3
import math


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        """
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]
        """
        self.buildHeap()

    def parent(self, i):
        return math.floor((i - 1) / 2)

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def shiftUp(self, i):
        while i > 0 and self._data[self.parent(i)] > self._data[i]:
            self._data[self.parent(i)], self._data = self._data, self._data[self.parent(i)]
            i = self.parent(i)

    def shiftDown(self, i, size=None):
        if not size:
            size = len(self._data)
        maxIndex = i
        l = self.leftChild(i)
        if l < size and self._data[l] < self._data[maxIndex]:
            maxIndex = l
        r = self.rightChild(i)
        if r < size and self._data[r] < self._data[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            self._swaps.append((i, maxIndex))
            self._data[i], self._data[maxIndex] = self._data[maxIndex], self._data[i]
            self.shiftDown(maxIndex, size)

    def insert(self, p):
        self._data.append(p)
        self.shiftUp(len(self._data) - 1)

    def buildHeap(self):
        for i in range(math.floor(len(self._data)/2), -1, -1):
            self.shiftDown(i)

    def heapSort(self):
        size = len(self._data) - 1
        for i in range(0, len(self._data) - 1):
            self._swaps.append((0, size))
            self._data[0], self._data[size] = self._data[size], self._data[0]
            size -= 1
            self.shiftDown(0, size=size + 1)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
