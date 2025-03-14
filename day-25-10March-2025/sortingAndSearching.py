def sorting(arr):
    """
    Sorting is the process of arranging elements in a specific order, typically in ascending or descending order.
    This function takes an array as input and returns a sorted array using a sorting algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list of elements.
    """
    return sorted(arr)

def searching(arr, target):
    """
    Searching is the process of finding the position of a specific element within a collection of elements.
    This function takes an array and a target value as input and returns the index of the target value if found, otherwise -1.
    
    Parameters:
    arr (list): The list of elements to search within.
    target: The element to search for.
    
    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    try:
        return arr.index(target)
    except ValueError:
        return -1