n = int(input())

longest_intersection_numbers = {}

for i in range(n):

    right_range, left_range = input().split("-")

    left_range_start_idx, left_range_end_idx = tuple(map(int, left_range.split(",")))

    right_range_start_idx, right_range_end_idx = tuple(map(int, right_range.split(",")))

    left_set = {num for num in range(left_range_start_idx, left_range_end_idx + 1)}

    right_set = {num for num in range(right_range_start_idx, right_range_end_idx + 1)}

    intersection = left_set & right_set

    if len(intersection) > len(longest_intersection_numbers):

        longest_intersection_numbers = intersection

print(f"Longest intersection is [{', '.join(map(str, {i for i in longest_intersection_numbers}))}] with length {len(longest_intersection_numbers)}")