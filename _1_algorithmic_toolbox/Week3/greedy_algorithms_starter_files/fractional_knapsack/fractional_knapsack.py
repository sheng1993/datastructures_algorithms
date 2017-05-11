# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.

    for n in range(len(values)):
        if capacity == 0:
            return value

        # find the max value/weight
        prev_max = 0
        prev_max_index = 0
        for i in range(len(weights)):
            if weights[i] > 0 and values[i]/weights[i] > prev_max:
                prev_max = values[i]/weights[i]
                prev_max_index = i
        a = 0
        if weights[prev_max_index] <  capacity:
            a = weights[prev_max_index]
        else:
            a = capacity
        value = value + (a * (values[prev_max_index]/weights[prev_max_index]))
        weights[prev_max_index] = weights[prev_max_index] - a
        capacity = capacity - a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
