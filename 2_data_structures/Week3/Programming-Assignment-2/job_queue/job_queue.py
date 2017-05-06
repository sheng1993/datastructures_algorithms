# python3
import math


class PriorityQueue:
    def __init__(self, size, data, priorities):
        self._size = size
        self._max_size = self._size
        self._data = data   # ype: list
        self._priorities = priorities   # type: list

    @classmethod
    def from_data(cls, data):
        return cls(len(data), data, [0 for x in range(len(data))])

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
        if l < self._size and (self.value(l) < self.value(low_index)
                               or (self.value(l) == self.value(low_index) and self._data[l] < self._data[low_index])):
            low_index = l
        r = self.right_child(i)
        if r < self._size and (self.value(r) < self.value(low_index)
                               or (self.value(r) == self.value(low_index) and self._data[r] < self._data[low_index])):
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

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.workers = PriorityQueue.from_data([x for x in range(self.num_workers)])    # type PriorityQueue
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        """for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]"""

        for i in range(len(self.jobs)):
            next_worker = self.workers.extract_max()
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] = next_free_time[next_worker] + self.jobs[i]
            self.workers.insert(next_worker, next_free_time[next_worker])



    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

