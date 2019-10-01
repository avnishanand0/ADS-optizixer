'''test'''

from sys import stdin, stdout


def find_unsorted_subarray(ar, n):
    i = 1
    start = end = 0
    first = 1
    while i < n:
        if ar[i] <= ar[i-1]:
            flag = 0
            j=i
            while j > 0 and ar[j] < ar[j-1]:
                flag = 1
                ar[j], ar[j-1] = ar[j-1], ar[j]
                j -= 1
            if flag:
                if first:
                    first = 0
                    start = j
                    end = i
                else:
                    if j < start:
                        start = j
                    end = i

        i += 1

    return start, end

t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    ar = [int(i) for i in stdin.readline().split()]
    x, y = find_unsorted_subarray(ar, n)
    stdout.write(str(x) + " " + str(y) + "\n")
    t -= 1
