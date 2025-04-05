from math import sqrt
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points in 2D space.
    
    Args:
        point1 (Tuple[float, float]): The first point (x1, y1).
        point2 (Tuple[float, float]): The second point (x2, y2).
        
    Returns:
        float: The distance between the two points.
    """
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def plot_points(points: List[Tuple[float, float]], title: str = "Points Plot") -> None:
    """
    Plot a list of points in 2D space. 
    Each point is represented as a tuple (x, y).
    
    Args:
        points (List[Tuple[float, float]]): List of points to plot.
        title (str): Title of the plot.
    """
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, color='blue', marker='o')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def calculate_mean(points: List[Tuple[float, float]]) -> Tuple[float, float]:
    """
    Calculate the mean of a list of points in 2D space.
    
    Args:
        points (List[Tuple[float, float]]): List of points to calculate the mean.
        
    Returns:
        Tuple[float, float]: The mean point (mean_x, mean_y).
    """
    if not points:
        return (0.0, 0.0)
    
    mean_x = np.mean([point[0] for point in points])
    mean_y = np.mean([point[1] for point in points])
    
    return (mean_x, mean_y)