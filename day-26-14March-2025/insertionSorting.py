def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

data = [8, 4, 5, 2, 9]
insertion_sort(data)
print("Sorted Array:", data)




# # import matplotlib.pyplot as plt
# # import numpy as np
# # import time

# # def insertion_sort_visual(arr):
# #     fig, ax = plt.subplots()
# #     bars = ax.bar(range(len(arr)), arr, align="edge")

# #     for i in range(1, len(arr)):
# #         key = arr[i]
# #         j = i - 1

# #         while j >= 0 and key < arr[j]:
# #             arr[j + 1] = arr[j]
# #             j -= 1
# #             arr[j + 1] = key

# #             # Update bars
# #             for bar, val in zip(bars, arr):
# #                 bar.set_height(val)
# #             plt.pause(0.2)  # Pause for visualization

# #     plt.show()

# # # Example Array
# # arr = np.random.randint(1, 100, 10)  # Generate 10 random numbers
# # insertion_sort_visual(arr)



import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Insertion Sort Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BAR_COLOR = (50, 150, 255)

# Generate random array
arr = [random.randint(10, 300) for _ in range(20)]

def draw_array(arr):
    screen.fill(WHITE)
    bar_width = width // len(arr)
    for i, val in enumerate(arr):
        pygame.draw.rect(screen, BAR_COLOR, (i * bar_width, height - val, bar_width, val))
    pygame.display.update()

def insertion_sort_visual(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
            draw_array(arr)
            pygame.time.delay(100)  # Delay for visualization

running = True
while running:
    screen.fill(WHITE)
    draw_array(arr)
    insertion_sort_visual(arr)
    running = False  # Stop the loop after sorting

pygame.quit()



# # VisuAlgo (Insertion Sort)

def insertionSort(list):
    for i in range(1,len(list)):
        j=i 
        while list[j-1] > list[j] and j > 0:
            list[j-1],list[j]=list[j],list[j-1]
            j-=1
            
list=[1,3,5,7,9,2,6,8]
insertionSort(list)
print(list)
