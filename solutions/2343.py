def subarray_max(arr, m):
    def count_subarrays(max_sum):
        count = 1
        current_sum = 0
        for num in arr:
            current_sum += num
            if current_sum > max_sum:
                count += 1
                current_sum = num
        return count

    left, right = max(arr), sum(arr)

    while left <= right:
        mid = (left + right) // 2
        subarray_count = count_subarrays(mid)

        if subarray_count <= m:
            right = mid - 1
        else:
            left = mid + 1

    return left


n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = subarray_max(arr, m)
print(result)
