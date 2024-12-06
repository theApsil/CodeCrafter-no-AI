# Python: быстрая сортировка
elements = [111, 22, 413, 44, 56, 989]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if isinstance(x, str) and isinstance(pivot, str):
            if x.lower() < pivot.lower():
                left.append(x)
            elif x.lower() == pivot.lower():
                middle.append(x)
            else:
                right.append(x)
        else:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
    return quicksort(left) + middle + quicksort(right)

sorted_elements = quicksort(elements)
print(sorted_elements)