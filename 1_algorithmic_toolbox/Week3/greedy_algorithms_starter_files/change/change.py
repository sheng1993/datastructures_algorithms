# Uses python3
import sys

coins = [10, 5, 1]


def get_change(m):
    curr_val = 0
    coins_count = 0
    for i in range(len(coins)):
        cur_coin_count = (m - curr_val) // coins[i]
        if cur_coin_count > 0:
            coins_count = coins_count + cur_coin_count
            curr_val = curr_val + cur_coin_count * coins[i]
        if m == curr_val:
            break;
    return coins_count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
