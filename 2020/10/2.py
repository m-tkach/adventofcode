from functools import lru_cache


def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def dp(a):
    @lru_cache(maxsize=None)
    def f(i):
        if i == 0:
            return 1
        s = 0
        j = i - 1
        while j >= 0 and a[i] - a[j] < 4:
            s += f(j)
            j -= 1
        return s
    return f(len(a) - 1)


def process(a):
    a = sorted((a:=list(map(int, a))) + [0, max(a) + 3])
    return dp(a)


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
