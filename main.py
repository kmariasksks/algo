def min_speed(piles, H):
    def is_possible(K):
        hours = 0
        for pile in piles:
            hours += (pile + K - 1) // K
        return hours <= H

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if is_possible(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(min_speed([3, 6, 7, 11], 8))
print(min_speed([30, 11, 23, 4, 20], 5))
print(min_speed([30, 11, 23, 4, 20], 6))