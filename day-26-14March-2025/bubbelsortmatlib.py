import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort_visual(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align="edge")

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                # Update the bars
                for bar, val in zip(bars, arr):
                    bar.set_height(val)
                plt.pause(0.1)  # Small pause to show sorting step

    plt.show()

# Example Array
arr = np.random.randint(1, 100, 10)  # Random numbers
bubble_sort_visual(arr)
