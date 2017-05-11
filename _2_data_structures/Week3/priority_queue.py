import math


class PriorityQueue:
    def __init__(self, size, data, priorities):
        self._size = size
        self._max_size = self._size
        self._data = data   # ype: list
        self._priorities = priorities   # type: list

    @classmethod
    def from_data(cls, data):
        return cls(len(data), data, data)

    @staticmethod
    def parent(i):
        return math.floor((i - 1) / 2)

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    def value(self, i):
        return self._priorities[i]

    def swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._priorities[i], self._priorities[j] = self._priorities[j], self._priorities[i]

    def shift_up(self, i):
        while i > 0 and self.value(self.parent(i)) > self.value(i):
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def shift_down(self, i):
        low_index = i
        l = self.left_child(i)
        if l < self._size and self.value(l) < self.value(low_index):
            low_index = l
        r = self.left_child(i)
        if r < self._size and self.value(r) < self.value(low_index):
            low_index = r
        if i != low_index:
            self.swap(i, low_index)
            self.shift_down(low_index)

    def insert(self, element, priority):
        if self._max_size == self._size:
            raise Exception
        self._data[self._size] = element
        self._priorities[self._size] = priority
        self.shift_up(self._size)
        self._size += 1

    def extract_max(self):
        result = self._data[0]
        self.swap(0, self._size - 1)
        self._size -= 1
        self.shift_down(0)
        return result
