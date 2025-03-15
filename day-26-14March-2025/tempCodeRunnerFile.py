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