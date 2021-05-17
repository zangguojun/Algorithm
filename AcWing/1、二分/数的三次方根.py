n = float(input())
def search(l, r, n):
    while r - l > 1e-8:
        mid = (l + r) / 2
        # q[mid] * q[mid] * q[mid] >= x
        if mid**3 >= n: r = mid
        else: l = mid
    return l
print("{:.6f}".format(search(-10000, 10000, n)))
