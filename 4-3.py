import random
import time
import matplotlib.pyplot as plt

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Radix Sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Counting Sort
def counting_sort_direct(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    arr.clear()
    for i in range(len(count)):
        arr.extend([i] * count[i])
    return arr

def compare_sort():
    sizes = [1000, 5000, 10000, 20000]  # ขนาดข้อมูลที่ใช้ทดสอบ
    bubble_times = []
    insertion_times = []
    selection_times = []
    shell_times = []
    quick_times = []
    merge_times = []
    radix_times = []
    counting_times = []
    
    for size in sizes:
        data = [random.randint(0, 999999) for _ in range(size)]  # ข้อมูล 0-999999
        
        # วัดเวลา Bubble Sort
        start_time = time.time()
        bubble_sort(data.copy())
        bubble_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา Insertion Sort
        start_time = time.time()
        insertion_sort(data.copy())
        insertion_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Selection Sort
        start_time = time.time()
        selection_sort(data.copy())
        selection_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Shell Sort
        start_time = time.time()
        shell_sort(data.copy())
        shell_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Quick Sort
        start_time = time.time()
        quick_sort(data.copy())
        quick_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Merge Sort
        start_time = time.time()
        merge_sort(data.copy())
        merge_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Radix Sort
        start_time = time.time()
        radix_sort(data.copy())
        radix_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Counting Sort
        start_time = time.time()
        counting_sort_direct(data.copy())
        counting_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Bubble Sort: {bubble_times[-1]:.2f} มิลลิวินาที")
        print(f"  Insertion Sort: {insertion_times[-1]:.2f} มิลลิวินาที")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")
        print(f"  Merge Sort: {merge_times[-1]:.2f} มิลลิวินาที")
        print(f"  Radix Sort: {radix_times[-1]:.2f} มิลลิวินาที")
        print(f"  Counting Sort: {counting_times[-1]:.2f} มิลลิวินาที")

    # วาดกราฟเปรียบเทียบ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort', linestyle='--')
    plt.plot(sizes, insertion_times, marker='d', label='Insertion Sort', linestyle='-.')
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort', linestyle='-')
    plt.plot(sizes, shell_times, marker='^', label='Shell Sort', linestyle=':')
    plt.plot(sizes, quick_times, marker='p', label='Quick Sort', linestyle='-.')
    plt.plot(sizes, merge_times, marker='x', label='Merge Sort', linestyle='--')
    plt.plot(sizes, radix_times, marker='v', label='Radix Sort', linestyle='-.')
    plt.plot(sizes, counting_times, marker='h', label='Counting Sort', linestyle='-')
    plt.title('Comparison of Sorting Algorithms (Random Data 0-999999). Created By [Suphawadee]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Sorting_Performance_Comparison.png')  # บันทึกเป็นรูปภาพ
    plt.show()

# เปรียบเทียบประสิทธิภาพ
compare_sort()
