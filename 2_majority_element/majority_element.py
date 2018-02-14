# Uses python3
import sys

def get_majority_element(a, right):
    counter = {}
    majority = right // 2
    for i in a:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
        if counter[i] > majority:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)
