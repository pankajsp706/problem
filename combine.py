
def overlap_ratio(a, b):
    left = max(a[0], b[0])
    right = min(a[1], b[1])
    overlap = max(0, right - left)
    length_a = a[1] - a[0]
    return overlap / length_a if length_a else 0

def combine_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []

    while combined:
        current = combined.pop(0)
        i = 0
        while i < len(combined):
            if overlap_ratio(current['positions'], combined[i]['positions']) > 0.5:
                current['values'] += combined[i]['values']
                current['positions'][1] = max(current['positions'][1], combined[i]['positions'][1])
                combined.pop(i)
            else:
                i += 1
        result.append(current)
    return result

# Example usage
if __name__ == "__main__":
    list1 = [{"positions": [0, 5], "values": [1, 2]}]
    list2 = [{"positions": [3, 7], "values": [3, 4]}]
    merged = combine_lists(list1, list2)
    print(merged)
