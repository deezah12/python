def two_sum(arr: list, target: int) -> list:
    from itertools import permutations

    solutions = [pair for pair in permutations(arr, 2) if sum(pair) == target]
    print('Solutions:', solutions)
    return solutions


numbers = [3, -1, 5, 4]
target_number = 3

print(two_sum(numbers, target_number))


def two_sum(arr: list, target: int) -> list:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]


numbers = [3, -1, 5, 4]
target_number = 8
print(two_sum(numbers, target_number))
