import time

def bubble_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawrectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])


def insertion_sort(data, drawrectangle, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawrectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))])
            time.sleep(delay)
        data[j + 1] = key
        drawrectangle(data, ['blue' if x == i else 'red' for x in range(len(data))])
    drawrectangle(data, ['blue' for x in range(len(data))])


def selection_sort(data, drawrectangle, delay):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
            drawrectangle(data, ['blue' if x == min_idx or x == j else 'red' for x in range(len(data))])
            time.sleep(delay)
        data[i], data[min_idx] = data[min_idx], data[i]
        drawrectangle(data, ['blue' if x == i or x == min_idx else 'red' for x in range(len(data))])
    drawrectangle(data, ['blue' for x in range(len(data))])


def merge_sort(data, drawrectangle, delay):
    merge_sort_alg(data, 0, len(data)-1, drawrectangle, delay)
    drawrectangle(data, ['blue' for x in range(len(data))])

def merge_sort_alg(data, left, right, drawrectangle, delay):
    if left < right:
        mid = (left + right) // 2
        merge_sort_alg(data, left, mid, drawrectangle, delay)
        merge_sort_alg(data, mid + 1, right, drawrectangle, delay)
        merge(data, left, mid, right, drawrectangle, delay)

def merge(data, left, mid, right, drawrectangle, delay):
    left_part = data[left:mid + 1]
    right_part = data[mid + 1:right + 1]
    left_idx = right_idx = 0
    sorted_idx = left

    while left_idx < len(left_part) and right_idx < len(right_part):
        if left_part[left_idx] <= right_part[right_idx]:
            data[sorted_idx] = left_part[left_idx]
            left_idx += 1
        else:
            data[sorted_idx] = right_part[right_idx]
            right_idx += 1
        sorted_idx += 1

    while left_idx < len(left_part):
        data[sorted_idx] = left_part[left_idx]
        left_idx += 1
        sorted_idx += 1

    while right_idx < len(right_part):
        data[sorted_idx] = right_part[right_idx]
        right_idx += 1
        sorted_idx += 1

    drawrectangle(data, ['blue' if left <= x <= right else 'red' for x in range(len(data))])
    time.sleep(delay)


def quick_sort(data, drawrectangle, delay):
    quick_sort_alg(data, 0, len(data) - 1, drawrectangle, delay)
    drawrectangle(data, ['blue' for x in range(len(data))])

def quick_sort_alg(data, low, high, drawrectangle, delay):
    if low < high:
        pivot_index = partition(data, low, high, drawrectangle, delay)
        quick_sort_alg(data, low, pivot_index - 1, drawrectangle, delay)
        quick_sort_alg(data, pivot_index + 1, high, drawrectangle, delay)

def partition(data, low, high, drawrectangle, delay):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            drawrectangle(data, ['blue' if x == i or x == j else 'red' for x in range(len(data))])
            time.sleep(delay)
    data[i + 1], data[high] = data[high], data[i + 1]
    drawrectangle(data, ['blue' if x == i + 1 or x == high else 'red' for x in range(len(data))])
    time.sleep(delay)
    return i + 1
