"""
Sorting in Python

Definition:
Sorting is the process of arranging data in a particular order, typically in ascending or descending order. Sorting is a common operation in programming and is used to organize data for efficient searching, retrieval, and analysis.

Examples and Syntax:
Python provides several ways to sort data, including built-in functions and methods. Here are some examples:

1. Using the sorted() function:
The sorted() function returns a new sorted list from the elements of any iterable.

Example:
"""
# Example of sorted() function
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("Sorted list:", sorted_numbers)

"""
2. Using the sort() method:
The sort() method sorts the list in place and returns None.

Example:
"""
# Example of sort() method
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print("Sorted list:", numbers)

"""
3. Sorting with a custom key:
Both sorted() and sort() can take a key parameter to specify a function to be called on each list element prior to making comparisons.

Example:
"""
# Example of sorting with a custom key
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print("Sorted list by length:", sorted_words)

"""
Flow Chart:
Below is a simple flow chart representing the sorting process:

    Start
      |
  [Input List]
      |
  [Choose Sorting Method]
      |
  [Apply Sorting Algorithm]
      |
  [Sorted List]
      |
     End

Conclusion:
Sorting is a fundamental operation in programming that helps in organizing data. Python provides easy-to-use functions and methods to perform sorting, making it a powerful tool for data manipulation and analysis.
"""
"""
4. Sorting in descending order:
You can sort in descending order by using the reverse parameter.

Example:
"""
# Example of sorting in descending order
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Sorted list in descending order:", sorted_numbers_desc)

"""
5. Sorting a list of tuples:
You can sort a list of tuples by specifying the index of the tuple to sort by.

Example:
"""
# Example of sorting a list of tuples
students = [("John", 22), ("Jane", 21), ("Dave", 25)]
sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted list of students by age:", sorted_students)

"""
6. Sorting a dictionary by keys:
You can sort a dictionary by its keys using the sorted() function.

Example:
"""
# Example of sorting a dictionary by keys
student_ages = {"John": 22, "Jane": 21, "Dave": 25}
sorted_student_ages = dict(sorted(student_ages.items()))
print("Sorted dictionary by keys:", sorted_student_ages)

"""
7. Sorting a dictionary by values:
You can sort a dictionary by its values using the sorted() function.

Example:
"""
# Example of sorting a dictionary by values
sorted_student_ages_by_value = dict(sorted(student_ages.items(), key=lambda item: item[1]))
print("Sorted dictionary by values:", sorted_student_ages_by_value)

"""
Types of Sorting in Data Structures and Algorithms (DSA):

1. Bubble Sort:
Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

Example:
"""
# Example of Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Bubble Sorted list:", sorted_numbers)

"""
2. Selection Sort:
Selection Sort is an in-place comparison-based sorting algorithm. It divides the input list into two parts: the sublist of items already sorted, which is built up from left to right, and the sublist of items remaining to be sorted. It repeatedly selects the smallest (or largest) element from the unsorted sublist, swaps it with the leftmost unsorted element, and moves the sublist boundaries one element to the right.

Example:
"""
# Example of Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print("Selection Sorted list:", sorted_numbers)

"""
3. Insertion Sort:
Insertion Sort is a simple comparison-based sorting algorithm. It builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Example:
"""
# Example of Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

numbers = [12, 11, 13, 5, 6]
sorted_numbers = insertion_sort(numbers)
print("Insertion Sorted list:", sorted_numbers)

"""
4. Merge Sort:
Merge Sort is a divide-and-conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves.

Example:
"""
# Example of Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

numbers = [12, 11, 13, 5, 6, 7]
sorted_numbers = merge_sort(numbers)
print("Merge Sorted list:", sorted_numbers)

"""
5. Quick Sort:
Quick Sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. A large array is partitioned into two arrays, one of which holds values smaller than the specified value, say pivot, based on which the partition is made and another array holds values greater than the pivot value.

Example:
"""
# Example of Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

numbers = [10, 7, 8, 9, 1, 5]
sorted_numbers = quick_sort(numbers)
print("Quick Sorted list:", sorted_numbers)